from flask import Flask, render_template, request, redirect, url_for
import os
import random



app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static')
ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return redirect(url_for('success'))
    return render_template('upload.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/gallery')
def gallery():
    image_files = [f for f in os.listdir(UPLOAD_FOLDER) if f.lower().endswith(('jpg', 'jpeg', 'png'))]
    random.shuffle(image_files)
    return render_template('gallery.html', images=image_files)

if __name__ == '__main__':
    app.run(debug=True)
