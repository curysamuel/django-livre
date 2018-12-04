# from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from events.models import Event
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class EventList(ListView):
    model = Event
    template_name = 'event_list.html'

    def get_queryset(self):
        queryset = Event.objects.filter(author=self.request.user).all()
        return queryset


@method_decorator(login_required, name='dispatch')
class EventView(DetailView):
    template_name = 'event_detail.html'
    model = Event


@method_decorator(login_required, name='dispatch')
class EventCreate(CreateView):
    model = Event
    fields = ['name', 'participantes']
    success_url = reverse_lazy('event_list')
    template_name = 'event_form.html'

    def form_valid(self, form):
        evento = form.save(commit=False)
        evento.author = self.request.user
        evento.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EventUpdate(UpdateView):
    model = Event
    fields = ['name', 'participantes', 'author']
    success_url = reverse_lazy('event_list')
    template_name = 'event_form.html'


@method_decorator(login_required, name='dispatch')
class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('event_list')
    template_name = 'event_confirm_delete.html'
