from django.db import models


class MovieManager(models.Manager):
    def validator(self, form):
        errors = {}

        if len(form['title']) < 2:
            errors["title"] = "Show title must be at least three characters."
        if len(form['network']) < 3:
            errors['network'] = "Show network must be at least three characters."
        if not form['air_date']:
            errors['date'] = "You must enter an air date."
        if len(form['description']) > 0 and len(form['description']) < 10:
            errors['description'] = "Show description is optional, but if entered, it must be at least ten characters."
        return errors

class Movie(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    air_date = models.DateField()
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MovieManager()

    def __repr__(self):
        return f"<ID {self.id} - Title: {self.title} Network: {self.network}>"