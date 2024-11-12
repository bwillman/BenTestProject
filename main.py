from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        hometown = request.form['hometown']
        favorite_band = request.form['favorite_band']
        with open('data.json', 'r') as f:
            data = json.load(f)
        data.append({'name': name, 'hometown': hometown, 'favorite_band': favorite_band})
        with open('data.json', 'w') as f:
            json.dump(data, f)
        return render_template('index.html', message='Data submitted successfully!')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)