# Generated by Django 3.2.1 on 2022-02-05 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_question_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
