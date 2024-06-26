# Generated by Django 5.0.6 on 2024-05-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_book', '0002_remove_book_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='publication_date',
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=13),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
