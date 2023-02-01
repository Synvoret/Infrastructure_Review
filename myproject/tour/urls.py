# import pandas as pd
from django.urls import path
from . import views

app_name = 'tour'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_tour', views.NewTour.as_view(), name='new-tour'),
    path('charts/<str:type_chart>', views.Charts.as_view(), name='charts'),
    path('history', views.History.as_view(), name="history"),
    path('edit_tour/<int:id>', views.edit_tour, name='edit-tour'),
    path('delete/<int:id>', views.delete_tour, name='delete-tour')
]
