import classes.Agenda as _

def main():

    test = _.Agenda("https://bdc28cbbb91a2746f0a8c052e9791812.eu-west-1.aws.found.io:9243/")
    print(test.putAgenda(1, {"title" : "CEci est un test", "date": "2017-05-01"}))
    print(test.getAgenda(1))
    print(test.deleteAgenda(1))
    print(test.getAgenda(1))

    """ r = requests.get(cluster.cluster['url'], auth=(cluster.cluster['login']['user'], cluster.cluster['login']['password']))
    print("Status : ", r.status_code)
    print("header", r.headers['content-type'])
    print("encoding", r.encoding)
    print("value", r.text)
    print("Json", r.json())
    """

main()
