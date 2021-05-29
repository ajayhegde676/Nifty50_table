from django.urls import path
from app import views


urlpatterns = [

    path('nifty/',views.NiftyView.as_view(),name='nifty')
]


