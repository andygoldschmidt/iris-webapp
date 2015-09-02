import sys
import os
from werkzeug.utils import secure_filename

sys.path.append(os.path.dirname(__file__))

from flask import Flask, jsonify, request
from flask.ext.cors import cross_origin, CORS
from ml.classification import classify
from ml.color import analyze_colors


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'tiff'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# CORS(app, resources=r'/*', allow_headers=['Content-Type', 'Access-Control-Allow-Origin'])
CORS(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
    return jsonify({"message": "Ok."})


@app.route('/classify', methods=['POST'])
def classify_data():
    result = classify(request.json['data'],
                      request.json['features'],
                      request.json['targetColumn'])
    return jsonify({"results": result[0], 'accuracy': result[1]})


@app.route('/color', methods=['POST'])
def color():
    file = request.files['file']
    if not file and not allowed_file(file.filename):
        return jsonify({'message': "Error"})
    filename = secure_filename(file.filename)
    full_filename= os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(full_filename)
    colors = analyze_colors(full_filename)
    return jsonify({"colors": colors})


if __name__ == '__main__':
    if not os.path.isdir(app.config['UPLOAD_FOLDER']):
        os.mkdir(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
