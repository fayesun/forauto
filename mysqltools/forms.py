from django import forms

class MysqlReplFrom(forms.Form):
    ip_addr = forms.GenericIPAddressField(label='ip address')
    tcp_port = forms.CharField(label='port', max_length=5)
    admin_name = forms.CharField(label='admin', max_length=10)
    admin_pass = forms.CharField(label='password', max_length=20,widget=forms.PasswordInput)