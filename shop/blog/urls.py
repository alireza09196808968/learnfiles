########################################################################################################
#---------------------------------- import section-----------------------------------------------------#
########################################################################################################
from extensions import converter # for <yyyy:year>
from django.urls import path, register_converter # for register converter.py and specify path
from . import views # include controller
########################################################################################################
#-----------------------------------code execution-----------------------------------------------------#
########################################################################################################
app_name = "blog" # define local variable for using at jinja 2
# register converter
register_converter(converter.fourDigitYearConverter, "yyyy")
# this list is using for define url
urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:post_id>", views.detail, name = "detail"),
    path("archive/<yyyy:year>/", views.archive, name = "archive")
]
