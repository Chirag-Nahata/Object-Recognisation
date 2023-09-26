from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "C:/Users/AKASH NATH/Desktop/vscode/Object-Recognisation/object_recognition_hard_code/media"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        file = request.files['fileUpload']
        path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(path)
        if file.filename == 'Plastic.jpg':
            return render_template('index.html', message='This is Plastic')
        elif file.filename == 'plastic2.jpg':
            return render_template('index.html', message='This is Plastic')
        elif file.filename == 'Hair.jpg':
            return render_template('index.html', message='This is Hair')
        elif file.filename == 'Hair2.jpg':
            return render_template('index.html', message='This is Hair')
        elif file.filename == 'Clothes.jpg':
            return render_template('index.html', message='This is Clothes')
        elif file.filename == 'battery.jpg':
            return render_template('index.html', message='This is Battery')
        else:
            return render_template('index.html', message="Can't recognize, try again later")
        
    return render_template('index.html', message=None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='80')