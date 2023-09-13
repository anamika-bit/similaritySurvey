from django.urls import path
from similarityCalculation import views
from similarityCalculation.views import surveyView

urlpatterns = [
    path('survey/',surveyView.as_view(),name = "submit-response-view"),
    path('survey/',surveyView.as_view(), name = "get-all-survey")
]