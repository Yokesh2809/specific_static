from django.urls import path
from yoke import views
app_name="yoke"

urlpatterns = [
    path('trail/',views.trial,name="Trial"),
    path('profile/',views.profile,name="profile"),
]