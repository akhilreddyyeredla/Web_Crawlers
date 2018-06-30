import redis


class RedisQueue(object):
    """Simple Queue with Redis Backend"""

    def __init__(self, name, namespace='queue', **redis_kwargs):
        """The default connection parameters are: host='localhost', port=6379, db=0"""
        # self.__db= redis.Redis(**redis_kwargs)
        self.__db = redis.Redis(host='127.0.0.1', port=6379)
        self.key = '%s:%s' % (namespace, name)

    def qsize(self):
        """Return the approximate size of the queue."""
        return self.__db.llen(self.key)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.qsize() == 0

    def put(self, item):
        """Put item into the queue."""
        self.__db.rpush(self.key, item)

    def get(self, block=False, timeout=None):
        """Remove and return an item from the queue. 

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)

        # if item:
        #   item = item[1]
        return item

    def get_nowait(self):
        """Equivalent to get(False)."""
        return self.get(False)


    def put_into_redis(self,data):
        try:
            queue_obj = RedisQueue('cassandra')
            queue_obj.put(data)
        except Exception as e:
            print e


    def get_from_redis(self):
        queue_obj = RedisQueue('cassandra')
        size = queue_obj.qsize()
        if size > 0:
            return queue_obj.get()
        return None
