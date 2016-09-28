from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from beta.choices import *
from sorl.thumbnail import ImageField
from django.core.validators import RegexValidator
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill


class Startup(models.Model):
    user =              models.ForeignKey(User, null=True, blank=True)
    startup_id =        models.CharField(max_length=30, unique=True)
    startup =           models.CharField(max_length=30)
    tagline =           models.CharField(max_length=60)
    home_page =         models.ImageField(upload_to="home_page")
    home_page_thumbnail=ImageSpecField(source='home_page',
                            processors=[ResizeToFill(300, 200)],
                            format='JPEG', options={'quality': 60})
    details_thumbnail=ImageSpecField(source='home_page',
                            processors=[ResizeToFill(600, 300)],
                            format='JPEG', options={'quality': 60})
    related_thumbnail=ImageSpecField(source='home_page',
                            processors=[ResizeToFill(250, 150)],
                            format='JPEG',options={'quality': 60})
    logo =              models.ImageField(upload_to="home_page", null=True, blank=True)
    logo_thumbnail=ImageSpecField(source='logo',
                            processors=[ResizeToFill(100, 50)],
                            format='JPEG', options={'quality': 60})
    category =          models.CharField(max_length=30, choices=CAT)
    description =       models.TextField()
    region =            models.CharField(max_length=60, choices=REGIONS)
    country =           models.CharField(max_length=60, choices=AFRICAN_COUNTRIES)
    city =              models.CharField(max_length=60)
    url =               models.URLField(max_length=120)
    tag =               models.CharField(max_length=60, choices=RELATED_TAGS)
    promoted =          models.BooleanField(blank=True, default=False)
    stat =              models.CharField(max_length=30, choices=STATUS)
    #status =            models.CharField(max_length=30, choices=BETA_STATUS)
    pub_status =        models.CharField(max_length=30, choices=PUB_STATUS, null=True, blank=True)
    pub_date =          models.DateField(null=True, blank=True)
    added_date =        models.DateTimeField(auto_now_add=True)
    mod_date =          models.DateTimeField(auto_now=True)
            
    def __unicode__(self):
        return "%s %s %s %s %s %s %s %s %s %s" %(self.startup_id, self.startup,
                self.tagline, self.category, self.region, self.country,
                self.city, self.tag, self.stat, self.pub_status)
    
    
class Team(models.Model):
    startup =           models.ForeignKey(Startup, blank=True, null=True)
    full_name =         models.CharField(max_length=60)
    photo =             models.ImageField(upload_to="team_photos")
    twitter_handle =    models.CharField(max_length=120, blank=True, null=True)
    role =              models.CharField(max_length=30, choices=TEAM_ROLE)
    
    def __unicode__(self):
        return "%s %s" %(self.full_name, self.role)
    
# class Comment(models.Model):
#     user =              models.ForeignKey(User)
#     startup =           models.ForeignKey(Startup)
#     comment =           models.TextField()
    
class NewLetter(models.Model):
    email =             models.EmailField(max_length=120, unique=True)
    added_date =        models.DateTimeField(auto_now_add=True)
    
    
class Tester(models.Model):
    user =              models.ForeignKey(User)
    region =            models.CharField(max_length=60, choices=REGIONS)
    country =           models.CharField(max_length=60, choices=AFRICAN_COUNTRIES)
    city =              models.CharField(max_length=60)
    age =               models.CharField(max_length=3)
    sex =               models.CharField(max_length=30, choices=GENDER)
    social_account =    models.URLField()
    your_industry =     models.CharField(max_length=250, choices=INDUSTRY)
    confirmation =      models.BooleanField(blank=True, default=False)
    added_date =        models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "%s %s %s %s %s %s" %(self.region, self.country, self.city, self.age,
                      self.sex, self.your_industry)
    


                       
    
    
class BetaTest(models.Model):
    user =              models.ForeignKey(User)
    test_id =           models.CharField(max_length=60, unique=True)
    name =              models.CharField(max_length=60)
    tagline =           models.CharField(max_length=60)
    description =       models.TextField()
    logo =              models.ImageField(upload_to="logo_image", blank=True, null=True)
    link =              models.URLField(max_length=120, blank=True, null=True)
    app_file =          models.FileField(upload_to='app_files', blank=True, null=True)
    region =            models.CharField(max_length=60, choices=REGIONS)
    country =           models.CharField(max_length=60, choices=AFRICAN_COUNTRIES)
    city =              models.CharField(max_length=60)
    age_from =          models.CharField(max_length=3)
    age_to =            models.CharField(max_length=3)
    sex =               models.CharField(max_length=30, choices=TARGETED_GENDER)
    start_date =        models.DateField()
    end_date =          models.DateField()
    status =            models.CharField(max_length=30, choices=PUB_STATUS)
    added_date =        models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "%s %s %s %s %s %s %s" %(self.test_id, self.name, self.tagline, self.region,
                        self.country, self.city, self.sex,)
    
class TestFeedBack(models.Model):
    user =              models.ForeignKey(User)
    testing =           models.ForeignKey(BetaTest)
    review =            models.TextField()
    added_date =        models.DateTimeField(auto_now_add=True)
    
class SignUp(models.Model):
    user =              models.ForeignKey(User, null=True)
    startup =           models.ForeignKey(Startup)
    signup_date =       models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'startup']
        
# class Contact(models.Model):
#     name = models.CharField(max_length=120)
#     subject = models.CharField(max_length=120)
#     email = models.EmailField(max_length=120)
#     message = models.TextField()
    
class Info(models.Model):
    """All the information goes in here"""
    FAQ = models.TextField(blank=True, null=True)
    about_us = models.TextField(blank=True, null=True)
    join_our_network = models.TextField(blank=True, null=True)
    advertise_with_us = models.TextField(blank=True, null=True)
    our_rules = models.TextField(blank=True, null=True)
    terms_and_conditions = models.TextField(blank=True, null=True)
    address_line_1 = models.CharField(max_length=120, blank=True)
    address_line_2 = models.CharField(max_length=120, blank=True)
    phone_number = models.CharField(max_length=120, blank=True)
    email = models.EmailField(max_length=120, blank=True)
    pub_date_info = models.DateTimeField(auto_now_add=True)
    mod_date_info = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s %s %s" % (self.address_line_1, self.address_line_2,
                             self.phone_number)

class Default(models.Model):
    """All the defaults tables are stored in this database"""
    logo =  models.ImageField()
    


    

    




    