from django.urls import path
from . import views

urlpatterns = [
    path( "home/", views.home, name="supportdesk_home" ),
    path( "create/", views.createRequest, name="supportdesk_create" ),
    path( "myRequest/", views.myRequest, name="supportdesk_myRequest" ),
    path( "completed/<int:id>/", views.completed, name="supportdesk_completed" ),
    path( "reassign/<int:id>/", views.reassign, name="supportdesk_reassign" ),
    path( "agentSingleView/<int:id>/", views.agentSingleView, name="supportdesk_agentSingleView" ),
        
   
]
