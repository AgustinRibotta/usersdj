# Generated by Django 4.2.4 on 2023-08-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cod_register',
            field=models.CharField(default='000000', max_length=6, verbose_name='Registration code'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
