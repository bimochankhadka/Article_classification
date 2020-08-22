# Generated by Django 2.0.4 on 2018-07-24 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.CharField(max_length=1000, null=True)),
                ('Commented_date', models.DateTimeField(editable=False)),
                ('Commented_by', models.CharField(max_length=250, null=True)),
                ('Article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blogs.Post')),
            ],
        ),
    ]
