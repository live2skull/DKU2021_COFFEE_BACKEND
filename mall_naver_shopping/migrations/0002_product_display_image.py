# Generated by Django 3.2.8 on 2021-10-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall_naver_shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='display_image',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
