import random
import time
from io import BytesIO

from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from .forms import ImageForm
from PIL import Image as PILImage


def check_image(image):
    img = PILImage.open(BytesIO(image.read()))
    width, height = img.size
    time.sleep(3)
    return f"Размер: {width}x{height}"


def image_list(request):
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)
            # нейро
            image_instance.nn_answer = check_image(request.FILES['image'])
            image_instance.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})


def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        image.delete()
        return redirect('image_list')
    return render(request, 'delete_image.html', {'image': image})


def yes_logic(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.status = "1"
    image.save()
    return redirect('image_list')


def no_logic(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.status = "0"
    image.save()
    return redirect('image_list')