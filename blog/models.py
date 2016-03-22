import datetime

from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title


# demonstration
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class EquipmentCategory (models.Model):
    title= models.CharField(max_length=200)
    description=models.CharField(max_length=500)

    # calculates the total price of all the EquipmentItems in a category

    def _get_total(self):
        total_price=0
        print(self.equipmentitem_set.filter())
        for item in self.equipmentitem_set.all():
            print(item.price)
            total_price+=item.price
        return total_price

    total = property(_get_total)

    def __str__(self):
        return self.title


class EquipmentItem (models.Model):
    title=models.ForeignKey(EquipmentCategory, on_delete=models.CASCADE)
    product_name=models.TextField()
    description=models.TextField()
    price=models.IntegerField()
    def __str__(self):
        return (self.product_name)