from django.db import models

class Contact(models.Model):
    CATEGORY_CHOICES = [
        ('customer', 'مشتری‌'),
        ('thread_seller', 'نخ فروش‌'),
        ('parts_seller', 'قطعه فروش'),
        ('oil_seller', 'روغن فروش‌'),
        ('dyeing', 'رنگرزی'),
        ('spinning', 'ریسندگی'),
        ('knitting','بافندگی'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='customer')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"