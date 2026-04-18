from flask import Flask, request, jsonify
import asyncio
from bot import solve_ixl

app = Flask(__name__)

@app.route('/')
def home():
    return "IXL Bot is Online and Ready!"

@app.route('/run', methods=['POST'])
def run_bot():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    skill_url = data.get('skill_url')

    if not username or not password or not skill_url:
        return jsonify({"error": "Missing info!"}), 400

    # This runs your bot.py logic in the background
    try:
        asyncio.run(solve_ixl(username, password, skill_url))
        return jsonify({"status": "Bot started successfully!"})
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
