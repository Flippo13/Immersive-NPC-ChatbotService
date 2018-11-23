import logging
from flask import Blueprint, request, jsonify
from rasa_core.channels.channel import UserMessage
from rasa_core.channels.channel import CollectingOutputChannel
from rasa_core.channels.channel import InputChannel

logger = logging.getLogger(__name__)

class CustomWebChannel(InputChannel):
    """A simple web bot that listens on url and responds"""

    def blueprint(self, on_new_message):
        custom_webhook = Blueprint('custom_webhook', __name__)

        @custom_webhook.route("/",methods=['GET'])
        def health():
            return jsonify({"status" : "ok"})

        @custom_webhook.route("/post_message", methods=['POST'])
        def recieve():
            payload = request.json
            sender_id = payload.get("sender",None)
            text = payload.get("message", None)
            out = CollectingOutputChannel()
            on_new_message(UserMessage(text, out, sender_id))
            responses = [m for _, m in out.messages]
            return jsonify(responses)
    
    
        return custom_webhook 