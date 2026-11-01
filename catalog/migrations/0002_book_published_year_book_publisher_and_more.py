from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_year',
            field=models.PositiveIntegerField(default=1402, verbose_name='سال انتشار'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, max_length=150, verbose_name='ناشر'),
        ),
    ]
