# Generated by Django 2.2.6 on 2019-10-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nid', models.IntegerField(max_length=50)),
                ('DateOfBirth', models.DateField()),
                ('FirstName', models.CharField(max_length=250)),
                ('LastName', models.CharField(max_length=250)),
                ('Phone1', models.IntegerField()),
                ('Status', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=250)),
                ('MaritalStatus', models.CharField(max_length=45)),
                ('Phone2', models.IntegerField()),
                ('Email', models.EmailField(max_length=250)),
                ('Village', models.CharField(max_length=50)),
            ],
        ),
    ]
