from flask  import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('game.html')

@app.route('/play', methods = ['POST', 'GET'])
def play():
    if request.method == 'POST':
        player_1 = request.form['player_1']
        player_2 = request.form['player_2']

        return render_template('play.html', p1 = player_1, p2 = player_2)


if __name__ == '__main__':
    app.run(debug=True)
