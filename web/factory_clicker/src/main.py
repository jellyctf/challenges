from flask import Flask, render_template, jsonify, request

app = Flask(__name__, static_url_path='/static')

score = 0
flag = ""

@app.route('/')
def index():
    global score 
    global flag 
    flag = ""
    score = 0
    return render_template('index.html', score=0)

@app.route('/increment', methods=['POST'])
def increment():
    global score
    global flag
    increment_amount = int(request.args.get('increment_amount', 1))
    score += increment_amount
    if score > 50000: flag = "jellyCTF{keep_on_piping_jelly}"
    return jsonify({'score': score, 'flag': flag})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
