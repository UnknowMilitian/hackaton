# Generated by Django 3.2.1 on 2022-02-05 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Categoriya')),
                ('slug', models.SlugField(max_length=200, verbose_name='*')),
            ],
            options={
                'verbose_name_plural': 'Categoriyes',
            },
        ),
        migrations.CreateModel(
            name='Turnir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Musobaqaning-Nomi')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Rasimi')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Matn')),
                ('address', models.CharField(max_length=200, verbose_name='Manzil')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Qachon va nechida boshlanishi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'verbose_name_plural': 'Turnirs',
            },
        ),
        migrations.CreateModel(
            name='TurnirsTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeline', models.TimeField(blank=True, null=True, verbose_name='Time Line')),
                ('text', models.CharField(max_length=200, verbose_name="Nima bo'lishi")),
                ('turnir', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='turnirs_time', to='main.turnir')),
            ],
            options={
                'verbose_name_plural': 'Turnirs Time',
            },
        ),
        migrations.CreateModel(
            name='TurnirQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=400, verbose_name='Ism Familiya: ')),
                ('age', models.FloatField(max_length=3, verbose_name='Yosh')),
                ('telephone', models.CharField(max_length=20, verbose_name='Telefon: ')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Qoshimcha fikringiz: ')),
                ('turnir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='main.turnir')),
            ],
        ),
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=400, verbose_name='Ism Familiya: ')),
                ('age', models.FloatField(max_length=3, verbose_name='Yosh')),
                ('staj', models.CharField(max_length=200, verbose_name='Tajribangiz necha oy/yil ?')),
                ('telephone', models.CharField(max_length=20, verbose_name='Telefon: ')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Ozingiz haqingizda qisqacha: ')),
                ('turnir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth', to='main.turnir')),
            ],
        ),
    ]
