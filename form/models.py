from django.db import models

# Create your models here.
from django.db import models

class InfoModel(models.Model):
    """Manage the info input"""
    OPTION_0 = "OPTION0"
    OPTION_1 = "OPTION1"
    OPTION_2 = "OPTION2"
    OPTIONS = [
        
        (OPTION_0, 'Option 0'),
        (OPTION_1, 'Option 1'),
        (OPTION_2, 'Option 2'),
    ]

    TYPE0_OPTIONS = [
        ("MEDINA0", "Medina 0"),
        ("MEDINA1", "Medina 1"),
    ]
    TYPE1_OPTIONS = [
        ("CITY0", "City 0"),
        ("CITY1", "City 1"),
    ]
    TYPE2_OPTIONS = [
        ("REGION0", "Region 0"),
        ("REGION1", "Region 1"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    selection = models.CharField(max_length=50, choices=OPTIONS, null=True)
    type0 = models.CharField(max_length=50, choices=TYPE0_OPTIONS, null=True, blank=True)
    type1 = models.CharField(max_length=50, choices=TYPE1_OPTIONS, null=True, blank=True)
    type2 = models.CharField(max_length=50, choices=TYPE2_OPTIONS, null=True, blank=True)
