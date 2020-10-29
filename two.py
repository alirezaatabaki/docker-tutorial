import redis

# Create connection
r = redis.Redis(host='localhost', port=6379, db=0)

# run code below first
# r.set('name', 'alireza')

# to test above code, run code below
print(r.get('name'))
