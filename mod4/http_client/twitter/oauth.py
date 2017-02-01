# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from requests_oauthlib import OAuth1Session

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
BASE_AUTHORIZATION_URL = "https://api.twitter.com/oauth/authorize"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"


def setup_oauth(consumer_key, consumer_secret):
    """Authorize your app via identifier."""
    # Request token using OAuth1Session
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
    r = oauth.fetch_request_token(REQUEST_TOKEN_URL)
    print(r)

    resource_owner_key = r.get('oauth_token')
    resource_owner_secret = r.get('oauth_token_secret')

    # Request token using OAuth1 auth helper
    # oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    # r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    # print(r.content)
    # credentials = parse_qs(r.content)
    # resource_owner_key = r.get('oauth_token')[0]
    # resource_owner_secret = r.get('oauth_token_secret')[0]

    # obtain authorization from the user to access their protected resources
    # Using OAuth1Session
    authorization_url = oauth.authorization_url(BASE_AUTHORIZATION_URL)
    print('Please go here and authorize,', authorization_url)
    redirect_response = input('Paste the full redirect URL here: ')
    oauth_response = oauth.parse_authorization_response(redirect_response)
    print(oauth_response)
    # {
    #     "oauth_token": "Z6eEdO8MOmk394WozF5oKyuAv855l4Mlqo7hhlSLik",
    #     "oauth_verifier": "sdflk3450FASDLJasd2349dfs"
    # }
    verifier = oauth_response.get('oauth_verifier')

    # Using OAuth1 auth helper
    # authorize_url = BASE_AUTHORIZATION_URL + '?oauth_token='
    # authorize_url = authorize_url + resource_owner_key
    # print('Please go here and authorize,', authorize_url)
    # verifier = input('Please input the verifier')

    # Obtain an access token from the OAuth provider
    # Save this token to be reused later.
    # using OAuth1Session
    oauth = OAuth1Session(consumer_key,
                          client_secret=consumer_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret,
                          verifier=verifier)
    oauth_tokens = oauth.fetch_access_token(ACCESS_TOKEN_URL)
    # {
    #     "oauth_token": "6253282-eWudHldSbIaelX7swmsiHImEL4KinwaGloHANdrY",
    #     "oauth_token_secret": "2EEfA6BG3ly3sR3RjE0IBSnlQu4ZrUzPiYKmrkVU"
    # }
    resource_owner_key = oauth_tokens.get('oauth_token')
    resource_owner_secret = oauth_tokens.get('oauth_token_secret')

    # using OAuth1
    # oauth = OAuth1(CONSUMER_KEY,
    #                 client_secret=CONSUMER_SECRET,
    #                 resource_owner_key=resource_owner_key,
    #                 resource_owner_secret=resource_owner_secret,
    #                 verifier=verifier)
    # r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    # r.content
    # "oauth_token=6253282-eWudHldSbIaelX7swmsiHImEL4KinwaGloHANdrY&oauth_token_secret=2EEfA6BG3ly3sR3RjE0IBSnlQu4ZrUzPiYKmrkVU"
    # credentials = parse_qs(r.content)
    # resource_owner_key = credentials.get('oauth_token')[0]
    # resource_owner_secret = credentials.get('oauth_token_secret')[0]
    return resource_owner_key, resource_owner_secret


def get_oauth(consumer_key, consumer_secret, access_token, access_token_secret):
    # use the OAuth1Session
    oauth = OAuth1Session(consumer_key,
                          client_secret=consumer_secret,
                          resource_owner_key=access_token,
                          resource_owner_secret=access_token_secret)

    # use OAuth1 helper
    # oauth = OAuth1(CONSUMER_KEY,
    #                client_secret=CONSUMER_SECRET,
    #                resource_owner_key=ACCESS_TOKEN,
    #                resource_owner_secret=ACCESS_TOKEN_SECRET)
    return oauth
