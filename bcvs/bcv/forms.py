# coding: utf8
# Date: '2017-06-07'
# Author: King.gp
# Description: defind publisher form
# Version: 0.1.0


from django.forms import ModelForm, Textarea
from models import Author
from django.utils.translation import ugettext_lazy as _

# define publisher  form


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': Textarea(attrs={'cols': 80, 'rows': 20})
        }
        labels = {
            'first_name': _('Writer'),
        }
        help_texts = {
            'first_name': _(u'输入作者名称')
        }
        error_messages = {
            'first_name': {
                'max_length': _(u'这个名称己经超最大长度'),
                'min_length': _(u'这个名称不满足最小要求长度')
            }
        }





