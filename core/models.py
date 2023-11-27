from django.db import models

# Create your models here.
State_choices =(
        ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
        ('Andhra Pradesh','Andhra Pradesh'),
        ('Arunachal Pradesh','Arunachal Pradesh'),
        ('Assam','Assam'),
        ('Bihar','Bihar'),
        ('Chandigarh','Chandigarh'),
        ('Chhattisgarh','Chhattisgarh'),
        ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
        ('Daman and Diu','Daman and Diu'),
        ('Delhi','Delhi'),
        ('Goa','Goa'),
        ('Gujarat','Gujarat'),
        ('Haryana','Haryana'),
        ('Himachal Pradesh','Himachal Pradesh'),
        ('Jammu & Kashmir','Jammu & Kashmir'),
        ('Jharkhand','Jharkhand'),
        ('Karnataka','Karnataka'),
        ('Kerala','Kerala'),
        ('Lakshadweep','Lakshadweep'),
        ('Madhya Pradesh','Madhya Pradesh'),
        ('Maharashtra','Maharashtra'),
        ('Manipur','Manipur'),
        ('Meghalaya','Meghalaya'),
        ('Mizoram','Mizoram'),
        ('Nagaland','Nagaland'),
        ('Odisha','Odisha'),
        ('Puducherry','Puducherry'),
        ('Punjab','Punjab'),
        ('Rajasthan','Rajasthan'),
        ('Sikkim','Sikkim'),
        ('Tamil Nadu','Tamil Nadu'),
        ('Telangana','Telangana'),
        ('Tripura','Tripura'),
        ('Uttarakhand','Uttarakhand'),
        ('Uttar Pradesh','Uttar Pradesh'),
        ('West Bengal','West Bengal'),
        
    )

GENDER_CHOICES =(
    ("male","MALE"),
    ('Female','FEMALE'),
    ('Others', 'OTHERS')
)

JOB_CITY_CHOICES = (
    ('delhi', 'DELHI'),
    ('mumbai', 'MUMBAI'),
    ('Banglore','BANGLORE')
)
class uploader(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False)
    gender = models.CharField(choices=GENDER_CHOICES ,max_length=30)
    phone = models.IntegerField()
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pin = models.IntegerField()
    state = models.CharField(choices=State_choices, max_length=50)
    email = models.EmailField()
    job_city = models.CharField(choices=JOB_CITY_CHOICES, max_length=50)
    profile = models.ImageField(upload_to='profileimage', blank=True)
    resume = models.FileField(upload_to='resume')

    def __str__(self) -> str:
        return self.name