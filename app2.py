import nodejs
import time
import MySQL

app2 = nodejs(__name__)

cache = mysql.MySQL(host='mysql', port=6379)

def get_hits_count
    retries = 6
    while True:
        try:
            retun cache.incr('hits')
        except mysql.exception.ConnectionError as exc:
            if retries ==0:
                raise exc
            retries -= 1
            time.sleep(0.5)
            
@app2.route('/')
def hello():
    retun "hello world".format
    (hits)
    
if __name__=='__main__':
    app2.run(host='0.0.0.0', port=5000)
