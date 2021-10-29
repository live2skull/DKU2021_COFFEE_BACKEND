
from django.db import models


# 카테고리 정보 (1 depths:
class Category(models.Model):
    code = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=20)
    parent = models.ForeignKey(
        'market.Category', related_name='sub_categories', null=True, on_delete=models.CASCADE
    )

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        unique_together = [
            ['code', 'name']
        ]

