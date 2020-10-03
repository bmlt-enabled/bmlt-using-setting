import requests
import json

roots_res = requests.get('https://tomato.bmltenabled.org/rest/v1/rootservers/?format=json')
roots = json.loads(roots_res.content)
for root in roots:
    root_server_info = json.loads(root['server_info'])[0]
    if root_server_info['emailEnabled'] == "1":
        print(format(root['name']))
