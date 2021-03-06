
#作用域

#在Python中，是通过_前缀来实现的。正常的函数和变量名是公开的（public），可以被直接引用

'''
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的
文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函
数或变量，但是，从编程习惯上不应该引用private函数或变量。
private函数或变量不应该被别人引用，
'''


