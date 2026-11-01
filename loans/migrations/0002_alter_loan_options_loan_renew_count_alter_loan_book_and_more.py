from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loan',
            options={'ordering': ['-borrow_date'], 'verbose_name': 'امانت', 'verbose_name_plural': 'امانت‌ها'},
        ),
        migrations.AddField(
            model_name='loan',
            name='renew_count',
            field=models.IntegerField(default=0, verbose_name='تعداد تمدید'),
        ),
    ]

