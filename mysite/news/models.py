from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Name')
    content = models.TextField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data of publication')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Published')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']
