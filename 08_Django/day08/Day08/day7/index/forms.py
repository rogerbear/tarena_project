from django import forms
from .models import *

# 为topic下拉列表初始化数据　－　元祖
TOPIC_CHOICE = (
    ('level1', '好评'),
    ('level2', '中评'),
    ('level3', '差评'),
)


class RemarkForm(forms.Form):
    # 1.创建一个subject属性，表示评论标题，对应成文本框
    # 1.1 label : 生成控件前的提示文本
    # 1.2 initial : 给控件初始化的文本，等同于　value　给的初始值
    subject = forms.CharField(label='标题', initial='初始数据')

    # 2.　创建一个email属性，表示邮箱，对应生成email控件
    # 2.1 label ：生成空间前的提示文本
    email = forms.EmailField(label='邮件')

    # 3. 创建一个message属性，表示评论内容，对应生成　多行文本域
    # 3.1 label ：生成空间前的提示文本
    # 3.2 widget :让当前属性变为一个多行文本域
    message = forms.CharField(label='内容', widget=forms.Textarea)

    # 4. 创建一个　topic 属性，表示评论级别，对应生成一个下拉列表
    # 4.1 choices : 指定下拉列表中的选项元组们
    topic = forms.ChoiceField(label='评价', choices=TOPIC_CHOICE)

    # 5. 创建一个　isSave　属性，表示一个复选框
    isSave = forms.BooleanField(label='是否保存')


class RegisterForm(forms.Form):
    uname = forms.CharField(label='用户名称')
    upwd = forms.CharField(label='用户密码',
                           widget=forms.PasswordInput)
    uemail = forms.EmailField(label='用户邮箱')
    uage = forms.CharField(label='用户年龄')


# 创建LoginForm类，继承自 forms.ModelForm 并关联 models 与　form
class LoginForm(forms.ModelForm):
    # 创建Meta内部类，关联Models
    class Meta:
        # 1. 关联的Models
        model = Users
        # 2.定义要生成控件的属性们
        # fields = '__all__'
        fields = ['uname', 'upwd']
        # 3.　每个控件对应的label
        labels = {
            'uname': '用户名称',
            'upwd': '用户密码',
            # 'uemail': '电子邮箱',
            # 'uage': '用户年龄',
        }

# 小部件的使用，继承自forms.Form


class WidgetForm1(forms.Form):
    uname = forms.CharField(
        label='用户名称',
        widget=forms.TextInput
    )

    upwd = forms.CharField(
        label='用户密码',
        widget=forms.PasswordInput
    )


class WidgetForm2(forms.Form):
    uname = forms.CharField(
        label='用户名称',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请输入用户名称',
            }
        )
    )

    upwd = forms.CharField(
        label='用户密码',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请输入密码',
            }
        )
    )


# 关联　form 以及 models
class WidgetForm3(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
        labels = {
            'uname': '用户名称',
            'upwd': '用户密码',
            'uemail': '电子邮箱',
            'uage': '用户年龄',
        }
        widgets = {
            'uname': forms.TextInput(attrs={
                'placeholder': '请输入用户名',
                'class': 'form-control',
            }),
            'upwd': forms.PasswordInput(attrs={
                'placeholder': '请输入密码',
                'class': 'form-control',
            }),
            'uemail': forms.EmailInput(attrs={
                'placeholder': '请输入邮箱',
                'class': 'form-control',
            })
        }
