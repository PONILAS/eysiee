# Generated by Django 4.0.3 on 2022-05-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aname', models.TextField(default='')),
                ('Aemail', models.TextField(default='')),
                ('Aphonenumber', models.TextField(default='')),
                ('Agender', models.TextField(default='')),
                ('Aage', models.TextField(default='')),
            ],
        ),
    ]
