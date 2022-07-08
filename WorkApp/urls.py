from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('',views.Main, name='Main'),
     path('Feedback/',views.Feedback, name="Feedback"),
     path('Register/',views.Register, name="Register"),
     path('delete_workapp/<int:thid>/',views.Delete_Register, name = "delete_workapp"),
     path('edit_reg/<int:thid>/',views.Edit_Reg,name ="edit_reg"),
     path('update_reg/<int:thid>/',views.Update_reg, name = "update_reg"),
     path('Jobs/',views.Jobs, name="Jobs"),
     path('Aboutus/',views.Aboutus, name="Aboutus"),
     path('Sampleresume/',views.Sampleresume, name="Sampleresume"),
     path('Tips/',views.Tips, name="Tips"),
      path('regtable/',views.TableReg, name="regtable"),

]
