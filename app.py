from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
  return "Bonjour! cette application est déployée sur Render (PAAS)."
  if __name__ == "__main__":
    app.run()
