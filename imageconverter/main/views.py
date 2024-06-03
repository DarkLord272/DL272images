from django.http import HttpResponse, JsonResponse
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

