# Generated by Django 2.1.2 on 2018-10-31 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0013_disciplina_abrev'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='abrev',
            field=models.CharField(max_length=10, null=True, verbose_name='Abreviação'),
        ),
    ]
