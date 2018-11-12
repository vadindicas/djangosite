from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from web import views

urlpatterns = [
    url(r'^journal/', views.getJournal, name='getJournal'),
    url(r'^journalAdd/', views.addJournal, name='JournalAdd'),
    url(r'^add/', views.add, name='add'),
    url(r'^students/', views.students, name='students'),
    url(r'^disp/', views.getDisp, name='disp'),
    url(r'^spec/', views.getSpec, name='spec'),
    url(r'^main/', views.main, name='main'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()