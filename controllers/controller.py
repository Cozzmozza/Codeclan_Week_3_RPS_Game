from app import app
from flask import render_template, redirect, request
# from models.game import game_logic
from models.game import Game
from models.player import Player

@app.route('/rps/')
def index():
    return render_template('welcome.html', title='Welcome!')

@app.route('/rps/play')
def play():
    return render_template('play.html', title='Play CPU')

@app.route('/rps/<p1_choice>/<p2_choice>')
def choices(p1_choice, p2_choice):
    p1 = Player('Player 1', p1_choice)
    p2 = Player('Player 2', p2_choice)
    outcome = Game().game_logic(p1, p2)
    players = [p1,p2]
    return render_template('index.html', title='Result', players=players, outcome=outcome)

@app.route('/rps/play', methods=['post'])
def play_cpu():
    human_choice = request.form['choice']
    human = Player(request.form['name'], human_choice) 

    computer_choice = Game().play_computer()
    computer = Player('Computer', computer_choice) 

    outcome = Game().game_logic(human, computer)

    players2 = [human, computer]

    return render_template('index.html', title='Result', players2=players2, outcome=outcome)
    # This seems a bit of a repetition from the decoration/choices function above
    # Can the play_cpu function utilize choices function?

    # And It's also not always working. Occasionally gives a wrong result. Why?
        # Computer choice is fine. But the outcome code is reading it wrong, or logic is wrong
        # The original possibilites all work fine entering into the URL, so that function does work..
        # Is it because I have two players lists?
        # *** THIS HAS FIXED IT, BUT IT SEEMS LAZY ***
