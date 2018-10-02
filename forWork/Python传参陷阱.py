def change_str(s):
    s = 'change'


my_str = 'origin'
change_str(my_str)
print(my_str)  # my_str并不会改变还是origin
# 数值类型（int和float）、字符串str、元组tuple都是不可变类型。作为函数参数传递时，不可变类型传递的是内容，所以...
# 不可变对象指的是：该对象所指向的内存中的值不能被改变。
# ----------------------------------------------------------


def change_lst(lst):
    lst.append(5)


my_lst = [1, 2, 3, 4]
change_lst(my_lst)
print(my_lst)  # my_lst 变成了[1, 2, 3, 4, 5]
# 列表list、字典dict、集合set是可变类型。 作为函数参数传递时，可变类型传递的是引用，所以...
# 如果不想改变原来列表的值，参数可以传入列变的拷贝。my_lst[:]
# 可变对象指的是：该对象所指向的内存中的值可以被改变

# 深入理解 参考博客 -> https://www.cnblogs.com/sun-haiyu/p/7096918.html

