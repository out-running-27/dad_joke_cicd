import requests


def get_dad_joke(joke_id=None):

    url = "https://icanhazdadjoke.com/"
    if joke_id:
        url += "j/" + joke_id
    headers = {
        "Accept": "text/plain",
        "User-Agent": "https://github.com/out-running-27/dad_joke_cicd",
    }

    r = requests.get(url, headers=headers)

    return r.text
