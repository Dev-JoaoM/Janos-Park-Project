# Generated by Django 5.0.6 on 2024-06-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0024_alter_registrovisitante_autorizacao_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registrovisitante",
            name="ligacao",
            field=models.BooleanField(
                blank=True, null=True, verbose_name="Ligou para o Visitante?"
            ),
        ),
    ]
