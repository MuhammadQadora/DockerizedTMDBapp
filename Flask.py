from flask import Flask, request, render_template
from TMDBclass import downloadAndDisplay
import json
app = Flask(__name__)


@app.route('/',methods=['GET'])
def main():
    return 'Just a welcome page'

@app.route('/search', methods=['POST','GET'])
def index():
    data = request.data('name')
    json.loads(data)
    result = downloadAndDisplay(data)

    return render_template('index.html')


app.run(debug=True, port=5000, host='0.0.0.0')