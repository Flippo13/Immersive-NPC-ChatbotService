import argparse
import warnings
import logging

from flask import Flask
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from threading import Thread
from typing import Text, Optional, List


import rasa_core
from rasa_core import constants, agent
from rasa_core import config
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.channels import (
    console, InputChannel,
    BUILTIN_CHANNELS)
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter, RegexInterpreter, RasaNLUHttpInterpreter
from rasa_core.channels.console import CmdlineInput
from rasa_core.channels.socketio import SocketIOInput
from rasa_core.channels.channel import RestInput
from rasa_core.utils import read_yaml_file, AvailableEndpoints

logger = logging.getLogger()  # get the root logger

nluModelDir = "models/current/nlu"
domainFile = "domain/domain.yml"
stories = "stories/"
modelPath = "models/dialogue"
policies_file = "config_core.yml"
credentials = "credentials.yml"
endpointsFile = "endpoints.yml"

def train_core():
    policies = config.load(policies_file)

    agent = Agent(domainFile, policies=policies)

    training_data = agent.load_data(stories)

    agent.train(training_data)

    agent.persist(modelPath)

def create_http_input_channels(
    channel: Optional[Text], 
    credentials_file: Optional[Text]
    ) -> List[InputChannel]:

    all_credentials = read_yaml_file(credentials_file)

    return [_create_single_channel(c,k) for c,k in all_credentials.items()]


def _create_single_channel(channel, credentials):
    if channel in BUILTIN_CHANNELS:
        return BUILTIN_CHANNELS[channel].from_credentials(credentials)


def start_server(agent, input_channels, port, cors):

    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": cors or ""}})

    rasa_core.channels.channel.register(input_channels, app, agent.handle_message, route="/webhooks/")

    http_server = WSGIServer(('0.0.0.0', port), app)
    http_server.start()
    return http_server

def run(agent, channel = None, port=constants.DEFAULT_SERVER_PORT, credentials_file = None, cors = None):
    if not channel and not credentials_file:
        channel = "cmdline"

    input_channels = create_http_input_channels(channel,credentials_file)

    http_server = start_server(agent, input_channels, port, cors)

    try:
        http_server.serve_forever()
    except Exception as exc:
        logger.exception(exc)

def load_agent(core_model, endpoints):
    return Agent.load(core_model, interpreter = RegexInterpreter(),action_endpoint=endpoints.action, tracker_store=endpoints.tracker_store)


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="starts the bot")
    parser.add_argument("-t", choices=["train", "run"], help="what the bot should do")
    task = parser.parse_args().t
    if task == "train":
        train_core()
    elif task == "run":
        endpoint = AvailableEndpoints.read_endpoints(endpointsFile)
        agent = load_agent(modelPath, endpoint)
        run(agent, credentials_file=credentials)
    else:
        warnings.warn("Need to pass 'train' or 'run_console' as argument")
        exit(1)

    