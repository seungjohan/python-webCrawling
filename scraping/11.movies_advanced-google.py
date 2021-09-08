import requests
from bs4 import BeautifulSoup



for idx, genre in enumerate(genres):

    url = "https://www.google.com/search?sxsrf=ALeKk00heD9-SU1lvtU9zXWUi61fs7UlwQ:1629529467131&q={}+movie+showtimes&stick=H4sIAAAAAAAAAOPgNeLSz9U3MMpOKTPN2cDI-IhRnlvg5Y97wlJik9acvMYowMXnm1-WmRqckV9ekpmbWsyziFUsMbkkMz9PIRckoVAMkwEA5-NNlkwAAAA&npsic=0&sxsrf=ALeKk00heD9-SU1lvtU9zXWUi61fs7UlwQ:1629529467131&ved=2ahUKEwj73aeoxsHyAhUoE6YKHU28DWUQ0CsoATAdegQIARAz".format(genre)

    res = requests.get(url)
    res.raise_for_status

    soup = BeautifulSoup(res.text, "lxml")

    genres = soup.find_all("div", attrs={"class":"znKVS"})

    images=soup.find_all("g-img", attrs={"class": "BA0A6c"})

    genre_list = genres.get_text()
    print(genre_list)
    link = ""

    for image in images:
        print(images["src"])

        image_url = image["src"]

        if image_url.startswith("//"):
            image_url = "https" + image_url










# switch문으로