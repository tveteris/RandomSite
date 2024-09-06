from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Load websites from file
def load_websites():
    with open('websites.txt', 'r') as file:
        return [line.strip() for line in file]

websites = load_websites()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-website')
def get_website():
    url = random.choice(websites)
    return jsonify({'url': url})

if __name__ == "__main__":
    app.run(debug=True, port=5002)