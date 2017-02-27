import requests
import csv
import os
import sys

from utils.movie import Movie, get_configuration, CONFIG, TMDb_URL
from utils.config import API_KEY


LANG = "en-US"

DATA = 'DATA'
CSVFILE = 'MOVIES.CSV'


class Movies:
    @staticmethod
    def search_movies(query, adult=False):
        url = TMDb_URL + "search/movie"
        movies = list()
        qs = {
            "api_key": API_KEY,
            "language": LANG,
            "query": query,
            "include_adult": adult
        }

        num_results = 0
        num_pages = 0
        current_page = 1

        while True:
            qs["page"] = current_page
            result = requests.get(url, params=qs)
            json_results = result.json()
            if num_results == 0:
                num_results = json_results["total_results"]
                num_pages = json_results["total_pages"]
            current_page = json_results["page"]
            for m in json_results["results"]:
                movies.append(Movie(m["id"], m["original_title"], m["overview"], m["release_date"], m["vote_average"],
                                    m["poster_path"]))
            current_page += 1
            if current_page > num_pages:
                break

        return movies


if __name__ == '__main__':
    if len(sys.argv) < 2:
        script_name = os.path.basename(__file__)
        print('usage: {} <query> [<outfile>]'.format(script_name))
        sys.exit(1)

    query = sys.argv[1]
    outpath = None
    if len(sys.argv) == 3:
        outpath = sys.argv[2]
        if not os.isabs(outpath):
            outpath = os.path.join(os.getcwd(), outpath)
    else:
        data_dir = os.path.join(os.path.dirname(__file__), DATA)
        if not os.path.exists(data_dir):
            try:
                os.makedirs(data_dir)
            except OSError as e:
                print(e)
        outpath = os.path.join(data_dir, CSVFILE)

    if outpath is None:
        print("invalid output path")
        sys.exit(1)

    CONFIG["outdir"] = os.path.dirname(outpath)

    movies = Movies.search_movies(query)
    write_header = not os.path.exists(outpath
                                      )
    with open(outpath, 'a') as csvfile:
        dictwriter = csv.DictWriter(csvfile, fieldnames=Movie.FIELDNAMES)
        if write_header:
            dictwriter.writeheader()
        for movie in movies:
            dictwriter.writerow(movie.todict())
            movie.save_poster()
