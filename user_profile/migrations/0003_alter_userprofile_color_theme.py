# Generated by Django 3.2.21 on 2023-09-27 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_userprofile_profile_image_public_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='color_theme',
            field=models.CharField(choices=[('default', 'Default Theme'), ('blue', 'Blue Theme'), ('turquoise', 'Turquoise Theme'), ('green', 'Green Theme'), ('pink', 'Pink Theme'), ('purple', 'Purple Theme'), ('brown', 'Brown Theme')], default='light', max_length=20),
        ),
    ]
