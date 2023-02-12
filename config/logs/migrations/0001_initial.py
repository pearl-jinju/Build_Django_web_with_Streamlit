# Generated by Django 4.1.5 on 2023-02-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchLog',
            fields=[
                ('log_id', models.IntegerField(primary_key=True, serialize=False)),
                ('search_user', models.TextField()),
                ('search_keyword', models.TextField()),
                ('search_keyword_type', models.TextField()),
                ('search_route', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
