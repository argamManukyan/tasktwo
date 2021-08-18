import json

from django.views.decorators.csrf import csrf_exempt
from jsonrpcclient.clients import http_client

from django.shortcuts import render
from django.conf import settings

from .exceptions import MethodNotAllowedException


@csrf_exempt
def login(request):
    if request.method == "POST":
        client = http_client.HTTPClient('https://slb.medv.ru/api/v2/')
        client.session.auth = ('test@test.test', settings.JSON_RPC_CLIENT_KEY)

        update_req_data = []
        for k,v in request.POST.items():
            new_dict = {"jsonrpc": "2.0",}
            new_dict[k] = v
            update_req_data.append(json.dumps(new_dict))
        try:
            resp = client.send(update_req_data, headers={'Content-Type': 'application/json-rpc'})
        except Exception as e:
            raise MethodNotAllowedException({'detail': 'method is not allowed'})

    return render(request, 'index.html',)
