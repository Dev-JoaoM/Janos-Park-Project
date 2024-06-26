# Generated by Django 5.0.6 on 2024-06-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0025_alter_registrovisitante_ligacao"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="registrovisitante",
            options={"ordering": ["data_limite", "data_saida"]},
        ),
        migrations.RemoveField(
            model_name="qntvagasvisita",
            name="registro_visitante",
        ),
        migrations.AddField(
            model_name="registrovisitante",
            name="esta_de_carro",
            field=models.BooleanField(
                blank=True, default=True, null=True, verbose_name="Está de carro?"
            ),
        ),
    ]
