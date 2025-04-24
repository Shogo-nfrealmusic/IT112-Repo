from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class VideoGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    platform = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Game {self.title}>'

@app.before_first_request
def create_tables_and_seed_data():
    db.create_all()

    if not VideoGame.query.first():
        game1 = VideoGame(title="The Legend of Zelda", genre="Action-Adventure", platform="Nintendo Switch")
        game2 = VideoGame(title="God of War", genre="Action", platform="PlayStation")
        game3 = VideoGame(title="Stardew Valley", genre="Simulation", platform="PC")
        game4 = VideoGame(title="Minecraft", genre="Sandbox", platform="Multi")

        db.session.add_all([game1, game2, game3, game4])
        db.session.commit()

@app.route('/games')
def list_games():
    games = VideoGame.query.all()
    return render_template('games.html', games=games)

@app.route('/games/<int:game_id>')
def game_detail(game_id):
    game = VideoGame.query.get_or_404(game_id)  # 指定IDのゲームを取得。なければ404エラー
    return render_template('game_detail.html', game=game)
