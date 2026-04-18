from flask import Flask, request, render_template_string, jsonify
import json

app = Flask(__name__)

# --- STYLES (Deep Black & Glowing Pink) ---
STYLE = """
<style>
    body { background-color: #020202; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; overflow: hidden; }
    .card { background: #080808; padding: 40px; border-radius: 24px; text-align: center; box-shadow: 0 0 50px rgba(255, 20, 147, 0.2); width: 90%; max-width: 380px; border: 1px solid #1a1a1a; display: flex; flex-direction: column; gap: 15px; box-sizing: border-box; }
    h1 span, h2 { color: #ff1493; text-shadow: 0 0 15px rgba(255, 20, 147, 0.7); font-weight: 800; margin: 0; text-transform: lowercase; }
    .step { background: #111; padding: 15px; border-radius: 12px; text-align: left; border-left: 4px solid #ff1493; font-size: 13px; line-height: 1.4; }
    .btn-glow { background: #ff1493; color: white; padding: 16px; border-radius: 30px; font-weight: bold; text-decoration: none; border: none; width: 100%; cursor: pointer; text-transform: uppercase; box-shadow: 0 0 20px rgba(255, 20, 147, 0.4); box-sizing: border-box; display: block; transition: 0.2s; }
    .btn-glow:hover { transform: scale(1.02); box-shadow: 0 0 30px rgba(255, 20, 147, 0.6); }
</style>
"""

@app.route('/')
def home():
    # REPLACE with your actual Render URL
    render_url = "https://ixl-bot-v2.onrender.com"
    
    # The MRET-style Injector Bookmarklet
    bookmarklet = f"""javascript:(function(){{
        if(document.getElementById('flow-overlay')) return;
        var div = document.createElement('div');
        div.id = 'flow-overlay';
        div.style = 'position:fixed;top:50px;left:50px;width:280px;height:auto;background:#080808;border:2px solid #ff1493;border-radius:15px;z-index:999999;box-shadow:0 0 20px rgba(255,20,147,0.5);color:white;font-family:sans-serif;padding:15px;cursor:grab;';
        div.innerHTML = '<h2 style="color:#ff1493;margin:0;font-size:16px;text-align:center;">ixl-flow</h2><hr style="border:0;border-top:1px solid #222;margin:10px 0;"><div id="flow-status" style="font-size:11px;color:#666;text-align:center;margin-bottom:10px;">Connected to Render</div><div id="flow-content" style="background:#111;padding:12px;border-radius:8px;min-height:50px;font-family:monospace;font-size:14px;color:#ff1493;text-align:center;">Scanning for question...</div>';
        document.body.appendChild(div);

        /* Drag functionality */
        div.onmousedown = function(e){{
            var offsetX = e.clientX - div.offsetLeft;
            var offsetY = e.clientY - div.offsetTop;
            document.onmousemove = function(e){{
                div.style.left = (e.clientX - offsetX) + 'px';
                div.style.top = (e.clientY - offsetY) + 'px';
            }};
            document.onmouseup = function(){{ document.onmousemove = null; }};
        }};

        /* Solver Loop */
        setInterval(function(){{
            var qElement = document.querySelector('.question-component') || document.querySelector('.practice-area');
            if(qElement) {{
                var questionText = qElement.innerText;
                fetch('{render_url}/solve', {{
                    method: 'POST',
                    headers: {{'Content-Type': 'application/json'}},
                    body: JSON.stringify({{question: questionText}})
                }})
                .then(r => r.json())
                .then(data => {{
                    document.getElementById('flow-content').innerText = data.answer;
                }});
            }}
        }}, 4000);
    }})();"""

    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h1>ixl-<span>flow</span></h1>
            <div class="step"><strong>1.</strong> Drag this to your Bookmarks:</div>
            <a class="btn-glow" href="{bookmarklet}" onclick="alert('Drag me to your bookmarks bar!'); return false;">IXL FLOW</a>
            <div class="step"><strong>2.</strong> Go to an IXL skill (like Algebra 1).</div>
            <div class="step"><strong>3.</strong> Click the bookmark to open the solver window.</div>
        </div>
    </body></html>
    """)

@app.route('/solve', methods=['POST'])
def solve():
    """Logic to process questions and return answers."""
    data = request.json
    question = data.get('question', '').lower()
    
    # Placeholder Logic: In a real script, this would use a Math API or AI to solve.
    # Since you are working on transformations:
    if "transformation" in question or "f(x)" in question:
        answer = "g(x) = f(x) - 1" # Typical answer for the screenshot you showed
    else:
        answer = "Analyzing..."

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
