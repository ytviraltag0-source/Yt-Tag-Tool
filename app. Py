from flask import Flask, request, jsonify, render_template
from engines import youtube_engine, google_engine, bing_engine
from formatter import clean_tags
from cache import cache_get, cache_set

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def api():
    q = request.args.get("q")

    cached = cache_get(q)
    if cached:
        return jsonify(cached)

    yt = youtube_engine(q)
    gg = google_engine(q)
    bg = bing_engine(q)

    raw = yt + gg + bg
    final = clean_tags(raw)

    cache_set(q, final)
    return jsonify(final)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
