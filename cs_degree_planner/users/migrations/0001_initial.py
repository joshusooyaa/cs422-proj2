# Generated by Django 4.2.1 on 2023-06-07 03:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forecast', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_credits', models.IntegerField(default=0)),
                ('major_credits', models.IntegerField(default=0)),
                ('bs_credits', models.IntegerField(default=0)),
                ('aoi_credits', models.IntegerField(default=0)),
                ('cultural_credits', models.IntegerField(default=0)),
                ('aal_credits', models.IntegerField(default=0)),
                ('ssci_credits', models.IntegerField(default=0)),
                ('sci_credits', models.IntegerField(default=0)),
                ('gp_credits', models.IntegerField(default=0)),
                ('us_credits', models.IntegerField(default=0)),
                ('courses_taken', models.ManyToManyField(to='forecast.course')),
                ('interests', models.ManyToManyField(to='forecast.keyword')),
                ('major', models.ManyToManyField(to='forecast.major')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Forecast_Has_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('term', models.CharField(choices=[('F', 'Fall'), ('W', 'Winter'), ('S', 'Spring'), ('U', 'Summer')], max_length=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecast.course')),
                ('forecast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.forecast')),
            ],
        ),
        migrations.AddField(
            model_name='forecast',
            name='courses_in_fc',
            field=models.ManyToManyField(through='users.Forecast_Has_Course', to='forecast.course'),
        ),
        migrations.AddField(
            model_name='forecast',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
