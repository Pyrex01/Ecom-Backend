from django.db import models
from userManagement.models import Users


class Address_types(models.Model):
    Address_type = models.CharField(max_length=15)




class Address(models.Model):
    STATES = [
            ('AP',"Andhra Pradesh"),
            ('AR',"Arunachal Pradesh"),
            ('AS',"Assam"),
            ('BR',"Bihar"),
            ('CT',"Chhattisgarh"),
            ('GA',"Goa"),
            ('GJ',"Gujarat"),
            ('HR',"Haryana"),
            ('HP',"Himachal Pradesh"),
            ('JH',"Jharkhand"),
            ('KA',"Karnataka"),
            ('KL',"Kerala"),
            ('MP',"Madhya Pradesh"),
            ('MH',"Maharashtra"),
            ('MN',"Manipur"),
            ('ML',"Meghalaya"),
            ('MZ',"Mizoram"),
            ('NL',"Nagaland"),
            ('OR',"Orissa, Odisha"),
            ('PB',"Punjab, Punjab (India)"),
            ('RJ',"Rajasthan"),
            ('SK',"Sikkim"),
            ('TN',"Tamil Nadu, Tamizh Nadu"),
            ('TG',"Telangana"),
            ('TR',"Tripura"),
            ('UL',"Uttarakhand"),
            ('UP',"Uttar Pradesh"),
            ('WB',"West Bengal"),
            ('AN',"Andaman and Nicobar Islands"),
            ('CH',"Chandigarh"),
            ('DN',"Dadra and Nagar Haveli, Dadra & Nagar Haveli"),
            ('DD',"Daman and Diu"),
            ('DL',"Delhi, National Capital Territory of Delhi"),
            ('JK',"Jammu and Kashmir"),
            ('LA',"Ladakh"),
            ('LD',"Lakshadweep"),
            ('PY',"Pondicherry, Puducherry"),
    ]

    Name = models.CharField(max_length=30)
    Phone_number = models.CharField(max_length=13)
    Pincode = models.IntegerField()
    Regein = models.TextField()
    Landmark = models.TextField()
    Town = models.TextField()
    State = models.CharField(max_length=2,choices=STATES)
    Address_type_ID = models.ForeignKey(Address_types,on_delete=models.CASCADE)    
    User_ID = models.ForeignKey(Users,on_delete=models.CASCADE)