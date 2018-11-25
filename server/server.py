from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/plot_scatter', methods=['GET'])
def plot_scatter():
    return render_template('plot_scatter.html')

@app.route('/plot_3d', methods=['GET'])
def plot_3d():
    return render_template('plot_3d.html')

if __name__ == "__main__":
    app.run()
