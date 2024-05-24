import secrets
from datetime import timedelta
from flask import Flask, render_template, jsonify, request, session

app = Flask(__name__, static_url_path='/static')
app.secret_key = secrets.token_urlsafe(32)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1)


@app.route('/')
def index():
    score = session.get("score", 0)
    return render_template('index.html', score=score)

@app.route('/increment', methods=['POST'])
def increment():
    increment_amount = int(request.args.get('increment_amount', 1))
    session['score'] = session.get("score", 0) + increment_amount
    if session['score'] > 500000000000:
        return jsonify({'score': session['score'], 'flag': "jellyCTF{redacted}"})
    return jsonify({'score': session['score'], 'flag': ""})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
