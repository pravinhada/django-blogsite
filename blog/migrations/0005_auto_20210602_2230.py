# Generated by Django 3.2.3 on 2021-06-03 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author'),
        ),
    ]