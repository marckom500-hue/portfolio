from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    extrait = models.TextField(max_length=300)
    contenu = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    categorie = models.CharField(max_length=100, default='Développement')
    date_publication = models.DateTimeField(auto_now_add=True)
    publie = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_publication']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre
