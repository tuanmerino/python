
import facebook
import re
import sys
import time
import os
token = ["   "] # your token 
print"""
	 ____ ____ ____ ____ ___  ____ ____ _  _   ___  ____ ___  
	 |--- |--| |___ |=== |==] [__] [__] |-:_   |==] [__]  | 
Auto likes, read newpages on facebook mod by Tuanmernio 		"""		  
idpages=["pythonvietnam","KemXoiOfficial","yannews","zingmp3","tintucvtv24","K14vn"]

for i in xrange(len(idpages)):	
	graph = facebook.GraphAPI(token)
	profile = graph.get_object(idpages[i])
	posts = graph.get_connections(profile['id'],"posts")
	for post in posts['data']:
		try:
			graph.put_object(post['id'],"likes")
			print "[+] "+str(idpages[i])+': ' +str(post["message"])
			if "video" in post["message"]:
				os.system('color 0c')
			else:
				os.system('color 0f')
	
#			graph.put_comment(post['id'],message=cmt) 
			
		except:
			continue
