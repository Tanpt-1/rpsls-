#coding:gbk
"""
���ܣ�ʯͷ����������ʷ������Ϸ
���ߣ�̷���
���ڣ�2020.3.30
"""

import random
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

def name_to_number(name):
	"""
    ����Ϸ�����Ӧ����ͬ������
    """
	n=name
	if n=="ʯͷ":
	   i=0
	elif n=="ʷ����":
	     i=1
	elif n=="ֽ":
	     i=2
	elif n=="����":
	     i=3
	elif n=="����":
	     i=4
	else:
	     print("Error: No Correct Name")
	     return i#��������
	
	
def number_to_name(number):#������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
	p=number
	if p==0:
	   q="ʯͷ"
	elif p==1:
		 q="ʷ����"
	elif p==2:
		 q="ֽ"
	elif p==3:
		 q="����"
	elif p==4:
		 q="����"
	else:
		print("Error: No Correct Name")
	return q#��������


def rpsls(player_choice):
	choice=player_choice
	return choice


print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
choice=input("����������ѡ��:")
print("----------------")
import name_to_number#���ú���name_to_number
i=name_to_number.name_to_number(choice)
print("����ѡ��Ϊ:"+str(choice))
j=int(random.randint(0,4))
import number_to_name#���ú���number_to_name
q=number_to_name.number_to_name(j)
print("������ѡ��Ϊ:"+str(q))


if j-i==4 or i-j==1 or j-i==3 or i-j==2:##j=4,i=0#i=1,j=0.i=2,j=1.i=3,j=2.i=4,j=3#j=3,i=0.j=4,i=1#i=2,j=0.i=3,j=1.i=4,j=2
   print("��Ӯ��")
elif j-i==2 or i-j==3 or i-j==4or j-i==1:##j=2,i=0.j=3,i=1.j=4,i=2#i=3,j=0.i=4,j=1#i=4,j=0#j=1,i=0.j=2,i=1,j=3,i=2,j=4,i=3
	 print("����Ӯ��")
   
	
