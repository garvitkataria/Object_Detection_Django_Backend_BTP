import requests

from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db import models
from django.db.models.signals import post_save
from io import BytesIO
from PIL import Image

import base64
# Create your models here.

class PotholeInfo(models.Model):
    """PotholeInfo model
    
    Fields:
        lat, long -- Latitude and Longitude
        img -- ImageField
        userFeedback -- TextField
    """

    lat  = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    img = models.ImageField(upload_to='pothole_info/images/img')
    img_with_potholes = models.ImageField(upload_to='pothole_info/images/img_with_potholes',
                            null=True, blank=True)
    added_on = models.DateTimeField(auto_now=True)
    danger_level = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    user_feedback = models.TextField(blank=True, null=True)

    def api_save(self, *args, **kwargs):
        # print(', '.join(['{}={!r}'.format(k, v) for k, v in kwargs.items()]))
        self.danger_level = kwargs['danger_level'][0]
        self.user_feedback = kwargs['user_feedback'][0]

        self.lat = kwargs['lat'][0]
        self.long = kwargs['long'][0]

        image_data = kwargs['img'][0]
        format, imgstr = image_data.split(';base64,')
        # print("format", format)
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr))  
        file_name = "'myphoto." + ext
        self.img.save(file_name, data, save=True)
        super(PotholeInfo, self).save()

    def __str__(self):
        return f'{str(self.id)}  => {str(self.danger_level)}'

    def get_image_with_pothole_path(self):
        path = str(self.img.path)
        path = path.replace('/img/', '/img_with_potholes/')
        return path
    
    def get_image_with_pothole_name(self):
        path = str(self.img.name)
        path = path.replace('/img/', '/img_with_potholes/')
        return path

    @classmethod
    def create_img_with_potholes(cls, instance, content):
        path = instance.get_image_with_pothole_path()
        f = open(path, 'wb')
        f.write(content)
        f.close()
        return open(path, 'rb')
 
    @classmethod
    def add_image_with_potholes(cls, sender, instance, **kwargs):
        try:
            """Adds img_with_potholes_for_image before saving the image"""
            print("check",instance.img.path)
            headers = {'enctype': 'multipart/form-data'}
            # print(instance.img.path, instance.img.name)
            r = requests.post(settings.TF_SERVER,
                    files={"pothole": open(instance.img.path, 'rb')})
            file = PotholeInfo.create_img_with_potholes(instance, r.content)
            f_name = instance.get_image_with_pothole_name()
            PotholeInfo.objects.filter(pk=instance.pk).update(img_with_potholes=File(file, name=f_name))
            file.close()
        except Exception as e:
            print(e)

post_save.connect(PotholeInfo.add_image_with_potholes, sender=PotholeInfo)

