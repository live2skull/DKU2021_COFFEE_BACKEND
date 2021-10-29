# Generated by Django 3.2.8 on 2021-10-29 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('product_id', models.PositiveIntegerField()),
                ('original_product_extension', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='naver_shopping_products', to='market.productmallextension')),
            ],
        ),
    ]