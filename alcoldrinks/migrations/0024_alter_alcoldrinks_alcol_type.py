# Generated by Django 5.0.6 on 2024-08-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alcoldrinks', '0023_alter_alcoldrinks_alcol_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alcoldrinks',
            name='alcol_type',
            field=models.CharField(choices=[('Wine', '와인'), ('Sake', '사케'), ('Other', '기타'), ('Soju', '소주'), ('Beer', '맥주'), ('Whisky', '위스키')], default='Other', max_length=20),
        ),
    ]
