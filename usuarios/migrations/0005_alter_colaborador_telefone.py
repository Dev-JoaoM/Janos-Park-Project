# Generated by Django 5.0.6 on 2024-06-27 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0004_alter_colaborador_telefone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="colaborador",
            name="telefone",
            field=models.CharField(max_length=11, null=True, verbose_name="Telefone"),
        ),
    ]
