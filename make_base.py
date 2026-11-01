path = r"E:\pycharm\library\templates\base.html"; html = """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}سامانه کتابخانه{% endblock %}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.rtl.min.css">
    <style>
        body { font-family: Tahoma, Vazir, sans-serif; background-color: #f8f9fa; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4 shadow">
        <div class="container">
            <a class="navbar-brand fw-bold" href="/">سامانه مدیریت کتابخانه</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbars">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbars">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" href="/">کاتالوگ کتاب‌ها</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/loans/my-loans/">امانت‌های من</a>
                    </li>
                </ul>
                <ul class="navbar-nav ms-auto">
                    {% if user.is_authenticated %}
                        <li class="nav-item d-flex align-items-center me-3 text-light">
                            <span>کاربر: <strong>{{ user.username }}</strong></span>
                        </li>
                        <li class="nav-item">
                            <form action="/accounts/logout/" method="POST" class="d-inline">
                                {% csrf_token %}
                                <button type="submit" class="btn btn-outline-danger btn-sm">خروج</button>
                            </form>
                        </li>
                    {% else %}
                        <li class="nav-item">
                            <a class="btn btn-primary btn-sm" href="/accounts/login/">ورود به حساب</a>
                        </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>

    <div class="container">
        {% if messages %}
            {% for msg in messages %}
                <div class="alert alert-{{ msg.tags }} alert-dismissible fade show" role="alert">
                    {{ msg }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            {% endfor %}
        {% endif %}

        {% block content %}
        {% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""; open(path, "w", encoding="utf-8").write(html); print("BASE_CREATED!")
