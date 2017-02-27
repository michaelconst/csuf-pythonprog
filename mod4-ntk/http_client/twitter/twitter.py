from oauth import setup_oauth, get_oauth
from pprint import pprint
import requests
from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


class TwitterAccount:
    SETTINGS_URL = "https://api.twitter.com/1.1/account/settings.json"
    HOME_STATUS_URL = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
    QUERY_URL = 'https://api.twitter.com/1.1/search/tweets.json'

    def __init__(self, consumer_key, consumer_secret, access_token=None, access_token_secret=None):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.oauth = None

        if self.access_token is None:
            self.access_token, self.access_token_secret = setup_oauth(self.consumer_key, consumer_secret)
        self.oauth = get_oauth(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)

        if self.oauth is None:
            raise ValueError("authentication failed")

    def _get(self, *args, **kwargs):
        return self.oauth.get(*args, **kwargs)

    def get_account_settings(self):
        return self._get(self.SETTINGS_URL)

    def get_recent_tweets(self, *fields):
        results = self._get(self.HOME_STATUS_URL)
        if results.status_code == requests.codes.ok:
            items = results.json()
            if fields:
                return self._filter(items, *fields)
            else:
                return items

    def _filter(self, items, *fields):
        twits = []
        for item in items:
            tw = dict()
            for field in fields:
                v = item.get(field)
                if v is not None:
                    tw[field] = v
            twits.append(tw)
        return [str(tw) for tw in twits]

    def query_tweets(self, query, location, *fields, count=None):
        import urllib.parse as urlparse
        from urllib.parse import urlencode

        params = {"q": query, "geocode": location}
        if count:
            params.update({"count": count})

        url_parts = list(urlparse.urlparse(self.QUERY_URL))
        url_parts[4] = urlencode(params)
        url = urlparse.urlunparse(url_parts)
        results = self._get(url)
        if results.status_code == requests.codes.ok:
            items = results.json()
            if fields:
                return '\n'.join(self._filter(items['statuses'], *fields))
            else:
                return '\n'.join(items)


if __name__ == "__main__":
    try:
        acct = TwitterAccount(CONSUMER_KEY, CONSUMER_SECRET,
                              access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
        r = acct.get_account_settings()
        pprint('My account settings:\n{}'.format(r.json()))
        print('========================\n\n')

        tweets = acct.get_recent_tweets('text')
        pprint('My tweets:\n{}'.format(tweets))
        print('========================\n\n')

        tweets_query = "Python"
        # near CSUF, 10mi radius
        tweets_location = "33.8782741,-117.8851012,10mi"
        results = acct.query_tweets(tweets_query, tweets_location, 'text', count=10)
        pprint("My query " + tweets_query + " results:\n{}".format(results))
        print('========================\n\n')
    except ValueError as e:
        print(e)
