# Generated by Django 2.1.2 on 2018-10-03 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=32)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name = "Test",
            fields = [
                ()
            ],
        )
    ]
