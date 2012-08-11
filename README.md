# 微博API调试器（Weibo API Debugger）

## 依赖于

1. [bottle](https://github.com/defnull/bottle)
1. [sae](https://github.com/SAEPython/saepythondevguide)
1. [jinja2](https://github.com/mitsuhiko/jinja2)
1. [beaker](http://www.bitbucket.org/bbangert/beaker)
1. [weibo.py](https://github.com/michaelliao/sinaweibopy)

本地运行需要安装[sae本地调试环境](http://saepy.sinaapp.com/topic/21/%E8%BD%BB%E6%9D%BE%E6%90%AD%E5%BB%BAsae-python-%E6%9C%AC%E5%9C%B0%E8%BF%90%E8%A1%8C%E7%8E%AF%E5%A2%83)。

## 原理

在服务器端进行Weibo OAuth认证。客户端向服务器端发送远程过程调用（RPC）请求，服务器端返回调用微博API得到的原始json数据。

