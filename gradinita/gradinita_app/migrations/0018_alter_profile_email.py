# Generated by Django 4.1.5 on 2023-03-27 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gradinita_app", "0017_alter_profile_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]