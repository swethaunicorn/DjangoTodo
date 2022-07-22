from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save,post_delete
from django.dispatch import receiver


class Task(models.Model):
    title               =models.CharField(max_length=250,  null=True)
    description         =models.TextField(null=True, blank=True)
    complete            =models.BooleanField(default=False)
    author              =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug                =models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['complete']

@receiver(post_delete,sender=Task)
def submission_delete(sender,instance,**kwargs):
    instance.delete(False)

def pre_save_Task_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.author.username + '-' + instance.title)

pre_save.connect(pre_save_Task_receiver,sender=Task)