# Generated by Django 4.2.3 on 2023-08-02 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='course_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sms_app.courses'),
        ),
        migrations.AlterField(
            model_name='students',
            name='profile_pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
