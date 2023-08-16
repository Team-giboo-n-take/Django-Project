# Generated by Django 4.2.4 on 2023-08-16 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=30)),
                ('notice_title', models.TextField()),
                ('notice_content', models.TextField()),
                ('notice_image', models.ImageField(null=True, upload_to='notice/')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
            options={
                'db_table': 'tbl_notice',
            },
        ),
    ]