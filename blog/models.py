from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=5)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.postal_code} {self.country}"

    class Meta:
        verbose_name_plural = "Addresses"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=15)

    def __str__(self):
        return self.caption


class BlogPost(models.Model):
    """
        BlogPost model
    """
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts", null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    excerpt = models.CharField(max_length=500)
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    slug = models.SlugField(unique=True, db_index=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} - {self.author}"

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    comment = models.TextField(max_length=400)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ["-id"]
