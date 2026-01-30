herimport requests, json

def youtube_engine(q):
    url = "https://suggestqueries.google.com/complete/search"
    params = {"client":"firefox","ds":"yt","q":q}
    r = requests.get(url, params=params, timeout=5)
    return json.loads(r.text)[1]

def google_engine(q):
    url = "https://suggestqueries.google.com/complete/search"
    params = {"client":"firefox","q":q}
    r = requests.get(url, params=params, timeout=5)
    return json.loads(r.text)[1]

def bing_engine(q):
    try:
        url = "https://api.bing.com/osjson.aspx"
        r = requests.get(url+"?query="+q, timeout=5)
        return json.loads(r.text)[1]
    except:
        return []
