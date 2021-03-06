from django.db import models
from django import forms
from django_social_app.models import MyUser
from django.core.validators import RegexValidator
from geoposition.fields import GeopositionField
from multiselectfield import MultiSelectField
from django.db import models
from image_cropping import ImageCropField, ImageRatioField



class UserProfile(models.Model):
	

	MY_CHOICES = (('item_key1', 'Travel'),
              ('item_key2', 'Fitness'),
              ('item_key3', 'Music'),
              ('item_key4', 'Hobbies'),
              ('item_key5', 'Spiritual'))

        user = models.OneToOneField(MyUser)
        profile_image = models.ImageField(upload_to="profile_photos")
        age = models.IntegerField(null=True)
        designation = models.TextField()
        channels = MultiSelectField(choices=MY_CHOICES,default='item_key1')
	credits = models.IntegerField(default=20)
        regular = models.BooleanField(default=True)
	working_at = models.TextField(default="",blank=True)
	college = models.TextField(default="",blank=True)
	about = models.TextField(default="",blank=True)
	score = models.IntegerField(default=0)

        def __unicode__(self):
                return self.user.username



class User_Details_Earlier(models.Model):

	MY_CHOICES = (('item_key1', 'Travel'),
              ('item_key2', 'Fitness'),
              ('item_key3', 'Music'),
              ('item_key4', 'Hobbies'),
              ('item_key5', 'Momentum'))


	info = models.TextField(unique=True)
	latitude =  models.FloatField(blank=True)
	longitude = models.FloatField(blank=True)
	interest = MultiSelectField(choices=MY_CHOICES,default='item_key1')


class User_Details(models.Model):

	MY_CHOICES = (('item_key1', 'Travel'),
              ('item_key2', 'Fitness'),
              ('item_key3', 'Music'),
              ('item_key4', 'Hobbies'),
              ('item_key5', 'Momentum'))


	user = models.ForeignKey(MyUser)
	info = models.TextField(blank=True)
	interest = MultiSelectField(choices=MY_CHOICES,default='item_key1')
	latitude = models.FloatField(blank=True)
	longitude = models.FloatField(blank=True)



class Hangout(models.Model):
	#owner = models.ForeignKey(MyUser)
	cover_pic = models.ImageField(upload_to="cover_pic")
	name = models.CharField(max_length=255)
	weblink = models.CharField(max_length=255)
	email = models.EmailField(max_length=70,blank=True, unique= True)
	about = models.TextField()
	address = models.TextField()
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone = models.TextField(validators=[phone_regex])
	position = GeopositionField()
	

	def __unicode__(self):
		return self.name

class Event(models.Model):

	MY_CHOICES = (('item_key1', 'Travel'),
              ('item_key2', 'Fitness'),
              ('item_key3', 'Music'),
              ('item_key4', 'Hobbies'),
              ('item_key5', 'Momentum'))

	hangout = models.ForeignKey(Hangout)
	cover_pic = models.ImageField(upload_to="cover_pic")
	name = models.TextField()
	organizer = models.OneToOneField(MyUser)
	datetime = models.DateTimeField(blank=True)
	about = models.TextField()
	interest = MultiSelectField(choices=MY_CHOICES,default='item_key1')
	tags = models.TextField(blank=True)
	def __unicode__(self):
		return self.name



"""class Hangout_ImageGallery(models.Model):
	hangout = models.ForeignKey(Hangout)
	gallery = models.ImageField(upload_to="image_gallery")
	uploaded_by=models.ForeignKey(MyUser)

	def __unicode__(self):
		return self.hangout.name	"""
	


class Event_ImageGallery(models.Model):
        event = models.ForeignKey(Event)
        gallery = models.ImageField(upload_to="image_gallery")
        uploaded_by=models.ForeignKey(MyUser)

        def __unicode__(self):
                return self.event.name

"""class Hangout_Promotion(models.Model):
	hangout = models.ForeignKey(Hangout)
	text = models.TextField()
	def __unicode__(self):
		return self.hangout.name"""


"""class Event_Promotion(models.Model):
        event = models.ForeignKey(Event)
        text = models.TextField()
        def __unicode__(self):
                return self.event.name


class Hangout_Staff(models.Model):
	hangout = models.ForeignKey(Hangout)
	name = models.CharField(max_length=255)
	#user = models.ForeignKey(UserProfile)
	designation=models.TextField()
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        phone = models.TextField(validators=[phone_regex])
	
	days = models.CharField(max_length=12)
	starttime = models.TimeField()
	endtime = models.TimeField()

	def __unicode__(self):
		return self.hangout.name	"""



class Event_Staff(models.Model):
        event = models.ForeignKey(Event)
	#user = models.ForeignKey(UserProfile)
        name = models.CharField(max_length=255)
        designation=models.TextField()
        phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        phone = models.TextField(validators=[phone_regex])

        days = models.CharField(max_length=12)
        starttime = models.TimeField()
        endtime = models.TimeField()

        def __unicode__(self):
                return self.event.name


"""class HangoutPermission(models.Model):
	hangout = models.ForeignKey(Hangout)
	access = models.ForeignKey(MyUser)
	def __unicode__(self):
		return self.hangout.name"""



class EventPermission(models.Model):
	event = models.ForeignKey(Event)
	access = models.ForeignKey(MyUser)
	def __unicode__(self):
		return self.event.name




class ProfileLimitation(models.Model):
	hangout = models.OneToOneField(Hangout)
	no_of_profiles = models.IntegerField(default=20)
	starttime = models.TimeField()


"""class Hangout_Liked(models.Model):
	user = models.ForeignKey(UserProfile)
	hangout = models.ForeignKey(Hangout)
	time = models.TimeField(auto_now_add=True)
	regular = models.BooleanField(default=False)"""

class User_Connection(models.Model):
	sender = models.ForeignKey(UserProfile)
	receiver = models.ForeignKey(UserProfile,related_name="receiver")
	interest_status = models.BooleanField(default=0)


	def __unicode__(self):
		return self.sender.user.username + "--" + self.receiver.user.username





class Event_Liked(models.Model):
	user = models.ForeignKey(UserProfile)
	event = models.ForeignKey(Event)
	time = models.TimeField(auto_now_add=True)
	going = models.BooleanField(default=False)	
	like = models.BooleanField(default=False)
	rating = models.IntegerField(default=1)

class UserStatus(models.Model):
	user = models.ForeignKey(UserProfile)
	status = models.TextField()
	public = models.BooleanField(default=0)





class Upload_Image(models.Model):
    user = models.OneToOneField(MyUser)
    image = ImageCropField(blank=True, upload_to='profile_photos')
    cropping = ImageRatioField('image', '430x360')	



class SimilarEvent(models.Model):
	event = models.ForeignKey(Event)
	selected = models.TextField(blank=True)

	def __unicode__(self):
		return self.event.name


class Event_Comment(models.Model):
	event = models.ForeignKey(Event)
	comment = models.TextField()
	commented_by = models.ForeignKey(UserProfile)
