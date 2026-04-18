from flask import Flask, request, render_template_string

app = Flask(__name__)

# --- STYLES ---
STYLE = """
<style>
    body { background-color: #020202; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .card { background: #080808; padding: 40px; border-radius: 24px; text-align: center; box-shadow: 0 0 50px rgba(255, 20, 147, 0.2); width: 100%; max-width: 380px; border: 1px solid #1a1a1a; display: flex; flex-direction: column; gap: 15px; box-sizing: border-box; }
    h1 span, h2 { color: #ff1493; text-shadow: 0 0 15px rgba(255, 20, 147, 0.7); font-weight: 800; margin: 0; }
    .step { background: #111; padding: 15px; border-radius: 12px; text-align: left; border-left: 4px solid #ff1493; font-size: 14px; }
    .btn-glow { background: #ff1493; color: white; padding: 16px; border-radius: 30px; font-weight: bold; text-decoration: none; border: none; width: 100%; cursor: pointer; text-transform: uppercase; box-shadow: 0 0 20px rgba(255, 20, 147, 0.4); box-sizing: border-box; display: block; }
    ul { list-style: none; padding: 0; text-align: left; margin: 0; }
    li { margin: 12px 0; color: #ff1493; font-size: 14px; font-weight: bold; animation: pulse 1.5s infinite; display: flex; align-items: center; }
    .dot { height: 6px; width: 6px; border-radius: 50%; display: inline-block; margin-right: 12px; background: #ff1493; box-shadow: 0 0 15px #ff1493; }
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
            <div class="step"><strong>2.</strong> Use the button below to link:</div>
            <a class="btn-glow" href="/run_sync">LINK IXL DASHBOARD</a>
        </div>
    </body></html>
    """)

@app.route('/run_sync')
def run():
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2>syncing...</h2>
            <ul>
                <li><span class="dot"></span>establishing socket connection</li>
                <li><span class="dot"></span>pulling ixl metadata</li>
                <li><span class="dot"></span>injecting dashboard v2.1</li>
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
