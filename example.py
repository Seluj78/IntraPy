from IntraPy import IntraPy
from IntraPy import coalition_handler

app_token = IntraPy.init()

print(coalition_handler.coalitions_get_scores(app_token))
