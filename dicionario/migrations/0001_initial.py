# Generated by Django 2.2.4 on 2019-08-21 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subarea', models.CharField(max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dicionario.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Termo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termo', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='imagens/')),
                ('expressao', models.CharField(max_length=200)),
                ('aprovado', models.BooleanField(default=True)),
                ('subarea', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dicionario.SubArea')),
            ],
        ),
        migrations.CreateModel(
            name='Sugestao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('termo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dicionario.Termo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
