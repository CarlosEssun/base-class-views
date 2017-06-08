# -*- coding: utf8 -*-
# Create your views here.
from django.shortcuts import render
from django.utils.timezone import now
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

from bcv.models import Publisher
from forms import AuthorForm


class PublisherList(ListView):
    # template_name = "publisher.html" # 定义使用的模板名称
    model = Publisher
    # context_object_name = 'publisher_obj' # 定义返因的字典的名称


class AboutUsView(TemplateView):
    template_name = 'about_us.html'
    # 获取上下文完成逻辑处理

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        if now().weekday() < 5 and now().hour < 18:
            context['open'] = True
        else:
            context['close'] = False
        return context


class ContactView(FormView):
    form_class = AuthorForm
    template_name = 'bcv/author.html'
    success_url = reverse_lazy('author')

    def form_valid(self, form_class):
        # first_name = self.form_class.cleaned_data['first_name']
        # email = self.form_class.cleaned_data['email']
        # last_name = self.form_class.cleaned_data['last_name']
        form_class.save()
        return super(ContactView, self).form_valid(form_class)

# our view
# def contact(request):
#     form_class = AuthorForm

#     # new logic!
#     if request.method == 'POST':
#         form = form_class(data=request.POST)
#         if form.is_valid():
#             first_name = request.POST.get('first_name', '')
#             last_name = request.POST.get('last_name', '')
#             email = request.POST.get('email', '')
#             return redirect('author')
#     else:
#         return render(request, 'bcv/author.html', {
#             'form': form_class,
#         })





