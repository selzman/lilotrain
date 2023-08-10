from django.db import models
from user_module.models import User
# Create your models here.
from ckeditor.fields import RichTextField

class Product(models.Model):
    name=models.CharField(max_length=300)
    slug=models.CharField(max_length=300,unique=True)
    image=models.ImageField(upload_to='static/image-product')
    description=RichTextField()
    price = models.IntegerField()
    discount_price = models.IntegerField(null=True,blank=True)
    activate = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name






class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='نظر')
    parent = models.ForeignKey('Comment', null=True, blank=True, on_delete=models.CASCADE, verbose_name='والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن نظر')
    is_active =models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'نظر '
        verbose_name_plural = 'نظرات '
