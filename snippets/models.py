from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLES_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜/시각')
    title = models.CharField(max_length=100, blank=True, default='', verbose_name='제목')
    code = models.TextField(verbose_name='코드')
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100, verbose_name='언어')
    style = models.CharField(choices=STYLES_CHOICES, default='friendly', max_length=100, verbose_name='스타일')

    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, verbose_name='소유자')
    highlighted = models.TextField(verbose_name='하이라이팅된 HTML 텍스트')

    class Meta:
        verbose_name = '스니펫'
        verbose_name_plural = '스니펫 목록'
        ordering = ['created']

    def save(self, *args, **kwargs):
        """
        코드 스니펫의 하이라이트 처리된 HTML 표현을 생성하기 위해 `pygments` 라이브러리를 사용함
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
