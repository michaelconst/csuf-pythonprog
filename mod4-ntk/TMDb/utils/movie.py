import requests
import os

from utils.config import API_KEY

TMDb_URL = "https://api.themoviedb.org/3/"

MINQS = {
    "api_key": API_KEY
}


def get_configuration():
    def get_size(s):
        try:
            return (s, int(s[1:]))
        except ValueError:
            pass

    config = {}
    r = requests.get(TMDb_URL + "configuration", params=MINQS)
    rjson = r.json()
    config["image_base_url"] = rjson["images"]["base_url"]
    logo_sizes = list(map(get_size, rjson["images"]["logo_sizes"]))
    logo_sizes = [ls for ls in logo_sizes if ls]
    intervals = list(zip(range(160, 1150, 50), range(200, 1201, 50)))
    for lo, hi in intervals:
        logo_size = [ls[0] for ls in logo_sizes if lo <= ls[1] < hi]
        if len(logo_size) > 0:
            config["logo_size"] = logo_size[0]
            return config


CONFIG = get_configuration()


class Movie:
    FIELDNAMES = ["id", "title", "overview", "release_date", "score", "poster_path"]

    FILE_TYPE_MAPPING = {
        'image/jpeg': '.jpg',
        'image/png': '.png',
        'image.gif': '.gif'
    }

    def __init__(self, id_, title, overview, release_date, score, poster_path):
        self.id = id_
        self.title = title
        self.overview = overview
        self.release_date = release_date
        self.score = score
        self.poster_path = poster_path

    @classmethod
    def set_outpath(cls, outpath):
        cls.outtpath = outpath

    def get_poster_url(self, logo_size=CONFIG["logo_size"]):
        if self.poster_path:
            return (CONFIG["image_base_url"] + '{}{}').format(logo_size, self.poster_path)
        else:
            return None

    def download_poster(self, logo_size=CONFIG["logo_size"]):
        url = self.get_poster_url(logo_size=logo_size)
        if url:
            try:
                r = requests.get(url, stream=True)
                fileext = '.jpg'
                r.raise_for_status()
                try:
                    fileext = self.FILE_TYPE_MAPPING[r.headers['Content-Type']]
                except KeyError:
                    pass
                filepath = os.path.join(CONFIG['outdir'], str(self.id) + fileext)
                with open(filepath, 'wb') as f:
                    for chunk in r:
                        f.write(chunk)
            except requests.HTTPError as e:
                print('error downloading poster for movie id={} ({})'.format(self.id, str(e)))
        else:
            print('poster url missing for movie id={}'.format(self.id))

    def todict(self):
        d = dict()
        for field in self.FIELDNAMES:
            if hasattr(self, field):
                d[field] = getattr(self, field)
        return d