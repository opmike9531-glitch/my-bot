import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app) # This line stops the "Check Render" error

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        data = request.json
        q_text = data.get('question', '')
        choices = data.get('choices', '')
        
        prompt = f"IXL Math. Question: {q_text}. Choices: {choices}. Return ONLY the exact text of the correct choice."
        
        response = model.generate_content(prompt)
        return jsonify({"answer": response.text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
