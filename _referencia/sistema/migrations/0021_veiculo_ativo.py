# Generated by Django 2.2.3 on 2019-07-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0020_auto_20190726_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
