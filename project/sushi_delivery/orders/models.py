from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def str(self):
        return f"{self.first_name} {self.last_name}"


class Dish(models.Model):
    name = models.CharField(max_length=100)
    weight = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def str(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def str(self):
        return f"{self.order}: {self.dish}"