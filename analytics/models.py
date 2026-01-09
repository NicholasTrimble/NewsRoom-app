from django.db import models
from articles.models import Article

# Create your models here.
class ArticleView(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f"View of {self.article.title} at {self.viewed_at} from {self.ip_address}"