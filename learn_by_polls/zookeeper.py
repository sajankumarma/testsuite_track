class zookeeper:
    def is_zk_up(self,hostname,port):
        from kazoo.client import KazooClient
        from kazoo.client import KazooState
        try:
            zk = KazooClient(hosts=(str(hostname)+':'+str(port)), read_only=True)
            zk.start()
            if KazooState.CONNECTED == zk.client_state:
                return True
            else:
                return False
        except:
            return False
