#!/usr/bin/env python
'''
a python script to convert genus table to distance matrix

Contact:huimin.zhang@majorbio.com
'''
import os
import sys
if(len(sys.argv)<=1):
    print("Usage:\n filter_by_colum.py table.txt 1,10:20\n")
    exit()
if(len(sys.argv)<=2):
    print("your colum index:\n")
    os.system("head -n1 "+sys.argv[1]+"  | awk '{for(i=1;i<=NF;i++){print i,$i}}'")
    print("\n")
    print("Usage:\n filter_by_colum.py table.txt 1,10:20;2,14:20;8,:1e^-5\n a string to filter by which colum and a range linked by small:large ,  small and large either can be empty")
    exit()
with open('cmd.r','w') as cmd:
    cmd.write('''

options(stringsAsFactors = F)
library(stringr)
#options("scipen"=0,"digits"=4 )
df<-read.delim("'''+sys.argv[1]+'''",header = T,stringsAsFactors = F,check.names = F,fileEncoding='GBK')
#df<-read.delim("blastx.m8.xls",header = T,stringsAsFactors = F,check.names = F,fileEncoding='GBK')
colnames(df)<-gsub(" ","_",colnames(df))
pick<-"'''+sys.argv[2]+'''"

pick<-matrix(str_split(pick,',')[[1]],ncol=2,byrow=T)
for(i in 1:nrow(pick)){
#i=1
  myrange<-str_split(pick[i,2],':')[[1]]
  large<-as.numeric(myrange[2])
  small<-as.numeric(myrange[1])
  if(!is.na(large)){df<-df[df[,as.numeric(pick[i,1])]<=large,]}
  
  if(!is.na(small)){df<-df[df[,as.numeric(pick[i,1])]>=small,]}
}

write.table(df,paste("filter_","'''+sys.argv[1]+'''",sep=''),row.names=F,sep='\t',quote=F)
''')
os.system('/mnt/ilustre/users/huimin.zhang/newmdt/assess/R-3.5.1/bin/Rscript cmd.r')

