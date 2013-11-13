from google.appengine.ext import ndb
import logging
import time


class User(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    name = ndb.StringProperty()
    contacts = ndb.StringProperty()
    permissions = ndb.StringProperty()
    
    def to_object(self):
        details = {}
        details["meta"] = {"href": "http://api.bangonph.com/users/?" + self.key.id()}
        details["created"] = str(self.created)
        details["updated"] = str(self.updated)
        details["email"] = self.email
        details["name"] = self.name
        details["id"] = self.key.id()
        details["contacts"] = self.contacts
        details["permissions"] = self.permissions
        
        return details
        


class Distributor(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    name = ndb.StringProperty()
    contact_num = ndb.StringProperty()
    location = ndb.StringProperty()
    email = ndb.StringProperty()
    website = ndb.StringProperty()
    contacts = ndb.KeyProperty()
    facebook = ndb.StringProperty()


class Location(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    name = ndb.StringProperty()
    latlong = ndb.StringProperty()
    featured_photo = ndb.StringProperty()
    death_count = ndb.IntegerProperty()
    affected_count = ndb.IntegerProperty()
    status_board = ndb.StringProperty()
    needs = ndb.JsonProperty()
    status = ndb.JsonProperty()
    images = ndb.JsonProperty()

    def to_object(self, extended=""):
        details = {}
        details["meta"] = {"href": "http://api.bangonph.com/v1/locations/" + str(self.key.id())}
        details["created"] = str(self.created)
        details["updated"] = str(self.updated)
        details["latlong"] = self.latlong
        details["id"] = self.key.id()
        details["featured_photo"] = self.featured_photo
        details["death_count"] = self.death_count
        details["affectedCount"] = self.affected_count
        details["statusBoard"] = self.status_board
        details["needs"] = self.needs
        details["status"] = self.status
        details["images"] = self.images
        return details

    

class DropOffCenter(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    name = ndb.StringProperty()
    drop_off_locations = ndb.StringProperty(repeated=True)
    distributor = ndb.StringProperty(repeated=True)
    address = ndb.StringProperty(repeated=True)
    latlong = ndb.StringProperty()
    destinations = ndb.StringProperty(repeated=True)
    schedule = ndb.StringProperty()
    twitter = ndb.StringProperty()
    facebook = ndb.StringProperty()
    contacts = ndb.StringProperty(repeated=True)
    email = ndb.StringProperty()

    def to_object(self, expand=""):
        details = {}
        details["meta"] = {"href": "http://api.bangonph.com/locations/?" + str(self.key.id())}
        details["created"] = str(self.created)
        details["updated"] = str(self.updated)
        details["drop_off_locations"] = self.drop_off_locations
        details["distributor"] = self.distributor
        details["address"] = self.address
        details["name"] = self.name
        details["latlong"] = self.latlong
        details["destinations"] = self.destinations
        details["schedule"] = self.schedule
        details["twitter"] = self.twitter
        details["facebook"] = self.facebook
        details["contacts"] = self.contacts
        details["email"] = self.email
        details["id"] = self.key.id()

        return details


class Distribution(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    date_of_distribution = ndb.DateTimeProperty()
    contact = ndb.StringProperty()
    destinations = ndb.KeyProperty()
    supply_goal = ndb.JsonProperty()
    actual_supply = ndb.JsonProperty()


    def to_object(self, expand=""):
        details = {}
        details["meta"] = {"href": "http://api.bangonph.com/efforts/?" + str(self.key.id())}
        details["created"] = str(self.created)
        details["updated"] = str(self.updated)
        details["dateOfDistribution"] = str(self.date_of_distribution)

        if expand == "contacts":
            contact_details = {}
            cont = self.contact.get()
            contact_details["contact_details"] = cont.to_object()
            details["contact"] = contact_details
        else:
            if self.contact:
                data = {}
                data["meta"] = {"href": "http://api.bangonph.com/contacts/" + str(self.contact.urlsafe())}
                details["contact"] = data
            else:
                details["contact"] = ""



        if expand == "destinations":
            destination_details = {}
            logging.critical(self.destinations)
            location = self.destinations.get()
            destination_details["destination_details"] = location.to_object()
            details["destination"] = destination_details
        else:
            if self.destinations:
                data = {}
                data["meta"] = {"href": "http://api.bangonph.com/contacts/" + str(self.destinations.urlsafe())}
                details["destinations"] = data
            else:
                details["destinations"] = ""


        details["id"] = self.key.id()
        details["supply_goal"] = self.supply_goal
        details["actual_supply"] = self.actual_supply

        return details

class Subscriber(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    fb_id = ndb.StringProperty()
    distribution = ndb.KeyProperty()

class Contact(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    name = ndb.StringProperty()
    contacts = ndb.StringProperty(repeated=True)
    email = ndb.StringProperty()
    facebook = ndb.StringProperty()
    twitter = ndb.StringProperty()

    def to_object(self, extended=""):
        details = {}
        details["meta"] = {"href": "http://api.bangonph.com/contacts/" + str(self.key.id())}
        details["created"] = str(self.created)
        details["updated"] = str(self.updated)
        details["name"] = self.name
        details["contacts"] = self.contacts
        details["email"] = self.email
        details["facebook"] = self.facebook
        details["twitter"] = self.twitter
        details["id"] = self.key.id()
        return details

class Post(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    twitter = ndb.StringProperty()
    facebook = ndb.StringProperty()
    phone = ndb.StringProperty()
    message = ndb.TextProperty()

    def to_object(self):
        details = {}
        details["meta"] = {"href": "http://api.bangonph.com/posts/" + str(self.key.id())}
        details["created"] = str(self.created)
        details["updated"] = str(self.updated)
        details["name"] = self.name
        details["twitter"] = self.twitter
        details["facebook"] = self.facebook
        details["phone"] = self.phone
        details["message"] = self.message
        
        return details



class LogActivity(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    user = ndb.StringProperty()
    previous_values = ndb.JsonProperty()
    new_values = ndb.JsonProperty
    action = ndb.StringProperty()





