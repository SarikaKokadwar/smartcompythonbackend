# Generated by Django 5.1.1 on 2024-10-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartcompythondemo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
