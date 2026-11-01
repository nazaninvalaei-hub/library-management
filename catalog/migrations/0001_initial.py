import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('biography', models.TextField(blank=True, verbose_name='زندگینامه')),
            ],
            options={
                'verbose_name': 'نویسنده',
                'verbose_name_plural': 'نویسندگان',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام دسته‌بندی')),
                ('description', models.TextField(blank=True, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'دسته‌بندی',
                'verbose_name_plural': 'دسته‌بندی‌ها',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان کتاب')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='شابک (ISBN)')),
                ('summary', models.TextField(blank=True, verbose_name='خلاصه کتاب')),
                ('stock', models.PositiveIntegerField(default=1, verbose_name='موجودی')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='catalog.author', verbose_name='نویسنده')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='catalog.category', verbose_name='دسته‌بندی')),
            ],
            options={
                'verbose_name': 'کتاب',
                'verbose_name_plural': 'کتاب‌ها',
            },
        ),
    ]
