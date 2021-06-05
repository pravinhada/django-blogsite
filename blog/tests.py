from django.test import TestCase

from .models import BlogPost, Author, Address


# Create your tests here.

class BlogPostTest(TestCase):

    def setUp(self):
        address = Address.objects.create(street="123 pine street", city="Manchester", state="", postal_code=2230,
                                         country="UK")
        author = Author.objects.create(first_name="Jen", last_name="Anderson", email_address="test@test.com",
                                       address=address)

        BlogPost.objects.create(title="Test", rating=1, image="test.jpg", excerpt="Testing",
                                content="Testing this model", author=author)

    def test_blogpost_not_empty(self):
        posts = BlogPost.objects.all()
        post_count = posts.count()
        self.assertTrue(post_count > 0, msg="BlogPost is more than 0")

    def test_blogpost_author(self):
        post = BlogPost.objects.get(title="Test")
        author = post.author
        self.assertEqual("Jen", author.first_name, msg="Jen is the author first name")

    def test_blogpost_author_address(self):
        post = BlogPost.objects.get(title="Test")
        address = post.author.address
        self.assertEqual("Manchester", address.city, msg="Manchester is the city where author lives")
