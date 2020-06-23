from flask import Flask
from flask import render_template,request
import os
import json

cached= []
class Intern:
	"""user class ,so we can use , user.name,user.point, ...
	"""
	
	def __init__(self,args):
		for key, value in args.items():
			setattr(self,key.lower(),value)
	
	def __getattr__(self,arg):
		return None
	
	def __gt__(self,other):
		# to sort with point
		return float(self.points) > float(other.points)
	
	def __str__(self):
		return self.points
		
	def __repr__(self):
		return str(self)
file= os.path.join(os.getcwd(),"intern.json")
app = Flask(__name__)

@app.route("/",methods=["GET",'POST'])
def home():
	if not cached:
		#to avoid opening the file each the server receive request, 
		# open once and save...
		users_file = json.load(open(file))
		cached.extend(users_file)
	else:
		users_file = cached
	users = []
	for user in users_file:
		users.append(Intern(user))
	users.sort(reverse=True)
	top3 = users[:3] #top 3 users
	return render_template("index.html",users=users,top3=top3)
	#best = users[:3]

if __name__ == "__main__":
	app.run()