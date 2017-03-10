# -*- coding: utf-8 -*-
import os # path manipulation
import shutil

path0 = ''
path1 = ''

#遍历某个目录及其子目录下所有文件拷贝到某个目录中
def copyFiles2(srcPath,dstPath): 
        if not os.path.exists(srcPath): 
                print "src path not exist!" 
        if not os.path.exists(dstPath): 
                os.makedirs(dstPath)  
#递归遍历文件夹下的文件，用os.walk函数返回一个三元组
        for root,dirs,files in os.walk(srcPath): 
                for eachfile in files:
                        if eachfile.find(".txt")>0 :
                                shutil.copy(os.path.join(root,eachfile),dstPath) 
                                print eachfile+" copy succeeded"
        
if __name__ == '__main__':
	copyFiles2(path0,path1)


	
