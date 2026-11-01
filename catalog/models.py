from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته‌بندی")
    description = models.TextField(blank=True, verbose_name="توضیحات")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    biography = models.TextField(blank=True, verbose_name="زندگینامه")

    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان کتاب")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books", verbose_name="نویسنده")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="books", verbose_name="دسته‌بندی")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="شابک (ISBN)")
    summary = models.TextField(blank=True, verbose_name="خلاصه کتاب")
    publisher = models.CharField(max_length=150, blank=True, verbose_name="ناشر")
    published_year = models.PositiveIntegerField(verbose_name="سال انتشار")
    stock = models.PositiveIntegerField(default=1, verbose_name="موجودی")

    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب‌ها"

    def __str__(self):
        return self.title
