# Generated by Django 4.0.4 on 2022-07-18 18:43

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persian_title', models.CharField(max_length=200)),
                ('english_title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='store_app')),
                ('weight', models.CharField(default='225', max_length=4)),
                ('price', models.PositiveIntegerField(default=12000000)),
                ('review', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('count', models.PositiveSmallIntegerField(default=2)),
                ('screen_size', models.CharField(blank=True, default='15.6 اینچ', max_length=10, null=True)),
                ('usb_port_no', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='3', max_length=2, null=True)),
                ('ram', models.CharField(blank=True, choices=[('4', '4'), ('8', '8'), ('16', '16'), ('32', '32')], default='16', max_length=3, null=True)),
                ('proccessor_serie', models.CharField(blank=True, default='Core i7', max_length=20, null=True)),
                ('proccessor_builder', models.CharField(blank=True, default='intel', max_length=10, null=True)),
                ('graphic_proccessor_builder', models.CharField(blank=True, default='NVIDIA', max_length=10, null=True)),
                ('internal_storage', models.CharField(blank=True, choices=[('128', '128 گیگ'), ('256', '256 گیگ'), ('512', '512 گیگ'), ('1024', '1 ترابایت'), ('2048', '2 ترابایت')], default='256', max_length=4, null=True)),
                ('networks', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('2G', '2G'), ('3G', '3G'), ('4G', '4G'), ('5G', '5G')], default=['2G', '3G', '4G'], max_length=11, null=True)),
                ('pic_resolution', models.CharField(default='64', max_length=3)),
                ('simcard_no', models.CharField(blank=True, choices=[('1', 'تک سیمکارت'), ('2', 'دو سیمکارت'), ('4', 'چهار سیمکارت')], default='2', max_length=20, null=True)),
                ('special_features', models.TextField(blank=True, null=True)),
                ('chipset', models.CharField(blank=True, default='Apple A11 Bionic Chipset', max_length=30, null=True)),
                ('chipset_type', models.CharField(blank=True, default='64', max_length=3, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobiles', to='store_app.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobiles', to='store_app.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Publish')], default='d', max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
