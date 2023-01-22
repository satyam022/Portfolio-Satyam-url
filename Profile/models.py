from telnetlib import STATUS

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField


# Create your models here.
class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Aboutprofile(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    Description = RichTextField()
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return self.name


class Certificate(models.Model):
    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    image = models.ImageField(blank=True, null=True, upload_to='avatar/certificates')
    name = models.CharField(max_length=50, blank=True, null=True)
    Description = RichTextField()

    def __str__(self):
        return self.name


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class BlogPage(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="avatar/Blogimage")
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Achievement(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="avatar/achievement")
    title = models.CharField(max_length=200, unique=True)
    details = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title


class ProjectWork(models.Model):
    image = models.ImageField(blank=True, null=True,upload_to="avatar/projectwork")
    name = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ExperienceWork(models.Model):
    profilename = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    compuny_name = models.CharField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.profilename


class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return self.name
