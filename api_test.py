from ros import Ros

# Initiate Ros object
ros = Ros("http://181.41.245.44/", "admin", "ThinkDiff3r3nt$")

#result = ros.ppp.active(name="oterosBAI")
#print(result)

#test_user = ros.ppp.active(name = "arenasBAI")[0]
#print(test_user)
#del_user = ros.ppp.active.remove(test_user)
#print(del_user)

#from ros.queue import SimpleQueue
#new_queue = SimpleQueue(name="Test", target="192.168.88.0/24", max_limit="10M/10M", disabled=True)
#new_queue = ros.queue.simple.add(new_queue)
#print(new_queue)

#test_queue = ros.queue.simple(name="Test")[0]
#borra = ros.queue.simple.delete(test_queue)
#print(borra)

test_resource = ros.system.resource
print(test_resource)