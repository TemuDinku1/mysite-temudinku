# Generated by Django 4.1.1 on 2023-08-23 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image1', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('image2', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('image3', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('image4', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('image5', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='base.category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='base_catego_name_8e6637_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['id', 'slug'], name='base_produc_id_a62598_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='base_produc_name_220298_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-created'], name='base_produc_created_35f5b3_idx'),
        ),
    ]