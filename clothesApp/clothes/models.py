from django.db import models


class role(models.Model):
    db_table = "role_table"
    name = models.CharField(max_length=20)


class user(models.Model):
    db_table = "user_table"
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    role = models.ForeignKey(role, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


class category(models.Model):
    db_table = "category_table"
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=5)


class clothes(models.Model):
    db_table = "clothes_table"
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    size = models.CharField(max_length=15)
    text = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    gender = models.BooleanField()
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
