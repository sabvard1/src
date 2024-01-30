from django.db import models
from accounts.models import profileModel

# Create your models here.

class locationModel(models.Model):
    Name = models.CharField(max_length=100)
    CountryName = models.CharField(max_length=100, null = True)
    CityName = models.CharField(max_length = 100)
    FlagImage = models.ImageField(upload_to="flagImages/")
    MapImage = models.ImageField(upload_to="mapImages/", null=True)
    Description = models.CharField(max_length = 100)

    def __str__(self):
        return "{}-{}".format(self.CountryName, self.CityName)

class serverModel(models.Model):
    locationModel= models.ForeignKey("locationModel", on_delete = models.PROTECT)
    Name = models.CharField(max_length = 100)
    Fixed = 1
    Not_Fixed = 2
    fixed_status = ((Fixed, "Fixed"), (Not_Fixed, "Not Fixed"))
    FixedIpAddress = models.IntegerField(choices=fixed_status, null=True)
    Description = models.CharField(max_length = 100)

    Full = 1
    Ready = 2
    Stoped = 3
    Updating = 4
    Coming_soon = 5
    Status_choices = ((Full, "Full"),(Coming_soon, "Coming soon"), (Ready, "Ready"), (Stoped, "Stoped"), (Updating, "Updating"))
    Status = models.IntegerField(choices=Status_choices, null = True)
    UrlAddress = models.CharField(max_length=100, null = True)


    def __str__(self):
        return "Server {} in {}".format(self.Name, self.locationModel.Name)

class configModel(models.Model):
    serverModel = models.ForeignKey("serverModel", on_delete= models.PROTECT)
    profileModel = models.ForeignKey(profileModel, on_delete= models.PROTECT)
    Name = models.CharField(max_length = 100)
    Type = models.CharField(max_length = 100)
    Time = models.CharField(max_length = 100)
    QRcode = models.ImageField(upload_to="qrcodeImages/")
    ConfigLink = models.CharField(max_length = 300)

    def __str__(self):
        return "config {} on server {} time period {}".format(self.Name, self.serverModel.Name, self.Time)
    
