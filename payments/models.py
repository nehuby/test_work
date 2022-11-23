from django.db import models

class Item(models.Model):
    name = models.CharField(verbose_name="name", max_length=100)
    description = models.TextField(verbose_name="description")
    price = models.PositiveIntegerField(verbose_name="price", default=0)

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"

    def __str__(self) -> str:
        return self.name

    def get_display_price(self) -> str:
        return "{0:.2f}".format(self.price / 100)