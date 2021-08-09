from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLES_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜/시각')
    title = models.CharField(max_length=100, blank=True, default='', verbose_name='제목')
    code = models.TextField(verbose_name='코드')
    linenoes = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100, verbose_name='언어')
    style = models.CharField(choices=STYLES_CHOICES, default='friendly', max_length=100, verbose_name='스타일')

    class Meta:
        verbose_name = '스니펫'
        verbose_name_plural = '스니펫 목록'
        ordering = ['created']
