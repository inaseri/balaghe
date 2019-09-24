from django.db import models

class Language(models.Model):
    title = models.TextField()

class Translator(models.Model):
    title = models.TextField()
    language = models.ForeignKey(Language,on_delete=models.CASCADE)

class Content(models.Model):
    number = models.IntegerField()
    translator = models.ForeignKey(Translator,on_delete=models.CASCADE)
    type = models.IntegerField()
    title_Ar = models.CharField(max_length=500)
    title_En = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()


class Section(models.Model):
    number = models.IntegerField()
    subtitle_fa = models.TextField()
    subtitle_ar = models.TextField()
    body_fa = models.TextField()
    body_ar = models.TextField()
    description_fa = models.TextField()
    description_ar = models.TextField()
    content = models.ForeignKey(Content,on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
