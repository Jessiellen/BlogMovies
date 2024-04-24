from django.db import models

# Create your models here.
class Category(models.Model):
    nome = models.CharField(max_length=100)
    id = models.BigAutoField(primary_key=True)
    
    def __str__(self): 
        return self.nome
    
    class Meta:  
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        ordering = ['id']

class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    opinions = models.TextField(default='')
    image = models.ImageField(upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True,blank=True)
    
    def __str__(self): 
        return self.title
    
    class Meta:  
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']