from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

# --- STYLES ---
STYLE = """
<style>
    body { background-color: #020202; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .card { background: #080808; padding: 40px; border-radius: 24px; text-align: center; box-shadow: 0 0 50px rgba(255, 20, 147, 0.2); width: 90%; max-width: 400px; border: 1px solid #1a1a1a; display: flex; flex-direction: column; gap: 15px; }
    h1 span { color: #ff1493; text-shadow: 0 0 15px rgba(255, 20, 147, 0.7); font-weight: 800; }
    .step { background: #111; padding: 15px; border-radius: 12px; text-align: left; border-left: 4px solid #ff1493; font-size: 14px; color: #ccc; }
    .btn-glow { background: #ff1493; color: white; padding: 16px; border-radius: 30px; font-weight: bold; text-decoration: none; border: none; width: 100%; cursor: pointer; text-transform: uppercase; box-shadow: 0 0 20px rgba(255, 20, 147, 0.4); display: block; }
</style>
"""

@app.route('/')
def home():
    # MAKE SURE THIS IS YOUR ACTUAL RENDER URL
    render_url = "https://ixl-bot-v2.onrender.com"
    
    # This is the "Loader" - it forces the browser to fetch the logic from your server
    bookmarklet = f"javascript:(function(){{var s=document.createElement('script');s.src='{render_url}/inject.js?v='+Math.random();document.body.appendChild(s);}})();"

    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h1>ixl-<span>flow</span></h1>
            <div class="step"><strong>1.</strong> Drag the button to your bookmarks.</div>
            <a class="btn-glow" href="{bookmarklet}">IXL FLOW</a>
            <div class="step"><strong>2.</strong> Go to IXL and click it.</div>
        </div>
    </body></html>
    """)

@app.route('/inject.js')
def inject_js():
    # This is the actual logic that opens the window on IXL
    return """
    (function() {
        if(document.getElementById('flow-window')) {
            alert('Flow already active!');
            return;
        }
        var div = document.createElement('div');
        div.id = 'flow-window';
        div.style = 'position:fixed; top:20px; right:20px; width:260px; background:#080808; border:2px solid #ff1493; border-radius:15px; z-index:9999999; padding:15px; color:white; font-family:sans-serif; box-shadow:0 0 20px #ff1493; cursor:move;';
        div.innerHTML = '<h2 style="color:#ff1493; margin:0; font-size:18px; text-align:center;">ixl-flow</h2><hr style="border:1px solid #222; margin:10px 0;"><p id="flow-ans" style="font-size:14px; text-align:center;">Scanning Question...</p>';
        document.body.appendChild(div);

        // Make it draggable
        div.onmousedown = function(e) {
            var oX = e.clientX - div.offsetLeft;
            var oY = e.clientY - div.offsetTop;
            document.onmousemove = function(e) {
                div.style.left = (e.clientX - oX) + 'px';
                div.style.top = (e.clientY - oY) + 'px';
            };
            document.onmouseup = function() { document.onmousemove = null; };
        };

        // Real-time "Detection" Simulation
        setInterval(function() {
            var q = document.querySelector('.question-component') || document.querySelector('.practice-area');
            if(q) {
                document.getElementById('flow-ans').innerHTML = 'Answer Found: <br><span style="color:#ff1493; font-weight:bold;">g(x) = f(x) - 1</span>';
            } else {
                document.getElementById('flow-ans').innerText = 'Open a skill to start...';
            }
        }, 2000);
    })();
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
