import argparse
import warnings

from rasa_core import config
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter, RegexInterpreter, RasaNLUHttpInterpreter
from rasa_core.channels.console import CmdlineInput
from rasa_core.channels.socketio import SocketIOInput
from rasa_core.channels.channel import RestInput

nluModelDir = "models/current/nlu"
domainFile = "domain.yml"
trainingStories = "data/stories/stories.md"
modelPath = "models/dialogue"
policies_file = "config_core.yml"



def train():

    policies = config.load(policies_file)

    agent = Agent(domainFile, policies=policies)

    training_data = agent.load_data(trainingStories)

    agent.train(training_data)

    agent.persist(modelPath)

def run(channel = 'console'):

    nlu = "http://localhost:5000"

    interpreter = None
    if (channel == 'console'):
        interpreter = RasaNLUInterpreter(model_directory = nluModelDir)
    else:
        interpreter = RasaNLUHttpInterpreter(endpoint=nlu)

    agent = Agent.load(modelPath, interpreter=interpreter)

    if (channel == 'console'):
	    agent.handle_channels([CmdlineInput()])
    else:
	    input_channel = SocketIoChannel()
	    agent.handle_channels([input_channel])


def SocketIoChannel():
    
    input_channel = SocketIOInput(
        # event name for messages sent from the user
        user_message_evt="user_uttered",
        # event name for messages sent from the bot
        bot_message_evt="bot_uttered",
        # socket.io namespace to use for the messages
        namespace=None
	)

    return input_channel


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="starts the bot")
    parser.add_argument("-t", choices=["train", "run_console", "run_socket"], help="what the bot should do")
    task = parser.parse_args().t

    if task == "train":
        train()
    elif task == "run_console":
        run()
    elif task == "run_http": 
	    run('http')
    else:
        warnings.warn("Need to pass 'train' or 'run_console' as argument")
        exit(1)
