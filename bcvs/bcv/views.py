# -*- coding: utf8 -*-
# Create your views here.
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from bcv.models import Publisher, Book
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
        form_class.save()  # 保存数据到数据库
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


# 动态查询

class PublisherBookList(ListView):
    template_name = 'bcv/book_by_publisher.html'
    context_object_name = 'book_publisher'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)
    # 添加额外的方法

    def get_context_data(self, **kwargs):
        context = super(PublisherBookList, self).get_context_data(**kwargs)
        context['publisher'] = self.publisher
        return context



