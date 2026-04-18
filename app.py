from flask import Flask, request, render_template_string

app = Flask(__name__)

# --- STYLES (Cleaned up to prevent overlap) ---
STYLE = """
<style>
    body { background-color: #020202; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .card { background: #080808; padding: 40px; border-radius: 24px; text-align: center; box-shadow: 0 0 50px rgba(255, 20, 147, 0.2); width: 100%; max-width: 380px; border: 1px solid #1a1a1a; display: flex; flex-direction: column; gap: 15px; box-sizing: border-box; }
    h1 span, h2 { color: #ff1493; text-shadow: 0 0 15px rgba(255, 20, 147, 0.7); font-weight: 800; margin: 0; }
    .step { background: #111; padding: 15px; border-radius: 12px; text-align: left; border-left: 4px solid #ff1493; font-size: 14px; }
    input { width: 100%; padding: 14px; border-radius: 10px; border: 1px solid #222; background: #000; color: white; box-sizing: border-box; outline: none; }
    input:focus { border-color: #ff1493; }
    .btn-glow { background: #ff1493; color: white; padding: 16px; border-radius: 30px; font-weight: bold; text-decoration: none; border: none; width: 100%; cursor: pointer; text-transform: uppercase; box-shadow: 0 0 20px rgba(255, 20, 147, 0.4); box-sizing: border-box; }
    .btn-glow:hover { transform: scale(1.02); background: #ff4da6; }
    ul { list-style: none; padding: 0; text-align: left; margin: 0; }
    li { margin: 12px 0; color: #222; font-size: 14px; display: flex; align-items: center; }
    li.done { color: #ff1493; }
    li.active { color: #ff1493; font-weight: bold; animation: pulse 1.5s infinite; }
    .dot { height: 6px; width: 6px; border-radius: 50%; display: inline-block; margin-right: 12px; background: #1a1a1a; }
    li.done .dot { background: #ff1493; box-shadow: 0 0 10px #ff1493; }
    li.active .dot { background: #ff1493; box-shadow: 0 0 15px #ff1493; }
    @keyframes pulse { 0% { opacity: 0
