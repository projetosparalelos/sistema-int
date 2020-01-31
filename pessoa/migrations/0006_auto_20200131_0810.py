# Generated by Django 2.2.5 on 2020-01-31 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0005_auto_20200131_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arma', models.TextField(unique=True)),
            ],
            options={
                'verbose_name': 'arma',
                'verbose_name_plural': 'armas',
                'ordering': ('arma',),
            },
        ),
        migrations.RemoveField(
            model_name='infracao',
            name='arma_de_fogo',
        ),
        migrations.AddField(
            model_name='infracao',
            name='arma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='armas', to='pessoa.Arma', verbose_name='arma de fogo'),
        ),
    ]