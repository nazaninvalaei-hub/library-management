from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import loans.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True, verbose_name='تاریخ امانت')),
                ('due_date', models.DateField(default=loans.models.get_due_date, verbose_name='موعد بازگشت')),
                ('return_date', models.DateField(blank=True, null=True, verbose_name='تاریخ واقعی بازگشت')),
                ('status', models.CharField(choices=[('borrowed', 'امانت داده شده'), ('returned', 'بازگردانده شده')], default='borrowed', max_length=20, verbose_name='وضعیت')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.book', verbose_name='کتاب')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'امانت',
                'verbose_name_plural': 'امانت‌ها',
            },
        ),
    ]

