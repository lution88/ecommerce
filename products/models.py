from django.db import models

from core.models import TimeStampModel


class Product(TimeStampModel):
    """ 제품 모델 """
    name = models.CharField("제품이름", max_length=50)
    content = models.TextField("제품설명")
    price = models.IntegerField("가격")
    quantity = models.IntegerField("수량")
    region = models.CharField("원산지", max_length=50)
    delivery_method = models.CharField("배송방법", max_length=30)
    delivery_charge = models.IntegerField("배송비")

    def __str__(self):
        return f'{self.name} / {self.price} / {self.content}'


class ProductImage(models.Model):
    """ 제품 이미지 """
    product = models.ForeignKey(
        Product,
        verbose_name="제품",
        on_delete=models.CASCADE,
        related_name="product_image"
    )
    product_image = models.ImageField(upload_to="products/images/%Y/%m/%d/", blank=True)


class ProductOption(models.Model):
    """ 제품 옵션 """
    product = models.ForeignKey(
        Product,
        verbose_name="제품",
        on_delete=models.CASCADE,
        related_name="product_opt"
    )
    opt_name = models.CharField("옵션 이름", max_length=50)
    opt_price = models.IntegerField("옵션 가격")

    def __str__(self):
        return f'{self.opt_name} / {self.opt_price}'
