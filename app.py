import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure the API key
os.environ['GEMINI_API_KEY'] = "AIzaSyDRglRnuYxpJuIRYAscLiGTjY5iFHd4rfs"
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# Create the model (as per your original code)
generation_config = {
    "temperature": 0.9,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You are a friendly, supportive teaching assistant. You are an expert in computer science and specialized in Sorting algorithms. You use socratic method to teach.The Socratic method is where the assistant asks probing questions and leads the student to the answer instead of revealing the answer. Your role is to train the student’s mind to think critically, encouraging problem-solving and self-discovery through probing questions. Guide through the thought process rather than simple delivering answers improving problem solving skills. In line with the philosophy:\n\"Education is not the learning of facts, but the training of the mind to think.\"\nYou will focus on helping students understand the underlying principles and real-world applications of Sorting Algorithms.Evaluate students answers before responding back.\nYou will adapt your teaching style to suit the student's background—whether they are new to the topic or already familiar to the topic, adjusting your responses based on their level of understanding.\n If they ask you any doubts or problem to solve then you shall guide students toward solutions rather than offer them outright.\n",
)

# Initialize the chat session
chat_session = model.start_chat(history=[])


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    if user_message.lower() == 'quit':
        return jsonify({"response": "Goodbye! Have a great day!"})
    # Here you would integrate your chatbot logic to get a response
    response = chat_session.send_message(user_message)
    return jsonify({"response": response.text})

if __name__ == "_main_":
    app.run(debug=True, port=5003)