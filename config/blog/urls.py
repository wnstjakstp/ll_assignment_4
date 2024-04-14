from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # READ
    path('', views.home, name='home'), #  name ='home' 은 url에 별명을 붙여준 것

    # DETAIL READ
    path('blog/<int:blog_id>', views.detail, name='detail'), 
    # path converter blog id를 숫자로 바꿔줌 1이 view에도 넘어감

    # CREATE
    path('blog/new', views.new, name='new'), # url의 new라는 이름은 home.html의 새글작성하기 url의 new임
    path('blog/create', views.create, name='create'),

    # UPDATE
    path('blog/edit/<int:blog_id>', views.edit, name='edit'),
    path('blog/update/<int:blog_id>', views.update, name='update'),

    # DELETE
    path('blog/delete/<int:blog_id>', views.delete, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)