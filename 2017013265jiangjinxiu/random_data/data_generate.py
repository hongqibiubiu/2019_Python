# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 17:06:13 2019

@author: hp
"""

import random
import string
class Generate:
    def dic(self):
        dict={}
        k=''.join(random.sample(string.ascii_lowercase, 5))
        v=''.join(random.sample(string.ascii_letters + string.digits, 6))        
        dict[k]=v#生成字典
        return dict
    def string(self):
        s=''.join(random.sample(string.ascii_letters,6))
        #生成字符串
        return s
    def data_crecte(self,size=100000):
        data={}
        for i in range(size):
          data["int"]=random.randint(0,2000)
          data["float"]=random.uniform(3000,5000)
          data["string"]=self.dic()
          data["dic"]=self.string()
          #生成的字典包含整形，浮点，字符串，字典
          yield data
if __name__ == '__main__':
    f = open("output.txt", "w")
    for i in Generate().data_crecte():
       s=str(i)
       f.write(s+'\n')
    f.close()