from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem')

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

class Page(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    
    # Change the default value to a valid category ID
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    
    is_new = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    link = models.URLField()
    image = models.ImageField(upload_to='banner_images/')

    def __str__(self):
        return self.title

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity



class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address_street = models.TextField()
    address_optional = models.TextField(blank=True, null=True)
    town_city = models.CharField(max_length=100)
    country_state = models.CharField(max_length=100)
    postcode_zip = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    create_account = models.BooleanField(default=False)
    account_password = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"Order #{self.id} - {self.first_name} {self.last_name}"
class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def total_price(self):
        return self.quantity * self.product.price
