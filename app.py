from flask import Flask, request, render_template
from sentiment_analysis import get_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        sentiment = get_sentiment(text)
        return render_template('index.html', sentiment=sentiment)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)