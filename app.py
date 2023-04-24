from flask import Flask, request, jsonify, render_template

import openai

app = Flask(__name__)


# Setting up the OpenAI API
openai.api_key = "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"

def generate_response(prompt):
    # Set up the OpenAI completion API parameters
    model_engine = "text-davinci-002"
    prompt = prompt.strip()
    temperature = 0.7
    max_tokens = 1024
    top_p = 1
    frequency_penalty = 0
    presence_penalty = 0

    # Generate the response from the OpenAI API
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    # Extract the response text from the OpenAI API response
    message = response.choices[0].text.strip()

    return message

@app.route('/chat', methods=['POST'])
def chat():
    # Retrieve the user's input from the form
    user_input = request.form['text']

    # Generate a response from the OpenAI API
    bot_response = generate_response(user_input)

    # Return the response as a JSON object
    return jsonify({'text': bot_response})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



