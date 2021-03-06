# Generated by Django 3.0 on 2020-01-26 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('image', models.ImageField(default='img.jpg', upload_to='')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True)),
                ('date', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True)),
                ('author', models.CharField(max_length=50)),
                ('image', models.ImageField(default='img.jpg', upload_to='')),
                ('categories', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Categories')),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]
