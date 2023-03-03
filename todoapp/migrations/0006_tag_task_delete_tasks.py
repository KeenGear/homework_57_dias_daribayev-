# Generated by Django 4.1.6 on 2023-03-03 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_remove_tasks_text_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255, null=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('in_progress', 'In Progress'), ('done', 'Done')], default='todo', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tags', models.ManyToManyField(to='todoapp.tag')),
            ],
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
    ]
