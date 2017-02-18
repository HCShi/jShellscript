from flask import Flask, render_template
app = Flask(__name__)
@app.route('/test', methods=['GET', 'POST'])
def test():
    return str({'a': 1})
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('get-data-from-api.html')
if __name__ == '__main__':
    app.run()
