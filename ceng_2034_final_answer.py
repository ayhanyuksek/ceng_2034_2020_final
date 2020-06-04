#Ayhan Yüksek-170709041

#! /usr/bin/python3
from multiprocessing import Pool
import os
import requests
import uuid
import hashlib

def find_duplicate(name):       
    hashcode=["c8ac40dc6b37096d61c34c9a50a794b5",
                "7ed4550abfccb9470f03ba3b0200a05a",
                "3dcaee2bca739460bd30bb257785b107",
                "c8ac40dc6b37096d61c34c9a50a794b5",
                "3dcaee2bca739460bd30bb257785b107"]
    stat=hashlib.md5(open(name,'rb').read()).hexdigest()
            #for stat in hashcode:
    if hashcode.count(stat)==2:
        print(name,"is duplicate")
            
    else:
        print(name,"is uniq")
             
       

     

def download_file(url,file_name = None):
	r = requests.get(url, allow_redirects = True)
	file = file_name if file_name else str(uuid.uuid4())
	open(file, 'wb').write(r.content)



def parent_child(url):
    child_proc = os.fork()
    if child_proc == 0:
        print("child pid is: ",os.getpid())
        j=0
        for i in url:
            download_file(i,name[j])
            j = j + 1    
        os._exit(0)
      
        
    else:
        os.wait()
        print("parent pid is: ",os.getpid())    
        
     
        
              
url = ["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg","https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png","https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg","http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg","https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"]

name=["icon1","icon2","icon3","icon4","icon5"]


parent_child(url)

with Pool(5) as p:
   print(p.map(find_duplicate, [name[0],name[1],name[2],name[3],name[4]]))

'''
find_duplicate(name[0])
find_duplicate(name[1])
find_duplicate(name[2])
find_duplicate(name[3])
find_duplicate(name[4])
'''


