from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    scopes = models.ManyToManyField(Section, related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class ArticleSection(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_sections')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='article_sections')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.article.title} - {self.section.name}"