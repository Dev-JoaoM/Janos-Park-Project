# Generated by Django 5.0.6 on 2024-06-28 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0027_alter_registrovisitante_esta_de_carro"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apartamento",
            name="telefone_apto",
            field=models.CharField(max_length=11, verbose_name="Telefone"),
        ),
    ]
