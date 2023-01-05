from django.db import models

class Products(models.Model):
    product_id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    product_name = models.CharField(max_length=100)
    strap_color = models.CharField(max_length=20)
    highlight = models.TextField()
    price = models.IntegerField()
    active_inactive = models.BooleanField(default=True)
    image = models.ImageField(upload_to="images")


    def __str__(self):
        return str(self.product_name)




