from flask import Flask, request, jsonify, render_template_string
import asyncio
from bot import solve_ixl

app = Flask(__name__)

# The new "ixl-flow" Dashboard
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>ixl-flow | Sync</title>
    <style>
        body { background-color: #050505; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: #0d0d0d; padding: 40px; border-radius: 20px; text-align: center; box-shadow: 0 0 30px rgba(0, 255, 127, 0.1); width: 400px; border: 1px solid #1a1a1a; }
        h1 span { color: #00ff7f; text-shadow: 0 0 10px rgba(0, 255, 127, 0.5); }
        .step { background: #141414; padding: 15px; border-radius: 10px; margin: 10px 0; text-align: left; border-left: 4px solid #00ccff; }
        code { color: #00ff7f; font-family: monospace; font-size: 12px; word-break: break-all; }
        .btn-glow { background: linear-gradient(90deg, #00ff7f, #00ccff); color: #000; padding: 10px; border-radius: 5px; font-weight: bold; text-decoration: none; display: inline-block; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Sync <span>ixl-flow</span></h1>
        <div class="step">
            <strong>Step 1:</strong> Log in to IXL normally in a new tab.
        </div>
        <div class="step">
            <strong>Step 2:</strong> Drag this button to your Bookmarks Bar: <br>
            <a class="btn-glow" href="javascript:(function(){alert('Syncing to ixl-flow...'); fetch('https://ixl-bot-v2.onrender.com/sync', {method:'POST', body: JSON.stringify({url: window.location.href}), headers:{'Content-Type': 'application/json'}});})();">IXL SYNC</a>
        </div>
        <p style="font-size: 12px; color: #444;">Once clicked on IXL, your dashboard will link automatically.</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/sync', methods=['POST'])
def sync_data():
    data = request.get_json()
    # This is where the bookmark sends the IXL page info to your bot
    print(f"Sync received for: {data.get('url')}")
    return jsonify({"status": "connected"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
