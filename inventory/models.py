from django.db import models


class clients(models.Model):
    """ clients model """
    name = models.TextField() 
    middleName = models.TextField()
    lastName = models.TextField()
    phone = models.CharField(max_length=10)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name + self.lastName


class products(models.Model):
    """ inventory model """
    shortName = models.CharField(max_length=10)
    description = models.TextField()
    pcost = models.FloatField()
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.shortName


class sales_detail(models.Model):
    """ detail of sale model """
    idProduct = models.ManyToManyField(products)
    serial = models.TextField()
    expenses = models.FloatField()
    utility = models.FloatField()
    def __str__(self):
        return self.shortName


class sales(models.Model):
    """ sales model """
    idClient = models.ManyToManyField(clients)
    idDetail = models.ManyToManyField(sales_detail)
    total = models.FloatField()
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)


class servicing(models.Model):
    """ servicing model """
    idClient = models.ManyToManyField(clients)
    idSale = models.ManyToManyField(sales)
    total = models.FloatField()
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)


