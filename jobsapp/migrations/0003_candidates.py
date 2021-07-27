# Generated by Django 3.1.3 on 2021-07-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0002_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=60, null=True)),
                ('phone_number', models.IntegerField(default=0, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Prefer not to say', 'prefer not to say')], max_length=50, null=True)),
                ('resume', models.FileField(null=True, upload_to='')),
                ('company', models.ManyToManyField(blank=True, to='jobsapp.Company')),
            ],
        ),
    ]
