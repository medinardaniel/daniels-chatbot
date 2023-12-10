from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os

# Housekeeping
app = Flask(__name__)
CORS(app, supports_credentials=True)
# Load .env file
load_dotenv()
try:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
except:
    print("Error: Please set your OpenAI API key in the .env file.")

# Function to read text from a Markdown file and return it as a string
def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():

    # Get the data from the request
    data = request.get_json()
    # Get the message from the data
    user_message = data.get("message")

    # Get context from markdown file
    background = read_markdown_file("my_background.md")
    # Create the prompt
    context=f"You are a helpful assistant that answers questions based on the information below. " \
            f"Make sure to always answer confidently, in third person, and in a friendly demeanor. " \
            f"Keep a conversational tone by making answers short and concise. Do not answer in more that 80 words. " \
            f"If the question can't be answered with the information below, tell the user you don't know.\n{background}"

    try:
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": user_message}
            ]
        )

        # Get the response from the completion
        response = completion.choices[0].message.content

        # Check if the reply is empty, indicating the question may be out of context
        if not response:
            response = "I am sorry, but I am not equipped to answer that question."
    except Exception as e:
        print("In Exception!")
        return jsonify({"error": str(e)}), 500

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)