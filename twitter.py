#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor xkonde 03

import  tweepy
import json
import urllib
import string
import re
import sys
import os
    #kilce k vebove aplikaci
consumer_key = 'ywgOReM95Xv8wkAvIwG5miwve'     
consumer_secret = 'fGG7xhbnaigHFA0YzYomGL6VJZugpJNO0ndLL94og1xQ18LFSr'
access_token = '3242558031-QCKiOnvLZIjJC6Jlfg7ZJmHZJkcSTfDfvsGzXym'
access_token_secret = 'f0NU42YGRJ1f9CKVq88ZKk2wzhSpULOLeeaPlUDDkVS8V'


def aktulizace():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth) #načteni objektu z twitru
    c=0
    f = open("twiter.txt","r") 
    radky=""
    line =f.read(1)
    celek=""
    while (line!='\n') : # načetne pirvniho id  twitu 
        radky=radky+line
        line =f.read(1)
    print radky
    for status in tweepy.Cursor(api.user_timeline,id="@zdrojak").items(): #načita všech twitu od zdrojaklu
        c+=1
        neco=status.id
        neco2=str(neco)
        
        if(neco2==radky):   #pokud narazime na id ktere mame už zapsane tak vyskočime z načitani
            break
        uprava2=status.text.encode("utf-8") # ukladani do souboru
        uprava2=str(uprava2)
        celek=celek+neco2
        celek=celek+"\n"
        celek=celek+uprava2
        celek=celek+"\n"
        
        
        print status.author.name
        print neco
        #ulkadani html stranky ktere bylo na twitu
        for url in status.entities['urls']:
            jmeno=url['expanded_url']
            fc = urllib.urlopen(jmeno)
            data = fc.read()
            fc.close()
            #data=unicode(data,'utf-8')
            data=unicode(data, encoding="utf-8", errors="ignore")
            data=data.encode("utf-8")
            #v nazvu souboru nesmi byt určite znaky
            #jmeno=re.sub("\\","N",jmeno)
            jmeno=re.sub("/","+",jmeno)
            jmeno=re.sub("\.","+",jmeno)
            jmeno=re.sub("\?","+",jmeno)
            jmeno=re.sub(":","+",jmeno)
            jmeno=re.sub("\*","+",jmeno)
            jmeno=re.sub("<","+",jmeno) 
            jmeno=re.sub(">","+",jmeno)
            jmeno=re.sub("\|","+",jmeno)
            #uprava delkz jmena
            if (len(jmeno)>50):
                jmeno=jmeno[:50]
                
            celek=celek+"kod stranek: "
            uprava=str(url['expanded_url'])
            celek=celek+uprava
            celek=celek+"\n"
            jmeno="stranky_twiter/"+jmeno+".html"
            stranka = open(jmeno,"w")
            stranka.write(data)
            stranka.close()
        celek=celek+"*************************************************************************************"
        celek=celek+"\n"
        #podminka aby jsme nešli moc do historie
        if(c>150):
            break
    f.close()

    #ukladani abysme meli nejnov3i twity na začatku souboru
    f = open("twiter.txt","r")
    aloha =f.read()
    f.close()
    celek=celek+aloha
    f = open("twiter.txt","w")
    f.write(celek)
    f.close()

def inializace():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    c=0
    pag = 1
    #vytvoreni adresare na html soubory
    os.mkdir("stranky_twiter",0777)
    c=0
    f = open("twiter.txt","w")
    for status in tweepy.Cursor(api.user_timeline,id="@zdrojak").items():
        c+=1
        neco=status.id
        neco2=str(neco)
        #ukldame primo do souboru
        uprava2=status.text.encode("utf-8")
        f.write(neco2)
        f.write("\n")
        f.write(uprava2)
        f.write("\n")
        
        print status.author.name
        print neco
        for url in status.entities['urls']:
            jmeno=url['expanded_url']
            fc = urllib.urlopen(jmeno)
            data = fc.read()
            fc.close()
            #data=unicode(data,'utf-8')
            data=unicode(data, encoding="utf-8", errors="ignore")
            data=data.encode("utf-8")
            #jmeno=re.sub("\\","N",jmeno)
            jmeno=re.sub("/","+",jmeno)
            jmeno=re.sub("\.","+",jmeno)
            jmeno=re.sub("\?","+",jmeno)
            jmeno=re.sub(":","+",jmeno)
            jmeno=re.sub("\*","+",jmeno)
            jmeno=re.sub("<","+",jmeno) 
            jmeno=re.sub(">","+",jmeno)
            jmeno=re.sub("\|","+",jmeno)
            if (len(jmeno)>50):
                jmeno=jmeno[:50]
            f.write("kod stranek: ")
            f.write(url['expanded_url'])
            f.write("\n")
            jmeno="stranky_twiter/"+jmeno+".html"
            stranka = open(jmeno,"w")
            stranka.write(data)
            stranka.close()
        f.write("*************************************************************************************")
        f.write("\n")
        if(c>50):
            break
    f.close()

def main():
   #royhodnuti jestli aktualizeje nebo ne ztahujeme
    if os.path.isfile("twiter.txt"):
        aktulizace()
    else:
        inializace()
    print "dokonceno"
    
if __name__ == '__main__':
    main()    




