from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello():
    return "Hor bhai Rishab Ustaad Ghuseyan de vich aa gaya hain..koi na...you will change this innnn cinco anos"

if __name__ == '__main__':
    app.run(debug=True)