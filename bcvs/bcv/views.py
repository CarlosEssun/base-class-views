# -*- coding: utf8 -*-
# Create your views here.
from time import timezone

from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from bcv.models import Publisher, Book, Author
from forms import AuthorForm
from django.http import HttpResponse
from django.views.decorators.http import require_GET
import json


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

# 关键字查询


class BookDetailView(DetailView):
    model = Book
    slug_field = 'title'  # model 中读取的属性
    slug_url_kwarg = 'title'  # url中捕获的参数名称
    template_name = 'bcv/book_by_publisher.html'

    # def get(self, request, slug):  # 返回的是一个dict
    #     # context = super(BookDetailView, self).get(slug)
    #     acct = get_object_or_404(self.model.book_objects, title=slug)
    #     return render(request, self.template_name, {'book_model': acct}) 

    def get_queryset(self, **kwargs):
        self.queryset = super(BookDetailView, self).get_queryset()
        self.title = self.queryset.filter(title=self.kwargs['title'])
        return self.title

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['bookdetail'] = self.title
        return context
