# Generated by Django 4.2.5 on 2023-09-13 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('similarityCalculation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='similarityscore',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='similarityCalculation.survey'),
        ),
        migrations.AlterField(
            model_name='similarityscore',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part_of', to='similarityCalculation.survey'),
        ),
    ]
