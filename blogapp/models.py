from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200) #title은 Char(문자열)로 이루어지길 원해
    body = models.TextField() #더 대용량 문자로 이루어지길 원해
    date = models.DateTimeField(auto_now_add=True) #auto~: 자동으로 지금 시간 추가
    photo = models.ImageField(blank=True)   #blank는 비워도 된다는 뜻
    
    def __str__(self):  #작성한 글의 title이 목록에 보이도록 하는 함수
        return self.title

