from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Tag(models.Model):
    caption = models.CharField(max_length=200)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()



    def __str__(self):
        return self.first_name


class Post(models.Model):
    slug = models.SlugField(unique=True,db_index=True)
    image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True,
                               related_name='posts')
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment_text = models.TextField(
        validators = [MinLengthValidator(3),MaxLengthValidator(500)])
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", null=True)
