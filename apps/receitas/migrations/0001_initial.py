# Generated by Django 3.1.4 on 2020-12-14 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, verbose_name='Nome Receita')),
                ('date', models.DateField(verbose_name='Data')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total')),
                ('status', models.CharField(choices=[('CRD', 'Criado'), ('FCD', 'Fechado'), ('SALV', 'Salvar')], default='CRD', max_length=5, verbose_name='Status')),
                ('Categoria', models.ManyToManyField(through='receitas.Categoria', to='receitas.Receita', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Receita',
                'verbose_name_plural': 'Receitas',
            },
        ),
    ]
