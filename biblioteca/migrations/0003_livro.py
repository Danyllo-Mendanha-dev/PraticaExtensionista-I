# Generated by Django 5.2.3 on 2025-06-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_leitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('isbn', models.CharField(help_text='Ex: 978-85-333-0222-0', max_length=17, unique=True)),
                ('autor', models.CharField(max_length=100)),
                ('genero', models.CharField(blank=True, max_length=50, null=True)),
                ('data_publicacao', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('disponivel', 'Disponivel'), ('emprestado', 'Emprestado')], default='disponivel', max_length=10)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
            },
        ),
    ]
