from django.urls import path
from similarityCalculation import views
from similarityCalculation.views import surveyView,similarityScoreView

urlpatterns = [
    path('survey/',surveyView.as_view(),name = "submit-response-view"),
    path('survey/',surveyView.as_view(), name = "get-all-survey"),
    path('similarityScore/',similarityScoreView.as_view(), name = "get-similarity-scores-of-users"),
    path('similarityScore/',similarityScoreView.as_view(), name = "calculate-similarity-score-of-user")
]