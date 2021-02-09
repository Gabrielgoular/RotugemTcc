# Generated by Django 3.1.4 on 2020-12-15 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alimentos', '0002_auto_20201214_1221'),
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Quantidade')),
                ('alimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alimentos.alimento', verbose_name='Alimento')),
            ],
            options={
                'verbose_name': 'Ingredientes',
            },
        ),
        migrations.RemoveField(
            model_name='receita',
            name='Categoria',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='date',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='status',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='total',
        ),
        migrations.AddField(
            model_name='receita',
            name='quantidade',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10, verbose_name='Quantidade'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receita',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criando em'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='descricao',
            field=models.CharField(max_length=100, verbose_name='Descrição da receita'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='nome',
            field=models.CharField(max_length=20, verbose_name='Nome'),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='receita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receitas.receita', verbose_name='Receita'),
        ),
        migrations.AddField(
            model_name='receita',
            name='ingredientes',
            field=models.ManyToManyField(through='receitas.Ingrediente', to='alimentos.Alimento', verbose_name='Ingredientes'),
        ),
    ]
