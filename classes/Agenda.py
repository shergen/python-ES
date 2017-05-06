import requests, json

class XPack:
    def __init__(self, user=None, password=None):
            self.__user = "elastic" if not user else user
            self.__password = "MMzAqMxcQdsHtiIwbEkFvZXG" if not password else password
    def __getUser(self):
        return self.__user
    def __setUser(self, user):
        self.__user = user
    def __getPassword(self):
        return self.__password
    def __setPassword(self, password):
        self.__password = password

    user = property(__getUser, __setUser)
    password = property(__getPassword, __setPassword)

class ESCluster:
    def __init__(self, cluster):
        self.__cluster = cluster
        self.__xpack = XPack()

    def __setXpack(self, user, password):
        self.__xpack = XPack(user, password)
    
    
    def __getXPack(self):
        return self.__xpack

    def __getCluster(self):
        return { 'url': self.__cluster, 'login': { 'user': self.__xpack.user ,'password': self.__xpack.password } }

    def __setCluster(self, cluster): 
        self.__cluster = cluster

    cluster = property(__getCluster, __setCluster)
    xpack = property(__getXPack, __setXpack)

class Agenda(ESCluster):
    def __init__(self, cluster, types=None):
        self.__index = 'agenda'
        self.__types = types if types else { 'event': '/events'}
        ESCluster.__init__(self, cluster)
    def __getIndex(self):
        return self.__index
    def __getTypes(self):
        return self.__types
    def __getFullUrl(self):
        return self.cluster['url'] + self.__index + self.__types["event"]


    def getAgenda(self, id):
        r = requests.get(self.__getFullUrl() + "/" + str(id), auth=(self.xpack.user, self.xpack.password))
        return(r.json())
    def putAgenda(self, id, data):
        r = requests.put(self.__getFullUrl() + "/" + str(id), data=json.dumps(data), auth=(self.xpack.user, self.xpack.password))
        return(r.json())
    def deleteAgenda(self, id):
        r = requests.delete(self.__getFullUrl() + "/" + str(id), auth=(self.xpack.user, self.xpack.password))
        return(r.json())

    index = property(__getIndex)
    types = property(__getTypes)
    fullUrl = property(__getFullUrl)
        
