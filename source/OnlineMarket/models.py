from django.db import models


PRODUCT_OTHER_CHOICE = 'other'
PRODUCT_CATEGORY_CHOICES = (
    (PRODUCT_OTHER_CHOICE, 'Other'),
    ('food', 'Food'),
    ('drink', 'Drink'),
    ('cloth', 'Cloth'),
    ('electronics', 'Electronics')
)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(max_length=2000, verbose_name='Description', null=True, blank=True)
    category = models.CharField(max_length=20, verbose_name='Category',
                                choices=PRODUCT_CATEGORY_CHOICES, default=PRODUCT_OTHER_CHOICE)
    amount = models.IntegerField(verbose_name='Amount')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'