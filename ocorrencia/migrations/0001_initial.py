# Generated by Django 2.2.5 on 2020-02-01 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoa', '0016_auto_20200201_1830'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arma', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'arma',
                'verbose_name_plural': 'armas',
                'ordering': ('arma',),
            },
        ),
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
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('rai', models.IntegerField(blank=True, null=True)),
                ('data_do_fato', models.DateField(verbose_name='Data do Fato')),
                ('descricao', models.CharField(blank=True, max_length=500, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='criado por')),
            ],
            options={
                'verbose_name': 'ocorrencia',
                'verbose_name_plural': 'ocorrencias',
                'ordering': ('rai',),
            },
        ),
        migrations.CreateModel(
            name='PessoaOcorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='criado por')),
                ('ocorrencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ocorrencias1', to='ocorrencia.Ocorrencia')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pessoas_ocorrencias', to='pessoa.Pessoa')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OcorrenciaVeiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='criado por')),
                ('ocorrencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ocorrencia.Ocorrencia')),
                ('veiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoa.Veiculo')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Infracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('qualificacao', models.CharField(choices=[('aut', 'Autor'), ('coaut', 'Co-Autor'), ('part', 'Participe'), ('vit', 'Vitima')], default='aut', max_length=5)),
                ('status', models.CharField(choices=[('vivo', 'Vivo'), ('morto', 'Morto'), ('preso', 'Preso'), ('solto', 'Solto')], default='vivo', max_length=5)),
                ('arma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='armas', to='ocorrencia.Arma', verbose_name='arma de fogo')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='criado por')),
                ('natureza', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='naturezas', to='ocorrencia.Natureza', verbose_name='natureza')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pessoa.Pessoa')),
            ],
            options={
                'verbose_name': 'infração',
                'verbose_name_plural': 'infrações',
                'ordering': ('-created',),
            },
        ),
    ]
