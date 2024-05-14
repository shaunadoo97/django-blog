# Generated by Django 4.2.13 on 2024-05-14 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_on']},
        ),
        migrations.AddField(
            model_name='post',
            name='field_2',
            field=models.IntegerField(default=42),
        ),
        migrations.AddField(
            model_name='post',
            name='field_3',
            field=models.CharField(null=True),
        ),
    ]
