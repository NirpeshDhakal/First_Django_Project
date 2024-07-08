from django.urls import path
from .views import (home_view,root_page_view,portfolio_view,home_new_view,learning_dtl_view,using_bootstrap_view,temp_inherit_view,about_us_view,contact_us_view)

urlpatterns=[
    
     path("home/", home_view),
     path("",root_page_view, name="root_page"),
     path("portfolio/",portfolio_view,name="portfolio"),
     path("",home_new_view,name="Home"),
     path("learning_dtl/" ,learning_dtl_view, name="learning_dtl"),
     path("using-bootstrap/",using_bootstrap_view, name="using_bootstrap"),
     path("temp_inherit/",temp_inherit_view,name="temp_inherit"),
     path("about-us/",about_us_view,name="about_us"),
     path("contact-us/",contact_us_view,name="contact_us")
     
     

          ]


