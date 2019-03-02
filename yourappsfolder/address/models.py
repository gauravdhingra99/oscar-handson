from django.db import models

# from oscar.apps.address.abstract_models import AbstractProduct
from oscar.apps.address.abstract_models import AbstractUserAddress


class UserAddress(AbstractUserAddress):
    pannumber=models.CharField(max_length=10,null=True)
    gstnumber=models.CharField(max_length=15,null=True)
    shopname=models.CharField(max_length=15,null=True)




from oscar.apps.address.models import *