from django.urls import path,include
from . import views

urlpatterns = [
    # ex: /exlorer/2/
    # path("<int:df_id>/", views.dataset, name='dataset'),
    # path('<int:df_id>/sample/<sample_name>/how/<how>/<strand>/fastqc', views.fastqc),
    # path('<int:df_id>/sample/<sample_name>/', views.sample),
]