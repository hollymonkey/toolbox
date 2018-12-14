
'''
author :        ming71
creat time :    2018.12.14 11:52
function description：
提取xml文件的中制作voc数据集的基本信息：xmin,xmax,ymin,ymax和class_id，并且写成txt，格式为修改后的NWPU：
class,(xmin,ymin),(xmax,ymax)
attention:批量操作需谨慎，没看明白勿操作！！！
'''

import os
import sys
import cv2


img_path = r"D:\研究生\第一年\dataset\HRSC2016\AllImages" 
anno_path = r"D:\研究生\第一年\dataset\HRSC2016\Annotations"
txt_path =  r"D:\研究生\第一年\dataset\HRSC2016\txt"

Class_ID=[]

files= os.listdir(anno_path)                            #得到文件夹下的所有文件名称
flag=0

for file in files:                                      #每个文件名称
    with open(txt_path+'/'+file[:9]+'.txt','w') as f:   #打开要写的文件
        with open(anno_path+'/'+file,'r') as fd:        #打开要读的文件
            lines=fd.readlines()                        #得到所有行
            for line in lines:                          #得到每行内容
               ##去掉特定类别ID的不记录
               # if 'Class_ID' in line:
               #        if '100000027' in line:
               #             flag=1#不读取潜艇的那四行
               #        else:
               #             flag=0
               # if flag==0:               
                     if('<Class_ID>') in line:  
                        id_number=line[16:25]
                        ##id再分类
                        #class0=['100000002','100000006','100000005','100000012','100000013','100000016','100000032']
                        #class1=['100000003','100000007','100000008','100000009','100000010','100000011','100000015','100000017','100000019']
                        #class2=['100000022']
                        #class3=['100000001','10000004','100000018','100000020','100000024','100000025','100000026','100000028','100000029','100000030']
                        #classes=['1','2','3','4']   #分别是CV CL AP ETC
                        #if id_number in  class0:
                        #    name=classes[0]
                        #if id_number in class1:
                        #    name=classes[1]
                        #if id_number in class2:
                        #    name= classes[2]
                        #if id_number in class3:
                        #    name=classes[3] 
                        ##print(name)
                        ##a=input()                     
                        #f.write(name+',')
                        f.write(id_number+',')
                     if('<box_xmin>') in line:               
                        f.write('('+line[line.find('<box_xmin>')+10:line.find('</box_xmin>')]+',')
                     if('<box_ymin>') in line:
                        f.write(line[line.find('<box_ymin>')+10:line.find('</box_ymin>')]+'),(')
                     if('<box_xmax>') in line:
                        f.write(line[line.find('<box_xmax>')+10:line.find('</box_xmax>')]+',')
                     if('<box_ymax>') in line:
                        f.write(line[line.find('<box_ymax>')+10:line.find('</box_ymax>')]+')'+'\n')
    
     
##源xml获取类别
#for file in files:
#     with open(anno_path+'/'+file,'r') as fd:
#         lines=fd.readlines()
#         for line in lines:
#             if('<Class_ID>') in line:
#                    id = line[16:25]              
#                    if id not in Class_ID:
#                        Class_ID.append(id)
#Class_ID.sort()                                     #从小到大排序
#print(Class_ID,len(Class_ID))

##源xml获取每类出现次数,number与Class_ID索引对应位相对应
#for file in files:
#     with open(anno_path+'/'+file,'r') as fd:
#         lines=fd.readlines()
#         for line in lines:
#             if('<Class_ID>') in line:
#                 for i in range(len(Class_ID)):
#                     if Class_ID[i] in line:
#                            number[i]+=1              
#print(number)


##删除空文件及对应的图片和xml
#txt_files= os.listdir(txt_path)                       
#for file in txt_files:
#    if os.path.getsize(txt_path+'/'+file) == 0:  
#        os.remove(txt_path+'/'+file) 
#        os.remove(img_path+'/'+file[:-4]+'.bmp')
#        os.remove(anno_path+'/'+file[:-4]+'.xml')



#从txt获取类别
txt_files= os.listdir(txt_path)
for file in txt_files:
     with open(txt_path+'/'+file,'r') as fd:
         lines=fd.readlines()
         for line in lines:
                    id = line[:line.find(',')]              
                    if id not in Class_ID:
                        Class_ID.append(id)
Class_ID.sort()                                     #从小到大排序
print(Class_ID,len(Class_ID))


number=[0 for n in range(len(Class_ID))]
for file in txt_files:
     with open(txt_path+'/'+file,'r') as fd:
         lines=fd.readlines()
         for line in lines:
                 for i in range(len(Class_ID)):
                     if Class_ID[i] == line[:line.find(',')]:
                            number[i]+=1              
print(number)
a=input()



     

##查找类别名
#txt_files= os.listdir(txt_path) 
#img_files=os.listdir(img_path)
#c=0
#for file in files:
#    with open(anno_path+'/'+file,'r') as fr:
#        lines=fr.readlines()
#        for line in lines:
#            if 'Class_ID' in line:
#                c+=1
#print(c)
#a=input()


     











