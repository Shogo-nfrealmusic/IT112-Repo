from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# モデル定義
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# DB初期化を関数にして明示的に呼ぶ
def create_tables():
    with app.app_context():  # Flaskのアプリコンテキストを明示的に使う
        db.create_all()

@app.route('/')
def hello():
    return 'Hello, Flask API!'

@app.route('/add-test-item')
def add_test_item():
    new_item = Item(name="Test Item")
    db.session.add(new_item)
    db.session.commit()
    return "Item added!"

@app.route('/api/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    data = [{"id": item.id, "name": item.name} for item in items]
    return jsonify(data), 200

@app.route('/api/items', methods=['POST'])
def add_item():
    try:
        data = request.get_json()
        print("Received JSON:", data)
        new_item = Item(name=data['name'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"message": "Item added successfully"}), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500


create_tables()

if __name__ == '__main__':
    app.run(debug=True)

