from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/', null=True)

# id 또한 저장이 된다 자동으로

# 규격화시키는 역할 
# db는 냉장고 
# model은 냉장고 매니저와 같음 요소를 특정 규격으로 규격화 해줌

# 규격을 미리 지정 -> url로 요청 받음 -> view가 처리 -> model에서 가공 -> template에 내용을 얹어서
# -> view가 다시 처리 -> url 쏴줌 
# url은 처음이자 마지막에 작동 