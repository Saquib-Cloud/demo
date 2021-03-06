# Generated by Django 3.1.7 on 2021-03-10 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sunshine', '0004_auto_20210310_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=100)),
                ('message', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Home1',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='sunshine/images')),
            ],
        ),
        migrations.CreateModel(
            name='Home2',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=200)),
                ('desc', models.TextField()),
                ('image', models.ImageField(default='', upload_to='sunshine/images')),
            ],
        ),
    ]
