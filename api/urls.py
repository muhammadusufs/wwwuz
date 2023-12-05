from django.urls import path
from api.views import add_count
from api.views import WebsiteListAPIView


app_name = 'api'


urlpatterns = [
    path('add-count/', add_count),
    path('websites/', WebsiteListAPIView.as_view()),

]
