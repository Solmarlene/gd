# Generated by Django 3.0.4 on 2020-03-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(db_index=True, max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Masculine'), ('F', 'Feminine'), ('B', 'Both')], max_length=3)),
            ],
        ),
    ]
