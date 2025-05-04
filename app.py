from flask import Flask, request
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return "IG ChatGPT Bot is running."

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return {"reply": "沒收到訊息喔～"}

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    reply = response.choices[0].message.content.strip()
    return {"reply": reply}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
