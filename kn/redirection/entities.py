from kn.leden.mongo import db, SONWrapper, _id, son_property, ObjectId
import kn.leden.entities as Es

rcol = db['redirections']

def redirect_by_short(red):
        return "Blap"

'''
def redirect_by_long(red):
'''

class Redirection(SONWrapper):
    def __init__(self, data):
        super(Redirection, self).__init__(data, rcol)
