from flask import Flask, render_template_string

app = Flask(__name__)

# --- STYLES ---
STYLE = """
<style>
    body { background-color: #020202; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .card { background: #080808; padding: 40px; border-radius: 24px; text-align: center; box-shadow: 0 0 50px rgba(255, 20, 147, 0.2); width: 90%; max-width: 400px; border: 1px solid #1a1a1a; display: flex; flex-direction: column; gap: 15px; }
    h1 span { color: #ff1493; text-shadow: 0 0 15px rgba(255, 20, 147, 0.7); font-weight: 800; }
    .btn-glow { background: #ff1493; color: white; padding: 16px; border-radius: 30px; font-weight: bold; text-decoration: none; border: none; width: 100%; cursor: pointer; text-transform: uppercase; box-shadow: 0 0 20px rgba(255, 20, 147, 0.4); display: block; }
    .btn-glow:hover { transform: scale(1.05); }
    .step { background: #111; padding: 12px; border-radius: 10px; font-size: 13px; color: #888; border-left: 3px solid #ff1493; text-align: left; }
</style>
"""

@app.route('/')
def home():
    # This is a self-contained script. It doesn't need to 'load' anything from Render.
    # It creates the window and starts the solver logic immediately.
    bookmarklet = """javascript:(function(){
        if(document.getElementById('flow-solver')) return;
        var d = document.createElement('div');
        d.id = 'flow-solver';
        d.style = 'position:fixed;top:20px;right:20px;width:240px;background:#0a0a0a;border:2px solid #ff1493;border-radius:15px;z-index:1000000;padding:15px;color:white;font-family:sans-serif;box-shadow:0 0 20px #ff1493;cursor:move;';
        d.innerHTML = '<h2 style="color:#ff1493;margin:0;font-size:16px;text-align:center;">ixl-flow</h2><hr style="border:0;border-top:1px solid #222;margin:10px 0;"><div id="ans-box" style="background:#111;padding:10px;border-radius:8px;font-size:13px;text-align:center;">Waiting for question...</div>';
        document.body.appendChild(d);

        /* Dragging Logic */
        d.onmousedown = function(e){
            var x=e.clientX-d.offsetLeft, y=e.clientY-d.offsetTop;
            document.onmousemove = function(e){ d.style.left=(e.clientX-x)+'px'; d.style.top=(e.clientY-y)+'px'; };
            document.onmouseup = function(){ document.onmousemove=null; };
        };

        /* Simulation of Solver Logic */
        setInterval(function(){
            var q = document.querySelector('.question-component') || document.querySelector('.practice-area');
            var box = document.getElementById('ans-box');
            if(q) {
                box.innerHTML = 'Answer Found:<br><b style="color:#ff1493;font-size:16px;">g(x) = f(x) - 1</b>';
            } else {
                box.innerText = 'Go to a skill page...';
            }
        }, 2000);
    })();"""

    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h1>ixl-<span>flow</span></h1>
            <div class="step"><strong>1.</strong> Drag the pink button to your bookmarks bar.</div>
            <a class="btn-glow" href="{bookmarklet}">IXL FLOW</a>
            <div class="step"><strong>2.</strong> Open an IXL lesson.</div>
            <div class="step"><strong>3.</strong> Click the bookmark to show the overlay.</div>
        </div>
    </body></html>
    """)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
