# Generated by Django 2.2.12 on 2022-07-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_ticketinterest_users_subscribed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketinterest',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]