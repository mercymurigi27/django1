from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)


    def save_location(self):
        self.save()

    
    def delete_location(self):
        self.delete()


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


    def __str__(self):
        return self.name



class Image(models.Model):
    image = CloudinaryField("image_image")
    name = models.CharField(max_length=60)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def save_image(self):
        self.save()

    
    def delete_image(self):
        self.delete()

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images


    
    @classmethod
    def search_by_category(cls,query):
        images = cls.objects.filter(category__name__icontains = query)
        return images

    @classmethod
    def filter_by_location(cls,query):
        images = cls.objects.filter(location__name__icontains = query)
        return images

    @classmethod
    def get_image_by_id(cls,id):
        
        image = cls.objects.filter(id = id)
        print(image)
        return image
        

        
        


     

    def __str__(self):
        return self.name + self.description

# Create your models here.
