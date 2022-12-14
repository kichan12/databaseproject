# Generated by Django 4.0.6 on 2022-11-21 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0015_delete_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.CharField(blank=True, max_length=3, null=True)),
                ('place', models.CharField(blank=True, max_length=20, null=True)),
                ('detail_content', models.TextField(blank=True, max_length=200, null=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project_app.post')),
            ],
        ),
        migrations.DeleteModel(
            name='Company_Comment',
        ),
    ]
