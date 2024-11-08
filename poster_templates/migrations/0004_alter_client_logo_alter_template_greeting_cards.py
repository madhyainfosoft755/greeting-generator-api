# Generated by Django 5.0.4 on 2024-11-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster_templates', '0003_remove_template_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='logo',
            field=models.ImageField(upload_to='static/client_logos/'),
        ),
        migrations.AlterField(
            model_name='template',
            name='greeting_cards',
            field=models.ImageField(upload_to='static/greeting_cards/'),
        ),
    ]
