# Generated by Django 2.1.2 on 2018-10-30 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0004_auto_20181029_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, verbose_name='Nome')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curriculo.Curso')),
            ],
            options={
                'db_table': 'DISCIPLINA',
            },
        ),
    ]