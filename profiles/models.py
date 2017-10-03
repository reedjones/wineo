__author__ = 'reed'

from django.db import models

from django.conf import settings
import uuid


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.name, filename)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True) #name and email

    photo = models.ImageField(
        'Profile picture',
        upload_to=user_directory_path,
        null=True,
        blank=True,
        default=None
    )
    def get_img(self):
        return self.photo.url

    nick = models.SlugField(
        unique=True,
        allow_unicode=True,
        max_length=60,

    )

    description = models.TextField(
        blank=True,
        null=True,
        default = None
    )

    joined_on = models.DateField(auto_now=True)