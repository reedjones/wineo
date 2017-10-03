from django.conf import settings
from django.db import models

# Create your models here.
#from WineO.settings import AUTH_USER_MODEL

def wine_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'wine_{0}/{1}'.format(instance.id, filename)



class Winery(models.Model):

    name = models.CharField(max_length=60)
    user_description = models.TextField(blank=True, default=None, null=True)
    description = models.TextField(blank=True, default=None, null=True)
    logo = models.ImageField(blank=True, default=None, null=True)
    tag_line = models.CharField(blank=True, default=None, null=True, max_length=100)
    country = models.CharField(max_length=3) #cz, usa, etc...



class Wine(models.Model):
    name = models.CharField(max_length=60)
    user_description = models.TextField(blank=True, default=None, null=True)
    winery_description = models.TextField(blank=True, default="No Winery Description")
    volume = models.DecimalField(decimal_places=2, max_digits=4)
    barcode = models.BigIntegerField(blank=True, default=None, null=True)
    year = models.CharField(max_length=10)
    image = models.ImageField(blank=True, default=None, null=True)
    wine_type = models.CharField(max_length=200)
    made_by = models.ForeignKey(Winery, related_name='wines', blank=True, default=None, null=True)
    user_made_by = models.CharField(max_length=200, blank=True, default=None, null=True)
    create_on = models.DateTimeField(auto_now=True)

    estimated_price = models.DecimalField(decimal_places=2, max_digits=12)

    region = models.CharField(max_length=200)
    country = models.CharField(max_length=10)
    label = models.ImageField(blank=True, default=None, null=True, upload_to=wine_directory_path)

    def get_url(self):
        return "/wine/{0}/".format(self.pk)

class Note(models.Model):
    rates = (
        (0, "Absolutely Horrible"),
        (1, "Bad"),
        (2, "Drinkable"),
        (3, "Ok | Normal"),
        (4, "Pretty Good"),
        (5, "Good"),
        (6, "Very Good"),
        (7, "Excellent"),
        (8, "Superb"),
        (9, "Exceptional | Special"),
        (10, "Unique | Rare | Exceptional | Special"),

    )
    by = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField()
    rating = models.CharField(choices=rates, default=rates[3][1], max_length=100)
    posted_on = models.DateTimeField(auto_now=True)
    drank_on = models.DateField()
    was_special = models.BooleanField(default=False)
    occasion = models.TextField(null=True, default="no occasion", blank=True)
    about = models.ForeignKey(Wine, related_name='notes')


    def __str__(self):
        return Note.rates[int(self.rating[0])][1]


    def get_occasion(self):
        return self.occasion or "no occasion"
