from django.db import models
#above line is for importing the models module from django.db, which allows us to define our database models.

class Product(models.Model): #This line defines a new model class called Product that inherits from models.Model, which is the base class for all Django models.
    name = models.CharField(max_length=255) #This line defines a name field for the Product model, which is a CharField with a maximum length of 255 characters.
    price = models.FloatField() #This line defines a price field for the Product model, which is a FloatField that can store decimal numbers.
    stock = models.IntegerField() #This line defines a stock field for the Product model, which is an IntegerField that can store whole numbers.
    image_url = models.CharField(max_length=2083) #This line defines an image_url field for the Product model, which is a CharField with a maximum length of 2083 characters (the maximum length of a URL).
    
    
class Offer(models.Model): #This line defines a new model class called Offer that inherits from models.Model.
    discount_code = models.CharField(max_length=50) #This line defines a code field for the Offer model, which is a CharField with a maximum length of 50 characters.
    discount_description = models.CharField(max_length=255) #This line defines a description field for the Offer model, which is a CharField with a maximum length of 255 characters.
    discount_percentage = models.FloatField() #This line defines a discount_percentage field for the Offer model, which is a FloatField that can store decimal numbers representing the percentage discount.