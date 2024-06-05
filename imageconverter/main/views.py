from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ResizeSerializer
from django.shortcuts import render
from .scripts.resize import resize_image
import io
import base64


def index(request):
    return render(request, 'main/index.html')


def resize(request):
    original_image = None
    processed_image = None

    if request.method == 'POST' and request.FILES['image']:
        # Получаем загруженное изображение
        image = request.FILES['image'].read()
        left = request.POST.get('left')
        right = request.POST.get('right')
        top = request.POST.get('top')
        bottom = request.POST.get('bottom')
        wnsize = request.POST.get('wnsize')
        hnsize = request.POST.get('hnsize')

        # Создаем буфер для временного хранения обработанного изображения
        output_buffer = io.BytesIO()

        # Обрабатываем изображение и сохраняем его в буфере
        resize_image(io.BytesIO(image), output_buffer, left, top, right, bottom, wnsize, hnsize)

        input_buffer = io.BytesIO(image)
        input_buffer.seek(0)

        # Encode images to base64
        input_image_base64 = base64.b64encode(input_buffer.getvalue()).decode()
        output_image_base64 = base64.b64encode(output_buffer.getvalue()).decode()

        return render(request, 'main/resize.html', {
            'input_image_base64': input_image_base64,
            'output_image_base64': output_image_base64})

    return render(request, 'main/resize.html')


class ResizeApi(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ResizeSerializer(data=request.data)
        if serializer.is_valid():
            # Получаем загруженное изображение
            image = serializer.validated_data['image']
            left = serializer.validated_data.get('left', '')
            right = serializer.validated_data.get('right', '')
            top = serializer.validated_data.get('top', '')
            bottom = serializer.validated_data.get('bottom', '')
            wnsize = serializer.validated_data.get('wnsize', '')
            hnsize = serializer.validated_data.get('hnsize', '')

            image = image.read()

            # Создаем буфер для временного хранения обработанного изображения
            output_buffer = io.BytesIO()

            # Обрабатываем изображение и сохраняем его в буфере
            resize_image(io.BytesIO(image), output_buffer, left, top, right, bottom, wnsize, hnsize)

            input_buffer = io.BytesIO(image)
            input_buffer.seek(0)

            # Encode images to base64
            input_image_base64 = base64.b64encode(input_buffer.getvalue()).decode()
            output_image_base64 = base64.b64encode(output_buffer.getvalue()).decode()

            return Response({
                'output_image': output_image_base64
            })
        else:
            return Response(serializer.errors, status=400)
