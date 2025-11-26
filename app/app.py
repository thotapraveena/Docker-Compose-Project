from flask import Flask
import os

app = Flask(__name__)

NAME = os.getenv("NAME", "app")
COLOR = os.getenv("COLOR", "#ffcc00")  # default yellow
PORT = int(os.getenv("PORT", "5000"))

HTML = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>Colorful App - {name}</title>
    <style>
      body {{
        margin:0;
        height:100vh;
        display:flex;
        align-items:center;
        justify-content:center;
        background:{color};
        font-family: Arial, Helvetica, sans-serif;
      }}
      .card {{
        background: rgba(255,255,255,0.8);
        padding: 30px 40px;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        text-align:center;
      }}
      h1 {{ margin:0 0 8px 0; font-size:34px; color:#222; }}
      p  {{ margin:0; font-size:16px; color:#444; }}
    </style>
  </head>
  <body>
    <div class="card">
      <h1>Welcome — {name}</h1>
      <p>This is a colorful page served by the container <strong>{name}</strong>.</p>
    </div>
  </body>
</html>
"""

@app.route("/")
def index():
    return HTML.format(name=NAME, color=COLOR), 200, {"Content-Type": "text/html; charset=utf-8"}

@app.route("/health")
def health():
    return "ok\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
