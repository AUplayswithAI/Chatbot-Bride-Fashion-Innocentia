from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatbot_logic import handle_customer_query
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').strip()
    reply = handle_customer_query(incoming_msg)

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
