from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, HttpResponseBadRequest
from dashboard import models
from dashboard.models import movie, show, theatre, screen, User
from django.views.generic import DetailView, ListView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.contrib import messages
from main.models import TicketsForm,booking1
from django.contrib.auth.decorators import login_required
from .forms import logint,registertable
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View



# Create your views here.

def index(request):
    slider_images = movie.objects.raw('SELECT id,slideshow_image FROM dashboard_movie ORDER BY id DESC LIMIT 4')

    thumbnail_images = movie.objects.raw('SELECT id,thumbnail_image FROM dashboard_movie ORDER BY id DESC LIMIT 8')

    trailer = movie.objects.raw('SELECT id,trailer FROM dashboard_movie ORDER BY id DESC LIMIT 6')

    return render(request, 'main/index.html',
                  {'slider_images': slider_images, 'thumbnail_images': thumbnail_images, 'trailer': trailer})


class movies(ListView):
    context_object_name = 'movie'
    model = models.movie
    template_name = 'main/movie-view.html'


class movie_detail_view(DetailView):
    context_object_name = 'movie'
    model = models.movie
    template_name = 'main/movie-detail-view.html'


class movie_booking_theatre(DetailView):
    context_object_name = 'movie'
    model = models.movie
    template_name = 'main/movie-booking-theatre.html'


class show_details(LoginRequiredMixin, DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TicketsForm
        show_id = self.kwargs['pk']
        Show = show.objects.get(pk=show_id)
        context['tickets_booked'] = booking1.objects.filter(show=Show)
        return context

    context_object_name = 'show'
    model = models.show
    template_name = 'main/booking-page.html'


@login_required
def book_ticket(request, pk=None, id=None):
    data = TicketsForm(request.POST)
    Booking = data.save(commit=False)
    Show = show.objects.get(pk=pk)
    user = User.objects.get(pk=id)
    Booking.show = Show
    Booking.user = user

    if Booking.row_num == 0 or Booking.col_num == 0 or Booking.row_num > Show.screen.no_of_rows or Booking.col_num > Show.screen.no_of_columns:
        return HttpResponseBadRequest("Invalid ticket number")

    if not request.session.session_key:
        request.session.save()
    Booking.session = request.session.session_key

    try:
        existing_tix = booking1.objects.get(row_num=Booking.row_num, col_num=Booking.col_num, show=Show)
        if existing_tix.session == Booking.session and existing_tix.status == 1:
            if existing_tix.status == 1:
                existing_tix.delete()
            else:
                Booking = existing_tix
        else:
         return HttpResponseBadRequest("This ticket has already been reserved")
    except booking1.DoesNotExist:
        pass

    Booking.save()

    return redirect('main:booked', pk=pk)
    


class account(LoginRequiredMixin, DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs['pk']
        username = self.kwargs['user']
        u = get_object_or_404(User, pk=user_id)
        context['tickets_booked'] = booking1.objects.filter(user=u)
        if u.username == username:
            context['test'] = username
            return context

    context_object_name = 'user'
    model = models.User
    template_name = 'main/account.html'


class account_update(LoginRequiredMixin, UpdateView):
    context_object_name = 'user'
    model = models.User
    fields = ['username', 'first_name', 'last_name', 'email', ]
    template_name = 'main/account_form.html'
    success_url = reverse_lazy('main:index')


class account_delete(LoginRequiredMixin, DeleteView):
    context_object_name = 'user'
    model = models.User
    template_name = 'main/user_confirm_delete.html'
    success_url = reverse_lazy('main:logout')



def user_signup(request) :

    if request.method == 'POST':
      if (request.POST.get('username')) and request.POST.get('first_name') and request.POST.get(
            'Last_name') and request.POST.get('email') and request.POST.get('password') and request.POST.get(
            'confirm_password'):
        i=request.POST.get('username')
        em=request.POST.get('email')
        if User.objects.filter(username=i).exists():
            return render(request, "main/invalidus.html")
        if User.objects.filter(email=em).exists():
            return render(request, "main/invalidem.html")
        reg = User()
        reg.username=request.POST.get('username')
        reg.first_name=request.POST.get('first_name')
        reg.last_name=request.POST.get('Last_name')
        reg.email=request.POST.get('email')
        reg.password=request.POST.get('password')
        y = request.POST.get('confirm_password')
        username=request.POST.get('username')
        password=request.POST.get('password')

        if reg.password == y:
            reg.save()
            user = User.objects.filter(username=username, password=password).first()
            auth_login(request, user)
            redirect('main:account', pk=user.id, user=user.username)
            return redirect('main:index')

        else:
             return render(request,"main/invalidpw.html")
    form=registertable()
    return render(request, 'main/signup.html', {'form': form} )

def login(request):
    if request.method == 'POST':
        form = logint(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.filter(username=username, password=password).first()
            if user is not None:
              auth_login(request, user)
              redirect('main:account', pk=user.id, user=user.username)
              return redirect('main:index')
            else:
              return render(request,"main/invlog.html")
    else:
        form=logint()
        return render(request, "registration/login.html", context={'form': form})


def search(request):
    if request.method == 'POST':
        search_query = request.POST['search']

        if search_query:
            result = movie.objects.filter(
                Q(name__icontains=search_query) | Q(hero__icontains=search_query) | Q(heroine__icontains=search_query))

            if result:
                return render(request, 'main/search.html', {'results': result, 'search_query': search_query})
            else:
                messages.error(request, 'Sorry no results found')
        else:
            return HttpResponseRedirect('/')

    return render(request, 'main/search.html')


class booked(LoginRequiredMixin, DetailView):
    context_object_name = 'show'
    model = models.show
    template_name = 'main/confirm_movie.html'


def cancel_ticket(request, pk=None):
    Ticket = booking1.objects.get(pk=pk)
    Ticket.delete()
    return redirect('main:index')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')
