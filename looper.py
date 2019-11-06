import requests

from config import Config


def looper():

    config = Config()

    r = requests.get(config.function_url, params={"name": "Chris"})

    print(r.status_code)
    print(r.text)


if __name__ == "__main__":

    looper()
