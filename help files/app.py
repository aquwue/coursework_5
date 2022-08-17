from flask import Flask, render_template


app = Flask(__name__)
app.irl_map.strict_slashes = False

heroes = {
    "player": BaseUnit,
    "enemy": BaseUnit
}

EQUIPMENT = load_equipment()

arena =  ... # TODO инициализируем класс арены

game = Game()


def game_processing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if game.game_processing:
            return func(*args, **kwargs)
        if game.game_result:
            return render_template('fight.html', heroes=heroes, result=game.game_result())
        return redirect(url_for('index'))

    return wrapper


def render_choose_personage_template(*args, **kwargs) -> str:
    return render_template(
        'hero_choosing.html',
        classes=personage_classes.values(),
        equipment=EQUIPMENT,
        **kwargs,
    )


@app.route("/")
def menu_page():
    return render_template('index.html')


@app.route("/fight/")
def start_fight():
    if 'player' in heroes and 'enemy' in heroes:
        game.run(**heroes )
        return render_template('fight.html', heroes=heroes, result='Fight')
    return redirect(url_for('index'))


@app.route("/fight/hit")
def hit():
    return render_template('fight.html', heroes=heroes, result=game.player_hit())


@app.route("/fight/use-skill")
def use_skill():
    return render_template('fight.html', heroes=heroes, result=game.player_use_skill())


@app.route("/fight/pass-turn")
def pass_turn():
    return render_template('fight.html', heroes=heroes, result=game.next_turn())


@app.route("/fight/end-fight")
def end_fight():
    # TODO кнопка завершить игру - переход в главное меню
    return redirect(url_for('index'))
    # return render_template("index.html", heroes=heroes)


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    if request.method == 'GET':
        return render_choose_personage_template(header='Выберете героя', next_button='Выбрать врага')
    heroes['player'] = Player(
        unit_class=personage_classes[request.form['unit_class']],
        weapon=EQUIPMENT.get_weapon(request.form['weapon']),
        armor=EQUIPMENT.get_armor(request.form['armor']),
        name=request.form['name']
    )
    return redirect(url_for('choose_enemy'))


@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy():
    if request.method == 'GET':
        return render_choose_personage_template(header='Выберете врага', next_button='Начать сражение')
    heroes['enemy'] = Player(
        unit_class=personage_classes[request.form['unit_class']],
        weapon=EQUIPMENT.get_weapon(request.form['weapon']),
        armor=EQUIPMENT.get_armor(request.form['armor']),
        name=request.form['name']
    )
    return 'Not implemented'


if __name__ == "__main__":
    app.run()
