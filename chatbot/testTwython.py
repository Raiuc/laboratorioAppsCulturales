from twython import Twython

APP_KEY             = 'jByrnJjBK1qwXbAs5IIXlGc7Q'
APP_SECRET          = 'ASQsvQnu0KGpPFakTDKbezy8dzYy9YEHGtGxy2ocgww2HGe322'
OAUTH_TOKEN         = '747471719342841856-ID2YX5V3iM4suIxyIWMZSmfVnnlwjcZ'
OAUTH_TOKEN_SECRET  = 'hyL409iSVq8LWLUNDqwQdIBiySm1fHYOucYXsIhub62cs'


twitter              = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.verify_credentials()
twitter.get_home_timeline()

# t = twitter.search(q='herramienta')
results = twitter.cursor(twitter.search, q='herramienta', count=10)
for result in results:
    print(result['text'])
# print(t)
# ACCESS_TOKEN = twitter.obtain_access_token()
