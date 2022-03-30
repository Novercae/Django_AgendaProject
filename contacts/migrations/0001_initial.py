# Generated by Django 2.1.5 on 2022-03-22 18:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='contacts.Category')),
            ],
        ),
    ]