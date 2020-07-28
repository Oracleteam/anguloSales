from django.db import models


class client(models.Model):
    """ clients model """
    name = models.TextField() 
    middleName = models.TextField()
    lastName = models.TextField()
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name + " " + self.middleName + " " + self.lastName


class product(models.Model):
    """ inventory model """
    shortName = models.CharField(max_length=10)
    description = models.TextField()
    pcost = models.FloatField()
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.description


class sale(models.Model):
    """ sales model """
    idClient = models.ManyToManyField(client)
    total = models.FloatField()
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)


class sale_detail(models.Model):
    """ detail of sale model """
    idProduct = models.ManyToManyField(product)
    idSale = models.ForeignKey(sale, on_delete=models.CASCADE)
    serial = models.TextField()
    expenses = models.FloatField()
    utility = models.FloatField()
    advance = models.FloatField()


class servicing(models.Model):
    """ servicing model """
    idClient = models.ManyToManyField(client)
    idSale = models.ManyToManyField(sale)
    total = models.FloatField()
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)


