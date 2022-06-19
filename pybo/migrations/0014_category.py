# Generated by Django 3.1.3 on 2022-06-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0013_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardCode', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
