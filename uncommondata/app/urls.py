from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('index.html', views.index, name='index_html'),
    
    # Existing endpoints (keep your existing ones)
    path('time/', views.time, name='time'),
    path('sum/', views.sum, name='sum'),
    
    # NEW Step 2 endpoints
    path('app/new/', views.new, name='new_user'),
    path('app/api/createUser/', views.createUser, name='create_user'),
    path('app/uploads/', views.uploads, name='uploads'),
    path('app/api/upload/', views.upload, name='api_upload'),
    path('app/api/dump-uploads/', views.dump_uploads, name='dump_uploads'),
    path('app/api/dump-data/', views.dump_data, name='dump_data'),
    path('app/api/knockknock/', views.knockknock, name='knockknock'),
]