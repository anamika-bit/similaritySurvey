# Generated by Django 4.2.5 on 2023-09-13 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('similarityCalculation', '0002_alter_similarityscore_user1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='similarityscore',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_of', to='similarityCalculation.survey'),
        ),
    ]
