from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from plan.models import PlanModel
from plan.serializers import PlanSerializer


class HttpMethod():  # noqa: D101
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


@csrf_exempt
def plans(request):
    """List all plans, or create a new plan."""
    if request.method == HttpMethod.GET:
        plans = PlanModel.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == HttpMethod.POST:
        data = JSONParser().parse(request)
        import ipdb; ipdb.set_trace()
        serializer = PlanSerializer(data)
        # if serializer.is_valid():
        #     serializer.save()
        return JsonResponse(serializer.data, status=201)

    plans = PlanModel.objects.all()
    serializer = PlanSerializer(plans, many=True)
    return JsonResponse(serializer.data, safe=False)
