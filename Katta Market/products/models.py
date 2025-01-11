from django.db import models

class Product(models.Model):
    product_image = models.ImageField(upload_to='media')
    product_name = models.CharField(max_length=150)
    price = models.IntegerField()
    discount = models.CharField(max_length=150, blank=True)
    discount_name = models.CharField(max_length=150, blank=True)
    buy_months = models.CharField(max_length=150, blank=True)
    # CATALOG = [
    #     ("Kiyimlar", "Kiyimlar"),
    #     ("Elektronika", "Elektronika"),
    #     ("Kiyimlar", "Kiyimlar"),
    # ]
    # catalog_name = models.CharField(max_length=150, choices=CATALOG)