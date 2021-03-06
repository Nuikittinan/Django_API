from django.urls import path
from django.urls.resolvers import URLPattern
from .views import * #ดึงมาทุกฟังชั่นใน views.py
urlpatterns = [
    path('',Home ),
    path('api/all-todolist/',all_todolist), #localhost:8000/api/all-todolist
    path('api/post-todolist', post_todolist),
    path('api/update-todolist/<int:TID>', update_todolist),
    path('api/delete-todolist/<int:TID>', delete_todolsit),
    path('api/register', register_app),
    path('api/login', login_app),
    path('api/deviceall', Deviceall),
    path('api/data/<str:parameter>', get_somedata),
    path('api/graph/<str:graphparameter>', get_temp),
    # path('api/graph2/<str:graphspo2>',get_spo2)

]
