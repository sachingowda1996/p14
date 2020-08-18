import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","P12.settings")

import django
django.setup()

from django.core.files.storage import FileSystemStorage

def store_image(image):
    fs=FileSystemStorage()
    file=fs.save(image.name,image)
    file_url=fs.url(file)
    return file_url