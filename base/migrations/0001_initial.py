# Generated by Django 5.0.4 on 2024-04-28 00:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11)),
                ('numInside', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('sentDate', models.DateTimeField(auto_now_add=True)),
                ('isResponse', models.BooleanField(default=False)),
                ('isArchived', models.BooleanField(default=False)),
                ('isDeleted', models.BooleanField(default=False)),
                ('isUnread', models.BooleanField(default=True)),
                ('isHighlighted', models.BooleanField(default=False)),
                ('isSelected', models.BooleanField(default=False)),
                ('currentBox', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.box')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
