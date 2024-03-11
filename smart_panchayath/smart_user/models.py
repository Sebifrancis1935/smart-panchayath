from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    Adhar = models.IntegerField()
    pin_code = models.IntegerField()
    phone_no = models.IntegerField(max_length=15)
    mail = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Panchayath(models.Model):
    p_name = models.CharField(max_length=100)
    p_id = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.p_name


class Muncipality(models.Model):
    m_name = models.CharField(max_length=100)
    m_id = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.m_name


class Panchayath_details(models.Model):
    p_name = models.CharField(max_length=100)
    pincode = models.IntegerField()

    def __str__(self):
        return self.p_name


class Muncipality_details(models.Model):
    m_name = models.CharField(max_length=100)
    pincode = models.IntegerField()

    def __str__(self):
        return self.m_name


class Corporation(models.Model):
    c_name = models.CharField(max_length=100)
    c_id = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.c_name


class Corporation_details(models.Model):
    c_name = models.CharField(max_length=100)
    pincode = models.IntegerField()

    def __str__(self):
        return self.c_name
