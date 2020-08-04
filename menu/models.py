"""Menu Models."""
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Dish(models.Model):
    """
    Dish Class.

        name: charfield
        description: charfield

        This model represents a dish that will
        be included in a course which will be
        included into a menu.
    """

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    slug = models.CharField(max_length=255, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self):
        """Slugify name to slug."""
        self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        """String Representation of model."""
        return self.name


class Course(models.Model):
    """
    Course model.

        name: name of course
        description: description of course
    """

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256, null=True, blank=True)
    dishes = models.ManyToManyField(
        Dish,
        through='DishCourse',
        through_fields=('course', 'dish')
    )

    def __str__(self):
        """String repr of model."""
        return self.name


class Menu(models.Model):
    """
    Menu model.

        name: name of the model
        description: description of the menu
        user: user who created the model
    """

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=255, editable=False)
    courses = models.ManyToManyField(
        Course,
        through='CourseMenu',
        through_fields=('menu', 'course')
    )

    def save(self):
        """Slugify name to slug."""
        self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        """String repr of model."""
        return self.name


class CourseMenu(models.Model):
    """Pivot table for Course and Menu."""

    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    order = models.IntegerField(default=0)

    def __str__(self):
        """String repr."""
        return "%s of %s - %s" % (self.course.name, self.menu.name, self.order)

    class Meta:
        """Model Meta."""

        ordering = ['order']


class DishCourse(models.Model):
    """Pivot Table for Dish and Course."""

    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    order = models.IntegerField(default=0)

    def __str__(self):
        """String repr."""
        return "%s of %s - %s" % (self.dish.name, self.course.name, self.order)

    class Meta:
        """Model Meta."""

        ordering = ['order']
