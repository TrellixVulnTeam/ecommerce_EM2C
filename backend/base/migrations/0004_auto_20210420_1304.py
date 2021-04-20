# Generated by Django 3.1.7 on 2021-04-20 07:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20210330_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='image',
            field=models.ImageField(blank=True, default='/images/sample.PNG', null=True, upload_to=''),
        ),
    ]