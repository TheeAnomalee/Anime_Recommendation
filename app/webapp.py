from flask import Flask, render_template, request
from recommender import recommend_anime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    title = ""
    if request.method == 'POST':
        title = request.form['title']
        recommendations = recommend_anime(title)

    return render_template('index.html', title=title, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)