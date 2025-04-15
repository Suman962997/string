from django.urls import path,include
from .views import General_api,view_api,get_one,viewport,forforms,postviewset,view_forms
from rest_framework.routers import DefaultRouter



router=DefaultRouter()
router.register(r'posts',postviewset,basename='post')

urlpatterns=[
    path('api/',General_api.as_view(),name='General_api'),
    path('view/',view_api.as_view(),name="VIEW THAT"),
    path('one/<int:pk>/',get_one.as_view(),name='name'),
    path('list/',viewport.as_view(),name='viewport'),
    path('form/',forforms.as_view(),name='forforms'),
    path('view_datas/',view_forms.as_view(),name='view_forms'),
    path('',include(router.urls)),

]