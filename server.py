# coding=utf-8
import soaplib
from soaplib.core.util.wsgi_wrapper import run_twisted #发布服务
from soaplib.core.server import wsgi
from soaplib.core.service import DefinitionBase  #所有服务类必须继承该类
from soaplib.core.service import soap  #声明注解
from soaplib.core.model.clazz import Array #声明要使用的类型
from soaplib.core.model.clazz import ClassModel  #若服务返回类，该返回类必须是该类的子类
from soaplib.core.model.primitive import Integer,String
class C_ProbeCdrModel(ClassModel):
        __namespace__ = "C_ProbeCdrModel"
        Name=String
        Id=Integer
class AdditionService(DefinitionBase):  #this is a web service
        @soap(Integer,Integer,_returns=String)
        def addition(self,a,b):
                return str(a)+'+'+str(b)+'='+str(a+b)
        @soap(_returns=Array(String))
        def GetCdrArray(self):
                L_Result=["1","2","3"]
                return L_Result
        @soap(_returns=C_ProbeCdrModel)
        def GetCdr(self): #返回的是一个类，该类必须是ClassModel的子类，该类已经在上面定义
                L_Model=C_ProbeCdrModel()
                L_Model.Name=L_Model.Name
                L_Model.Id=L_Model.Id
                return L_Model


if __name__=='__main__':  #发布服务
        try:
                print '服务已经开启'
                from wsgiref.simple_server import make_server
                soap_application = soaplib.core.Application([AdditionService], 'tns')
                wsgi_application = wsgi.Application(soap_application)
                server = make_server('localhost', 7789, wsgi_application)
                server.serve_forever()

        except ImportError:
                print 'error'