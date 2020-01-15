# Generated by Django 2.2.5 on 2020-01-06 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infracao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infracao',
            name='arma_de_fogo',
            field=models.CharField(blank=True, choices=[('Revolver', 'Revolver'), ('Pistola', 'Pistola'), ('Fac', 'Faca')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='infracao',
            name='status',
            field=models.CharField(blank=True, choices=[('Vivo', 'Vivo'), ('Morto', 'Morto'), ('Preso', 'Preso'), ('Solto', 'Solto')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='modusoperandi',
            name='faccao',
            field=models.CharField(blank=True, choices=[('ADE', 'ADE'), ('Nenhumas', 'Nenhuma'), ('PCC', 'PCC-Primeiro Comando da Capital'), ('Comando Vermelho', 'Comando Vermelho')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='modusoperandi',
            name='funcao',
            field=models.CharField(blank=True, choices=[('Chefe', 'Chefe'), ('Menbro', 'Membro')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ocorrencias',
            name='dataDoFato',
            field=models.DateField(verbose_name='Data do Fato'),
        ),
    ]
