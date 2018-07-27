from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from core.models import Payment
from core.serializers import PaymentSerializer

# Create your views here.

def payment_request(request):
    if request.method == 'GET':
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            # TODO: Route to SaaS instance
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)