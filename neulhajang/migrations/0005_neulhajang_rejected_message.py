# Generated by Django 4.2.4 on 2023-08-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neulhajang', '0004_alter_authenticationfeedlike_authentication_feed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='neulhajang',
            name='rejected_message',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]