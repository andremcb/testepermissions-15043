# Generated by Django 2.2.13 on 2020-06-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_homepage_commit_2"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="commit_3",
            field=models.DurationField(blank=True, null=True),
        ),
    ]
