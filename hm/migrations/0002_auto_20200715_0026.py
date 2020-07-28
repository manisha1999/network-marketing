# Generated by Django 3.0.3 on 2020-07-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobn', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('spid', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='whatsapp',
            field=models.CharField(max_length=10),
        ),
    ]
