# Generated by Django 2.2.5 on 2020-01-31 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0004_remove_ocorrencia_pessoa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Natureza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('natureza', models.TextField(unique=True)),
            ],
            options={
                'verbose_name': 'natureza',
                'verbose_name_plural': 'naturezas',
                'ordering': ('natureza',),
            },
        ),
        migrations.AlterModelOptions(
            name='ocorrencia',
            options={'ordering': ('rai',), 'verbose_name': 'ocorrencia', 'verbose_name_plural': 'ocorrencias'},
        ),
        migrations.RemoveField(
            model_name='infracao',
            name='primeiranatureza',
        ),
        migrations.RemoveField(
            model_name='infracao',
            name='segundanatureza',
        ),
        migrations.AlterField(
            model_name='infracao',
            name='arma_de_fogo',
            field=models.CharField(blank=True, choices=[('revolver', 'Revolver'), ('pistola', 'Pistola'), ('faca', 'Faca')], max_length=10, null=True, verbose_name='arma de fogo'),
        ),
        migrations.AddField(
            model_name='infracao',
            name='primeira_natureza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='natureza1', to='pessoa.Natureza', verbose_name='primeira natureza'),
        ),
        migrations.AddField(
            model_name='infracao',
            name='segunda_natureza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='natureza2', to='pessoa.Natureza', verbose_name='segunda natureza'),
        ),
    ]