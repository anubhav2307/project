# Generated by Django 3.0.6 on 2021-04-10 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Info', '0008_admin_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Info.admin_files'),
        ),
    ]
