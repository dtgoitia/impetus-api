from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from presets.models import Preset
from presets.serializers import PresetSerializer


@csrf_exempt
def preset_list(request):
    """List all presets, or create a new preset."""
    if request.method == 'GET':
        presets = Preset.objects.all()
        serializer = PresetSerializer(presets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PresetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def preset_detail(request, pk):
    """Retrieve, update or delete a preset."""
    try:
        preset = Preset.objects.get(pk=pk)
    except Preset.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PresetSerializer(preset, many=False)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PresetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        preset.delete()
        return HttpResponse(status=204)
