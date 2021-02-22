# Generated by Django 3.1.7 on 2021-02-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('complated', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['complated', 'date'],
            },
        ),
    ]