from rasa_core.channels.socketio import SocketIOInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter

# load your trained agent
agent = Agent.load('D:/Saxion/_Year_3/Minor_Skilled/NPC/Chatbot/models/current/dialogue', interpreter=RegexInterpreter())

input_channel = SocketIOInput(
        # event name for messages sent from the user
        user_message_evt="user_uttered",
        # event name for messages sent from the bot
        bot_message_evt="bot_uttered",
        # socket.io namespace to use for the messages
        namespace=None
)

# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], 5005, serve_forever=True)