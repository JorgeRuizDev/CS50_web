from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=64)
    item_description = models.CharField(max_length=4000)
    min_bid = models.FloatField(default=1.0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_owner")
    image = models.URLField(max_length=200)
    categories = models.ManyToManyField(Category)
    users_watching = models.ManyToManyField(User, related_name="user_watchlist", blank=True)
    is_active = models.BooleanField(verbose_name="Item active", default=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.id}) Item {self.item_name} onwed by {self.owner}\n{self.item_description}\nimg_src={self.image}\nCategories: {self.categories}"


class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    bidder = models.OneToOneField(User, unique=True, null=False, on_delete=models.CASCADE)
    item = models.OneToOneField(Item, unique=True, null=False, on_delete=models.CASCADE)
    ammount = models.FloatField()

    def __str__(self):
        return f"{self.id}: {self.bidder} bid {self.ammount} for {self.item}"


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    field = models.CharField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        unique_together = (("user","bid"),)
