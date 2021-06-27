from django.db import models

class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    head0=models.CharField(max_length=500,default="")
    content_head0=models.CharField(max_length=500,default="")
    head1=models.CharField(max_length=500,default="")
    content_head1=models.CharField(max_length=500,default="")
    head2=models.CharField(max_length=500,default=0)
    content_head2=models.CharField(max_length=500,default=0)
    pub_date=models.DateField()
    thumbnail=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.title
