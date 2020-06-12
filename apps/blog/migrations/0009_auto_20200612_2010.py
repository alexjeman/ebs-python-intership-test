# Generated by Django 3.0.7 on 2020-06-12 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200612_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_set', to='blog.Blog'),
        ),
    ]
