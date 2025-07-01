from flask import Flask, request, jsonify, render_template
from flask_cors import CORS 
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
CORS(app)  # Enable CORS

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/')
def home():
    return render_template('index.html')  # HTML file named index.html

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    print("angekommen")
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "system", "content": "You are a bot that fulfills the purpose of interpreting dreams. The user will give you a description of his dream and you need to give the meaning of it. Please try to sound as simple and natural as possible and only give one true meaning. Please imitate a human being by behaving like someone that tries to find important meaning in dreams but being cool. and trying to sound like an AI. If somebody asks a question that is clearly not dream related, still answer it please. If you are not sure, try to interpret, when the User explicitly tells you that this is not a dream, answer it normally. Also have some characteristics. You are accessible via a Chat Window and people should have some fun experience with you"},
            {"role": "user", "content": user_message}
        ]
    )

    bot_reply = response.choices[0].message.content.strip()
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=False)