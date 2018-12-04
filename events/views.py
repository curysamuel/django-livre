from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from events.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin


class EventList(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'event_list.html'

    def get_queryset(self):
        queryset = Event.objects.filter(author=self.request.user).all()
        return queryset


class EventView(LoginRequiredMixin, DetailView):
    template_name = 'event_detail.html'
    model = Event


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'participantes']
    success_url = reverse_lazy('event_list')
    template_name = 'event_form.html'

    def form_valid(self, form):
        evento = form.save(commit=False)
        evento.author = self.request.user
        evento.save()
        return super().form_valid(form)


class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['name', 'participantes', 'author']
    success_url = reverse_lazy('event_list')
    template_name = 'event_form.html'


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('event_list')
    template_name = 'event_confirm_delete.html'
