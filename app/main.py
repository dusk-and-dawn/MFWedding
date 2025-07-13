from flask import Flask, render_template, url_for 
import os
import random as rs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/gallery')
def gallery():
    random_nr = rs.randint(0, 4)
    img_to_show = f'img{random_nr}.jpeg'
    
    return render_template('gallery.html', img_to_show=img_to_show)

if __name__ == '__main__':
    app.run(debug=True)