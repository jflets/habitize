# Generated by Django 3.2.21 on 2023-09-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_habit_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='frequency',
            field=models.CharField(choices=[('day', 'Daily'), ('week', 'Weekly'), ('month', 'Monthly')], default='day', max_length=10),
        ),
    ]