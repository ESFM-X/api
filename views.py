from core import api
from resources import cdp, hackathon

api.add_resource(cdp.cdp_data, '/cdp/<key>')
api.add_resource(hackathon.hackathon_register, '/hackathon/<key>')