from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    #path('about/', about_us_view, name='about_us'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    #path("viewevent", views.viewevent, name='viewevent'),
    path("createevent", views.createevent, name='createevent'),

    path("tracker", views.tracker, name='trackingstatus'),
    path("search", views.search, name='search'),
    path("productview", views.productview, name='search'),
    path("checkout", views.checkout , name='checkout'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),



    path('viewevent', views.category_list, name='viewevent'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:category_id>/', views.category_events, name='category_events'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/update/<int:event_id>/', views.update_event, name='update_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('event-chart/', views.event_chart, name='event_chart'),

]

# # urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('signup/', views.signup_view, name='signup'),
#     path('login/', views.login_view, name='login'),
# ]


