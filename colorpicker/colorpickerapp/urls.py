from django.urls import path
from colorpickerapp.views import ColorPickerView

urlpatterns=[
    path('', ColorPickerView.as_view(), name='paint'),
]