from django.db import models

class MovieManager(models.Manager):
    def process(self, form):
        title = form['title']
        network = form['network']
        air_date = form['air_date']
        description = form['description']
        Movie.objects.create()
        print(form)
        return form
        


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