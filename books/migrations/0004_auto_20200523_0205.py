# Generated by Django 2.2.7 on 2020-05-23 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
    ]
