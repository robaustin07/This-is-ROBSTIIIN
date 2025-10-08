from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/touppercase')
def touppercase():
    return render_template('touppercase.html')

@app.route('/areacircle')
def areacircle():
    return render_template('areacircle.html')

@app.route('/areatriangle')
def areatriangle():
    return render_template('areatriangle.html')

if __name__ == "__main__":
    app.run(debug=True)
