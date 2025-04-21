from flask import Flask, render_template
import os

app = Flask(__name__)

# Social links - replace these with your actual links
SOCIAL_LINKS = {
    'github': 'https://github.com/yourusername',
    'twitter': 'https://twitter.com/yourusername',
    'linkedin': 'https://linkedin.com/in/yourusername',
    'email': 'mailto:your.email@example.com'
}

@app.route('/')
def home():
    return render_template('index.html', social_links=SOCIAL_LINKS)

if __name__ == '__main__':
    app.run(debug=True) 