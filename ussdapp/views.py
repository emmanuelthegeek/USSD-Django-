from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def index(request):
    if request.method == ['POST', 'GET']:
        session_id = request.values.get('sessionId', None)
        service_code = request.values.get('serviceCode', None)
        phone_number = request.values.get('phoneNumber', None)
        text = request.values.get('text', "Default")

        response = ""

        if text == " ":
            response = "CON Hi, how may we be of help \n" #According to the API (Africaistalking), string responses must start with CON
            response += "1. Open account"
        elif text == "1":
            response = "END Your account number is {0}".format(phone_number)
        return HttpResponse(response)