from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Reciever(models.Model):
    user_name = models.CharField(max_length=20)
    email_address = models.EmailField()
    weixin_account = models.CharField(max_length=30)

class ReplHistory(models.Model):
    STATUS_CHOICE = (
        ('N','No'),
        ('Y','Yes'),
        ('C','Connecting')
    )
    io_status = models.CharField(choices=STATUS_CHOICE, max_length=10)
    sql_status = models.CharField(choices=STATUS_CHOICE, max_length=10)
    io_error = models.CharField(max_length=200,default='No errors')
    sql_error = models.CharField(max_length=200,default='No errors')
    check_date = models.DateTimeField()

class MysqlMaster(models.Model):
    name = models.CharField(max_length=30)
    repl_user = models.CharField(max_length=10)
    repl_password = models.CharField(max_length=128)
    serv_port = models.CharField(max_length=10)
    op_name = models.CharField(max_length=10)
    op_password = models.CharField(max_length=128)

class MysqlSlave(models.Model):
    name = models.CharField(max_length=30)
    op_name = models.CharField(max_length=10)
    op_password = models.CharField(max_length=128)
    serv_port = models.CharField(max_length=10)
    master = models.ForeignKey(MysqlMaster,on_delete=models.CASCADE)


class DBToRepl(models.Model):
    name = models.CharField(max_length=20)
    is_repl = models.CharField(max_length=5,default='No')
    master = models.ForeignKey(MysqlMaster,on_delete=models.CASCADE)
    slave = models.ForeignKey(MysqlSlave,on_delete=models.CASCADE)


