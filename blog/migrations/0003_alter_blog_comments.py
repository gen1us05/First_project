# Generated by Django 5.0.4 on 2024-04-18 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='blog.comment'),
        ),
    ]