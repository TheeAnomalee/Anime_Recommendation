from flask import Flask, render_template, request
from app.recommender import recommend_anime
import pandas as pd

app = Flask(__name__)
anime_df = pd.read_csv("app/data/animes.csv")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        title = request.form.get("title", "").strip()

        if not title:
            return render_template("index.html", error="Please enter a title."), 200

        if title not in anime_df['title'].values:
            return render_template("index.html", error="Anime not found.", title=title), 200

        recommendations = recommend_anime(title)
        return render_template("index.html", title=title, recommendations=recommendations), 200

    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)