# -*- coding: utf-8 -*-
from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
# 公司新闻
class ArticleNews(models.Model):
    title = models.CharField(max_length=1000, verbose_name=u'标题', default=u'')
    tag = models.CharField(max_length=20, verbose_name=u'文章标签', default=u'')
    intro = models.TextField(max_length=1000, verbose_name=u'文章介绍', default=u'')
    pic = models.ImageField(upload_to='web/news/img', verbose_name='文章缩略图', default=u'')
    content = UEditorField(verbose_name=u'内容', imagePath=u'web/news/img/', filePath=u'web/news/file/', default=u'')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='发布时间', null=True)
    object = models.Manager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'新闻'


# 行业白皮书
class IndustryArticle(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'标题')
    intro = models.CharField(max_length=200, verbose_name=U'简介')
    pic = models.ImageField(upload_to='web/news/img', verbose_name='文章缩略图')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='发布时间', null=True)
    content = UEditorField(verbose_name=u'内容', imagePath=u'web/news/img/', filePath=u'web/news/file/', default=u'')
    object = models.Manager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'行业白皮书'
