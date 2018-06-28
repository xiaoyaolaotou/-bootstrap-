from . import models
from django import forms
from django.forms import fields, widgets


class CreateIdcForm(forms.Form):
    """创建业务验证"""

    virIP = fields.GenericIPAddressField(required=True,
                                         widget=widgets.TextInput(attrs={'class': 'form-inline'}),
                                         error_messages={
                                             'required': '此项不能为空',
                                             'invalid': '请输入正确的IP格式'
                                         })

    physicalIP = fields.GenericIPAddressField(required=True,
                                              widget=widgets.TextInput(attrs={'class': 'form-inline'}),
                                              error_messages={'required': '此项不能为空',
                                                              'invalid': '请输入正确的IP格式'
                                                              })

    application = fields.CharField(required=True,
                                   widget=widgets.TextInput(attrs={'class': 'form-inline'}),
                                   error_messages={'required': '此项不能为空'})

    port = fields.IntegerField(required=False,
                               widget=widgets.TextInput(attrs={'class': 'form-inline'}),
                               error_messages={'invalid': '请输入正确的端口格式'}
                               )

    component = fields.CharField(required=True,
                                 widget=widgets.TextInput(attrs={'class': 'form-inline'}),
                                 error_messages={
                                     'required': '此项不能为空',
                                 })

    Bussiness_idc = fields.ChoiceField(
        choices=models.Bussiness.objects.values_list('id', 'name'),
        # choices=models.Idc.Bussiness_idc_id.objects.values_list('id','name'),
        widget=widgets.Select
    )

    fuzai = fields.ChoiceField(
        choices=models.Idc.type_Lalancing,
        widget=widgets.Select
    )

    principal = fields.CharField(required=True,
                                 widget=widgets.TextInput(attrs={'class': 'form-inline'}),
                                 error_messages={
                                     'required': '此项不能为空',
                                 })

    note = fields.CharField(required=False,
                            widget=widgets.TextInput(attrs={'class': 'form-inline'}),
                            )

    """业务表还有加自动更新"""


    def __init__(self, *args, **kwargs):
        super(CreateIdcForm, self).__init__(*args, **kwargs)
        self.fields['Bussiness_idc'].choices = models.Bussiness.objects.values_list('id', 'name')

class updateIdcForm(forms.ModelForm):
    """更新业务验证"""
    module = models.Idc
    fields = ('virIP',)
