# Generated by Django 2.0.13 on 2020-04-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('이름', models.CharField(max_length=20)),
                ('설명', models.TextField()),
                ('내용', models.TextField(blank=True, null=True)),
                ('Votes', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='사전',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('단어', models.CharField(max_length=20)),
                ('품사', models.CharField(blank=True, max_length=10, null=True)),
                ('품사2', models.CharField(blank=True, max_length=10, null=True)),
                ('국적', models.CharField(blank=True, max_length=10, null=True)),
                ('Tag', models.CharField(blank=True, max_length=10, null=True)),
                ('출처', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]