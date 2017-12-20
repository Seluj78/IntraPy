from IntraPy.config import APP_UID, APP_SECRET

from IntraPy.IntraPy import init

from IntraPy.coalition_handler import *

app_token = init()

print(coalitions_get_scores(app_token))
