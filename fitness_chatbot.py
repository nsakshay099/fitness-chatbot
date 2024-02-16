from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Set your OpenAI GPT-3 API key
openai.api_key = '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'

def get_chatbot_response(user_input):
    prompt = f"User: {user_input}\nChatbot:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    chatbot_response = get_chatbot_response(user_input)
    return render_template('index.html', user_input=user_input, chatbot_response=chatbot_response)

if __name__ == '__main__':
    app.run(debug=True)
