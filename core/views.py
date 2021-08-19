import requests

from jsonrpcclient.clients.http_client import HTTPClient

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .exceptions import MethodNotAllowedException, JSONDecodeCustomError
@csrf_exempt
def login(request):
    if request.method == "POST":
        """ Getting variables from settings.py and writing in the files """
        with open('certificate.cert', 'w') as cert_file:
            cert_file.write(settings.JSON_RPC_CERTIFICATE)
        with open('key.key', 'w') as key_file:
            key_file.write(settings.JSON_RPC_CLIENT_KEY)

        """ Getting files paths """
        key_file_path = str(settings.BASE_DIR) + f'\{key_file.name}'
        cert_file_path = str(settings.BASE_DIR) + f'\{cert_file.name}'


        try:
            resp = requests.get('https://slb.medv.ru/api/v2/ ', cert=(r'%s' % cert_file_path, r'%s' % key_file_path),
                                verify=True)
            if resp.status_code not in [200, 201]:
                raise MethodNotAllowedException({"detail": "Method not allowed"})

        except Exception as e:
            print(e)

        """ Exception handling , this exception raised but i all steps did with documentation """
        try:
            client = HTTPClient("http://cats.com")
            client.request("ping")
        except Exception as e:
            raise JSONDecodeCustomError({'detail': 'Something went wrong'})

    return render(request, 'index.html', )
