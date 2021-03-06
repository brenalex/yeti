# Generated by Django 2.0.6 on 2018-06-02 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='suggestion',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Participant'),
            preserve_default=False,
        ),
    ]
