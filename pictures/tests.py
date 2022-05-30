from django.test import TestCase
from unicodedata import category
from .models import Image,Location,Category

# Create your tests here.
class CategoryTestClass(TestCase):

    def setUp(self):
        self.new_category = Category(name = "Fashion")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))

    def test_save_method(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        self.new_category.save_category()
        test_category = Category(name = "Sports")
        test_category.save_category()
        self.new_category.delete_category()
        categories = Category.objects.all()

        self.assertTrue(len(categories),1)

class ImageTestClass(TestCase):

    def setUp(self):
        self.new_location = Location(name = "Nairobi")
        self.new_location.save_location()

        self.new_category = Category(name = "Fashion")
        self.new_category.save_category()


        self.new_image = Image(image = "image/upload/v1653735572/qjruwjselqauk9uqqz71.jpg",name = "new york fashion week",description = "A girl in new york fashion week",location= self.new_location,category = self.new_category)
        

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))


    def test_save_method(self):
        self.new_image.save_image()
        images =  Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_search_by_category(self):

        self.new_image.save_image()

        images = Image.search_by_category("Fashion")
        

        self.assertEquals(len(images),1)

    def test_filter_by_location(self):

        self.new_image.save_image()
        images = Image.filter_by_location("Nairobi")

        self.assertEqual(len(images),1)

    def test_get_image_by_id(self):
        self.new_image.save_image()
        image = Image.get_image_by_id(self.new_image.id)

        self.assertTrue(image)


class LocationTestClass(TestCase):

    def setUp(self):
        self.new_location = Location(name = "Nairobi")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_method(self):
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.new_location.save_location()
        test_location = Location(name = "New York")
        test_location.save_location()
        self.new_location.delete_location()
        locations = Location.objects.all()

        self.assertTrue(len(locations),1)    