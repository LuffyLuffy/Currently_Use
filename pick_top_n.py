#!/usr/bin/env python
#coding:utf-8
__description__ = ''' This script is designed to pick top species
in given table, ordering by sum of the spcies, others are grouped as "Others"
'''
import os,argparse
parser = argparse.ArgumentParser(description ="pick top species")
parser.add_argument("-i","--input",help="otu table or community table",required=True)
parser.add_argument("-n","--topn",default="10", help ="pick number ")

args = parser.parse_args()
infile = args.input
topn = args.topn

rscript='''
df<-read.table(file="'''+infile+'''",header=T,row.names=1,check.names=FALSE,sep="\\t",comment.char=\"\",quote=\"\\t\")
df$sum<-rowSums(df,na.rm=T)
df<-df[order(df$sum,decreasing = T),]
df1<-df[1:'''+topn+''',]
df2<-df['''+topn+'''+1:nrow(df),]
df1["Others",]<-colSums(df2,na.rm=T)
write.table(df1[,-ncol(df1)],"top'''+topn+''''''+infile+'''.txt",row.names=T, col.names=NA,quote=F, sep="\t")

'''
with open('pick_cmd.r','w') as wR:
	wR.writelines(rscript)
os.system("Rscript pick_cmd.r")

