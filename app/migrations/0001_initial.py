# Generated by Django 4.0.1 on 2022-02-05 09:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('thought', models.CharField(default='', max_length=100)),
                ('desc', tinymce.models.HTMLField()),
                ('desc1', tinymce.models.HTMLField(default='')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('v', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('email', models.EmailField(default='', max_length=254, null=True)),
                ('website', models.CharField(default='', max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('blog', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.blog')),
                ('user', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Replycomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_body', models.TextField(default='')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('comment', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='app.comment')),
                ('user', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=254, null=True)),
                ('fname', models.CharField(default='', max_length=254, null=True)),
                ('lname', models.CharField(default='', max_length=254, null=True)),
                ('city', models.CharField(default='', max_length=254, null=True)),
                ('address', models.CharField(default='', max_length=254, null=True)),
                ('country', models.CharField(default='', max_length=254, null=True)),
                ('postal_code', models.IntegerField(blank=True, default=0, null=True)),
                ('about_me', models.CharField(default='', max_length=254, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=50)),
                ('skill', models.CharField(default='', max_length=254, null=True)),
                ('dob', models.DateField(default=datetime.datetime.now)),
                ('social_medial_link', models.CharField(choices=[('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Instagram', 'Instagram')], default='', max_length=50)),
                ('website', models.CharField(default='', max_length=254, null=True)),
                ('image', models.CharField(default='', max_length=254, null=True)),
                ('follow', models.IntegerField(blank=True, default=0, null=True)),
                ('following', models.IntegerField(blank=True, default=0, null=True)),
                ('username', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=50)),
                ('blog', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='app.blog')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('email', models.EmailField(default='', max_length=254, null=True)),
                ('website', models.CharField(default='', max_length=50, null=True)),
                ('user', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='user_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
