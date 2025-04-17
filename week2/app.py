from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    if request.method == 'POST':
        name = request.form.get('user')
        color = request.form.get('color')
        number = request.form.get('number')

        fortunes = {
            ('red', '1'): "Stay Hard",
            ('yellow', '2'): "Opportunity",
            ('blue', '3'): "New Learning",
            ('green', '4'): "Nature"
        }

        fortune_result = fortunes.get((color, number), "The future depends on you!")
        return render_template('fortune_result.html', name=name, fortune=fortune_result)

    return render_template('fortune_form.html')

if __name__ == '__main__':
    app.run(debug=True)
