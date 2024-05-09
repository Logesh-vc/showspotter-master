from django.shortcuts import render
from django.views.generic import ListView, TemplateView, ListView, CreateView, DeleteView, DetailView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User



class theatre_manager_create(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    fields = '__all__'
    model = models.theatre_manager
    template_name = 'dashboard/theatre_manager_form.html'


class theatre_manager_view(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    context_object_name = 'theatre_managers'
    model = models.theatre_manager
    template_name = 'dashboard/theatre_manager_view.html'
    permission_required = 'dashboard.theatre_manager.can_view_theatre_manager'


class theatre_manager_detail_view(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    context_object_name = 'theatre_managers'
    model = models.theatre_manager
    template_name = 'dashboard/theatre_manager_detail_view.html'
    permission_required = 'dashboard.theatre_manager.can_view_theatre_manager'




class theatre_manager_delete_view(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    context_object_name = 'theatre_managers'
    model = models.theatre_manager
    success_url = reverse_lazy("dashboard:theatre-manager-view")
    permission_required = 'dashboard.theatre_manager.can_delete_theatre_manager'




class theatre_create(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    fields = '__all__'
    model = models.theatre



class theatre_view(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    context_object_name = 'theatre'
    model = models.theatre
    template_name = 'dashboard/theatre_view.html'
    permission_required = 'dashboard.theatre.can_view_theatre'


class theatre_detail_view(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    context_object_name = 'theatre'
    model = models.theatre
    template_name = 'dashboard/theatre-detail-view.html'
    permission_required = 'dashboard.theatre.can_view_theatre'





class theatre_delete_view(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    context_object_name = 'theatre'
    model = models.theatre
    success_url = reverse_lazy("dashboard:theatre-view")
    permission_required = 'dashboard.theatre.can_delete_theatre'




class screen_create(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    fields = '__all__'
    model = models.screen



class screen_view(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    context_object_name = 'screen'
    model = models.screen
    template_name = 'dashboard/screen_view.html'
    permission_required = 'dashboard.screen.can_view_screen'


class screen_detail_view(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    context_object_name = 'screen'
    model = models.screen
    template_name = 'dashboard/screen-detail-view.html'
    permission_required = 'dashboard.screen.can_view_screen'




class screen_delete_view(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    context_object_name = 'screen'
    model = models.screen
    success_url = reverse_lazy("dashboard:screen-view")
    permission_required = 'dashboard.screen.can_delete_screen'




class show_create(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    fields = '__all__'
    model = models.show



class show_view(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    context_object_name = 'show'
    model = models.show
    template_name = 'dashboard/show_view.html'
    permission_required = 'dashboard.show.can_view_show'


class show_detail_view(LoginRequiredMixin, DetailView):
    context_object_name = 'show'
    model = models.show
    template_name = 'dashboard/show-detail-view.html'
    permission_required = 'dashboard.show.can_view_show'





class show_delete_view(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    context_object_name = 'show'
    model = models.show
    success_url = reverse_lazy("dashboard:show-view")
    permission_required = 'dashboard.show.can_delete_show'




class movie_create(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    fields = '__all__'
    model = models.movie
    permission_required = 'dashboard.movie.can_add_movie'


class movie_view(PermissionRequiredMixin, ListView):
    context_object_name = 'movie'
    model = models.movie
    template_name = 'dashboard/movie_view.html'
    permission_required = 'dashboard.movie.can_view_movie'


class movie_detail_view(PermissionRequiredMixin, DetailView):
    context_object_name = 'movie'
    model = models.movie
    template_name = 'dashboard/movie-detail-view.html'
    permission_required = 'dashboard.movie.can_view_movie'





class movie_delete_view(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    context_object_name = 'movie'
    model = models.movie
    success_url = reverse_lazy("dashboard:movie-view")
    permission_required = 'dashboard.movie.can_delete_movie'


