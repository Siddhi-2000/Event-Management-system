from django.db import models

# Create your models here.
# makemigrations- create changes and store in a file
# migrate- apply the pending changes created by makemigrations--apply changes in databases

# class Product(models.Model):
#     product_id = models.AutoField
#     product_name = models.CharField(max_length=50)
#     desc= models.CharField(max_length=300)
#     pub_date = models.DateField()


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    priority = models.IntegerField(default=1)
    description = models.TextField(default='')
    location = models.CharField(max_length=255, default='')
    organizer = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name



class Conference(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)
    rsvp_option = models.BooleanField(default=False)
    image = models.ImageField(upload_to='conference_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Workshop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)
    rsvp_option = models.BooleanField(default=False)
    image = models.ImageField(upload_to='workshop_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Concert(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)
    rsvp_option = models.BooleanField(default=False)
    image = models.ImageField(upload_to='concert_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Seminar(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)
    rsvp_option = models.BooleanField(default=False)
    image = models.ImageField(upload_to='seminar_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class CommunityMeetup(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)
    rsvp_option = models.BooleanField(default=False)
    image = models.ImageField(upload_to='communitymeetup_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=122, default="")
    email = models.EmailField(max_length=122, default="")
    phone = models.CharField(max_length=12, default="")  # Provide a default value here
    desc = models.TextField(default="")

    def __str__(self):
        return self.name
     


