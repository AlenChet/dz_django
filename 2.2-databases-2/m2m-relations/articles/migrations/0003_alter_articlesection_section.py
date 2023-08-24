# Generated by Django 4.2.3 on 2023-08-10 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_section_articlesection_article_scopes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesection',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='articles.section'),
        ),
    ]
