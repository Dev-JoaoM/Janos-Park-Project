# Generated by Django 2.2.3 on 2019-07-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0007_auto_20190724_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='horario',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
