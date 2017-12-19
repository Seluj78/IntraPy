from decouple import config

# 42 API Variables
APP_UID = config('APP_UID', cast = str, default = None)
APP_SECRET = config('APP_SECRET', cast = str, default = None)