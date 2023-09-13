from django.db import models

# Create your models here.
options = (("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"))

class Survey(models.Model):
    name = models.CharField(max_length=30,blank = False)
    Q1 = models.CharField(max_length=10,blank=True,choices = options)
    Q2 = models.CharField(max_length=10,blank=True,choices = options)
    Q3 = models.CharField(max_length=10,blank=True,choices = options)
    Q4 = models.CharField(max_length=10,blank=True,choices = options)
    Q5 = models.CharField(max_length=10,blank=True,choices = options)
    Q6 = models.CharField(max_length=10,blank=True,choices = options)
    Q7 = models.CharField(max_length=10,blank=True,choices = options)
    Q8 = models.CharField(max_length=10,blank=True,choices = options)
    Q9 = models.CharField(max_length=10,blank=True,choices = options)
    Q10 = models.CharField(max_length=10,blank=True,choices = options)
    Q11 = models.CharField(max_length=10,blank=True,choices = options)
    Q12 = models.CharField(max_length=10,blank=True,choices = options)
    Q13 = models.CharField(max_length=10,blank=True,choices = options)
    Q14 = models.CharField(max_length=10,blank=True,choices = options)
    Q15 = models.CharField(max_length=10,blank=True,choices = options)
    Q16 = models.CharField(max_length=10,blank=True,choices = options)
    Q17 = models.CharField(max_length=10,blank=True,choices = options)
    Q18 = models.CharField(max_length=10,blank=True,choices = options)
    Q19 = models.CharField(max_length=10,blank=True,choices = options)
    Q20 = models.CharField(max_length=10,blank=True,choices = options)


    def __str__(self):
        return self.name


class similarityScore(models.Model):
    user1 = models.ForeignKey(Survey,on_delete = models.CASCADE)
    user1Name = models.CharField(max_length = 30,blank=False,default = 'root')
    user2 = models.ForeignKey(Survey,related_name = 'member_of',on_delete = models.CASCADE)
    user2Name = models.CharField(max_length = 30,blank=False,default = 'root')
    similarity_score = models.CharField(max_length = 10,blank = False)

    def __str__(self):
        return self.user1Name
