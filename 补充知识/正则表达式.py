import re

s = "Python java makabaka Python itheima"

## match()方法，从头开始匹配，只匹配一项
## span()方法，返回匹配成功项下标
## group()方法，返回匹配成功项内容

result1 = re.match("Python",s)
print(result1)
print(result1.span())
print(result1.group())

## search()方法，匹配整个字符串，从左到右开始，返回第一个

result2 = re.search("Python",s)
print(result2)
print(result2.span())
print(result2.group())

## findall()方法，匹配整个字符串，从左到右开始，以列表形式返回所有匹配内容

result3 = re.findall("Python",s)
print(result3)



## 匹配账号，只能由字母和数字组成，长度限制6到10位

r1 = "^[a-zA-Z0-9]{6,10}$"
s1 = "as456fch1"
print(re.findall(r1,s1))

## 匹配QQ号，纯数字组成，长度限制5到11位，第一位不为0

r2 = "^[1-9]{1}[0-9]{5,11}$"
s2 = "11234567123"
print(re.findall(r2,s2))

## 匹配邮箱，只能由qq,163,gmail这三种邮箱地址组成，例如abc.-fg@qq.com.yt-.aac
## r用于标记字符串为原始字符串，其中的转义字符为普通字符，无其他含义
## ()的作用是将()中的字符作为一个分组，但使用后调用findall()方法会打印()中的内容

r3 = r"(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)"
s3 = "abc.-fg@qq.com.yt-.aac"
print(re.findall(r3,s3))
print(re.match(r3,s3))
print(re.search(r3,s3))


