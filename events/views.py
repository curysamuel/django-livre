from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from events.models import Event, Band
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateResponseMixin
from django.http import JsonResponse

class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response
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
    fields = ['name', 'participantes', 'band']
    success_url = reverse_lazy('event_list')
    template_name = 'event_form.html'

    def form_valid(self, form):
        evento = form.save(commit=False)
        evento.author = self.request.user
        evento.save()
        return super().form_valid(form)


class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['name', 'participantes', 'author', 'band']
    success_url = reverse_lazy('event_list')
    template_name = 'event_form.html'


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('event_list')
    template_name = 'event_confirm_delete.html'


class BandList(LoginRequiredMixin, ListView):
    model = Band
    template_name = 'band_list.html'

    def get_queryset(self):
        queryset = Band.objects.filter(author=self.request.user).all()
        return queryset


class BandView(LoginRequiredMixin, DetailView):
    template_name = 'band_detail.html'
    model = Band


class BandCreate(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    model = Band
    fields = ['name', 'estilo']
    success_url = reverse_lazy('band_list')
    template_name = 'band_form.html'

    def form_valid(self, form):
        band = form.save(commit=False)
        band.author = self.request.user
        band.save()
        return super().form_valid(form)


class BandUpdate(LoginRequiredMixin, UpdateView):
    model = Band
    fields = ['name', 'estilo']
    success_url = reverse_lazy('band_list')
    template_name = 'band_form.html'


class BandDelete(LoginRequiredMixin, DeleteView):
    model = Band
    success_url = reverse_lazy('band_list')
    template_name = 'band_confirm_delete.html'
