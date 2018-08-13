from kazoo.client import KazooClient
from . import zookeeper
import json
class kafka:
    def is_kafka_up(self,hostname,port):
        is_zk_up=zookeeper.zookeeper().is_zk_up(hostname,port)
        if is_zk_up:
            zk = KazooClient(hosts=(str(hostname) + ':' + str(port)), read_only=True)
            zk.start()
            children = zk.get_children("/brokers/ids")
            if len(children)>0:
                hosts=""
                for i in range(len(children)):
                    ids_data ,ids_stat= zk.get("/brokers/ids/"+str(children[i]))
                    ids_data_dict=json.loads(ids_data)
                    hosts=hosts+' '+ids_data_dict['endpoints'][0]
                return True,hosts
            else:
                return False,'no kafa broker added to this zookeeper'

        else:
            return False, 'no kafa broker added to this zookeeper'