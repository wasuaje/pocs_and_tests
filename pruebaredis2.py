import redis
r = redis.Redis("localhost", port=6380)
from hashlib import md5
 
def add_user(username, fullname, password):
    if r.sadd("users", username):
        r.set("user:%s:fullname" % username, fullname)
        r.set("user:%s:password" % username, md5(password).hexdigest() )
        return True
    else:
        return False

def authenticate_user(username, password):    
	#if username in r.smembers("users"):	
	if r.sismember("users", username):					
		passhash = md5(password).hexdigest()
		if passhash == r.get("user:%s:password" % username):
			return True
		else:	
			return False
	else:		
		return False

def delete_user(username):
    if username in r.smembers("users"):
        r.srem("users", username)
        r.delete("user:%s:fullname" % username)
        r.delete("user:%s:password" % username)
        return True
    else:
        return False
#print add_user("bob", "Bob Barker", "priceisright")
print r.smembers("users")
#print r.get("user:bob:fullname")
#print r.get("user:bob:password")
#add_user("adam", "Adam Smith", "wealthofnations")
#add_user("carol", "Carol Burnett", "eartug")

#print authenticate_user("ghost", "idontexist!")
print authenticate_user("carol", "eartug")
print authenticate_user("adam", "wealthofnations")
print authenticate_user('bob', 'priceisright')
print delete_user("adam")
