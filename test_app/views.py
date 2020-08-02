from django.shortcuts import render
from django.views.generic import FormView
from test_app.forms import TestModelForm


class TestView(FormView):
    form_class = TestModelForm
    template_name = 'test_app/index.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(TestView, self).form_valid(form)
    
