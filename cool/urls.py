from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,),
    path('swag/', views.swag,),
    path('swag/me/', views.swag_me,),
    path('swag/me/and/you/', views.swag_me_and_you,),
]
