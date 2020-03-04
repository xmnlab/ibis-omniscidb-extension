
class DDL:
    def hello(self):
        return 'hello'

    def bye(self):
        return 'bye'


def register():
    import ibis

    ibis.omniscidb.client.OmniSciDBClient.hello = DDL.hello
    ibis.omniscidb.client.OmniSciDBClient.bye = DDL.bye
