# Generated by Django 4.0.6 on 2022-08-29 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0001_initial'),
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyapp.product')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.user')),
            ],
        ),
    ]
