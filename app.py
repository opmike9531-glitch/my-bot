from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

# --- STYLES (Deep Black & Glowing Pink) ---
STYLE = """
<style>
    body { background-color: #020202; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; overflow: hidden; }
    .card { background: #080808; padding: 40px; border-radius: 24px; text-align: center; box-shadow: 0 0 50px rgba(255, 20, 147, 0.2); width: 90%; max-width: 400px; border: 1px solid #1a1a1a; display: flex; flex-direction: column; gap: 15px; box-sizing: border-box; }
    h1 span { color: #ff1493; text-shadow: 0 0 15px rgba(255, 20, 147, 0.7); font-weight: 800; }
    .step { background: #111; padding: 15px; border-radius: 12px; text-align: left; border-left: 4px solid #ff1493; font-size: 14px; color: #ccc; }
    .btn-glow { background: #ff1493; color: white; padding: 16px; border-radius: 30px; font-weight: bold; text-decoration: none; border: none; width: 100%; cursor: pointer; text-transform: uppercase; box-shadow: 0 0 20px rgba(255, 20, 147, 0.4); display: block; margin-top: 10px; }
    .btn-glow:hover { transform: scale(1.02); background: #ff4da6; }
</style>
"""

@app.route('/')
def home():
    # REPLACE with your ACTUAL render link
    render_url = "https://ixl-bot-v2.onrender.com"
    
    # This is the "mret" injector script
    bookmarklet = f"javascript:(function(){{var s=document.createElement('script');s.src='{render_url}/inject.js';document.body.appendChild(s);}})();"

    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h1>ixl-<span>flow</span></h1>
            <div class="step"><strong>1.</strong> Log in to IXL in a new tab.</div>
            <div class="step"><strong>2.</strong> Drag the button below to your bookmarks bar.</div>
            <a class="btn-glow" href="{bookmarklet}">IXL FLOW</a>
            <p style="font-size:10px; color:#444;">Click the bookmark while on an IXL skill page.</p>
        </div>
    </body></html>
    """)

@app.route('/inject.js')
def inject_js():
    # This is the code that actually opens the solver window on IXL
    return """
    (function() {
        if(document.getElementById('flow-window')) return;
        var div = document.createElement('div');
        div.id = 'flow-window';
        div.style = 'position:fixed; top:20px; right:20px; width:250px; background:#080808; border:2px solid #ff1493; border-radius:15px; z-index:999999; padding:15px; color:white; font-family:sans-serif; box-shadow:0 0 20px #ff1493;';
        div.innerHTML = '<h2 style="color:#ff1493; margin:0; font-size:18px;">ixl-flow</h2><hr style="border:1px solid #222;"><p id="flow-ans" style="font-size:14px;">Waiting for question...</p>';
        document.body.appendChild(div);
        
        setInterval(function() {
            var q = document.querySelector('.question-component');
            if(q) document.getElementById('flow-ans').innerText = 'Answer: Calculating...';
        }, 3000);
    })();
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
