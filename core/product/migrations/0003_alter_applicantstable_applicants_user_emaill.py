# Generated by Django 4.2.1 on 2023-05-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "product",
            "0002_rename_applicants_born_date_applicantstable_applicants_born_date_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicantstable",
            name="applicants_user_emaill",
            field=models.EmailField(max_length=100, null=True, verbose_name="Email"),
        ),
    ]
