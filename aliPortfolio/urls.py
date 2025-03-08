from django.urls import path
from . import views

urlpatterns = [
    # HOME Page
    path('', views.index, name='index'),
    # About Page
    path('about', views.about, name='about'),
    # Gallery Page
    path('gallery', views.gallery, name='gallery'),
    # BTS "Behind The Scenes" Page
    path('behindthescenes', views.behindthescenes, name='bts'),
    # Login Page
    path('login', views.login, name='login'),
    # Control Dashboard
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/home', views.dashboard_home, name='dashboard_home'),
    path('dashboard/about', views.dashboard_about, name='dashboard_about'),
    path('dashboard/gallery', views.dashboard_gallery, name='dashboard_gallery'),
    path('dashboard/bts', views.dashboard_bts, name='dashboard_bts'),
    # About Page Dashboard
    path('dashboard/bts/bts_new', views.bts_new, name='bts_new'),
    path('dashboard/bts/bts_edit/<int:bts_id>', views.bts_edit, name='bts_edit'),
    path('dashboard/bts/bts_delete/<int:bts_id>', views.bts_delete, name='bts_delete'),

    # About Page Dashboard
    path('dashboard/about/about_edit', views.about_edit, name='about_edit'),
    path('dashboard/about/skill_edit/<int:skill_id>', views.skill_edit, name='skill_edit'),
    path('dashboard/about/education_edit/<int:education_id>', views.education_edit, name='education_edit'),
    path('dashboard/about/experience_edit/<int:experience_id>', views.experience_edit, name='experience_edit'),
    path('dashboard/about/experience_delete/<int:experience_id>', views.experience_delete, name='experience_delete'),
    path('dashboard/about/education_delete/<int:education_id>', views.education_delete, name='education_delete'),
    path('dashboard/about/new_education', views.new_education, name='new_education'),
    path('dashboard/about/new_experience', views.new_experience, name='new_experience'),
    # Home Page Dashboard
    path('dashboard/home/client_edit/<int:client_id>', views.client_edit, name='client_edit'),
    path('dashboard/home/client_add', views.client_add, name='client_add'),
    path('dashboard/home/home_edit', views.home_edit, name='home_edit'),
    path('dashboard/home/info_edits', views.info_edits, name='info_edits'),
    path('dashboard/home/client_delete/<int:client_id>', views.client_delete, name='client_delete'),
    # Gallery Page Dashboard
    path('dashboard/about/gallery_edit/<int:gallery_id>', views.gallery_edit, name='gallery_edit'),
    path('dashboard/about/gallery_delete/<int:gallery_id>', views.gallery_delete, name='gallery_delete'),
    path('dashboard/about/gallery_header_edit', views.gallery_header_edit, name='gallery_header_edit'),
    path('dashboard/about/new_gallery', views.new_gallery, name='new_gallery'),
]
