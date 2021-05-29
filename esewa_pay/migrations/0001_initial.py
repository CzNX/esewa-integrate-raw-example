# Generated by Django 3.2.3 on 2021-05-29 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_img', models.ImageField(upload_to='')),
                ('Payment_completed', models.BooleanField(default=False)),
            ],
        ),
    ]