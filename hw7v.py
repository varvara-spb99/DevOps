"""Напишите программу, которая читает данные из файлов
/etc/passwd и /etc/group на вашей системе и выводит
следующую информацию в файл output.txt:
1. Количество пользователей, использующих все имеющиеся
интерпретаторы-оболочки.
( /bin/bash - 8 ; /bin/false - 11 ; ... )
2. Для всех групп в системе - UIDы пользователей
состоящих в этих группах.
( root:1, sudo:1001,1002,1003, ...)"""
f1 = open('/etc/passwd')
lst1 = f1.readlines()
f1.close()

count1 = {}
for i in lst1:
    i = i.rsplit(":", maxsplit=1)
    if i[1].replace("\n", "") not in count1:
        count1[i[1].replace("\n", "")]=1
    else:
        count1[i[1].replace("\n", "")] += 1

out = open('/home/varya/Documents/homework/output.txt', 'w')
for key, value in count1.items():
    out.write("{0} - {1}".format(key, value) + "\n")
out.write("\n\n")
out.close()


f2 = open('/etc/group')
lst2 = f2.readlines()
f2.close()

count2 = {}
for i in lst2:
    i2 = i.split(":")
    if i.rsplit(":", maxsplit=1)[1] != "\n":
        count2[i2[0]]=i.rsplit(":", maxsplit=1)[1].replace("\n", "")

out = open('/home/varya/Documents/homework/output.txt', 'a')
for key, value in count2.items():
  out.write("{0}: {1}".format(key,value)+"\n")
out.close()


