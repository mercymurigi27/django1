from django.urls import path



from . import views

urlpatterns = [

    path('',views.home,name='pictures-home'),
    path('search/',views.search,name='search-results'),
    path('filter/',views.filter_location,name='filter-results')
]    
