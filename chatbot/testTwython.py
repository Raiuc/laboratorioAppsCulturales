from twython import Twython

APP_KEY             = 'ujKdZODxeNl5P18fFnkfzNjdD'
APP_SECRET          = 'u0pEpffrsPOowKfqMPc8TJloHeteZclk1dgiQl917LQkVRIoPO'
OAUTH_TOKEN         = '747471719342841856-nDifHde0e7EHbjjYsCx58esk3D50R3k'
OAUTH_TOKEN_SECRET  = 'NZRfyDddUVilOO3dU9Kb4l5jVh3MhbWXNMqTa2WXv5DVX'


twitter              = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.verify_credentials()
twitter.get_home_timeline()

t = twitter.search(q='herramienta')

print(t)
# ACCESS_TOKEN = twitter.obtain_access_token()
