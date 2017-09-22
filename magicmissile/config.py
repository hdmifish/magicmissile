import json
from .grasslands import Peacock
log = Peacock()

class Config():
    def __init__(self):
        try:
            with open('config.mm', 'r') as fp:
                self.doc = json.load(fp)
        except IOError as e:
            log.err("Could not open config.mm" + str(e))
            exit()
        except Exception as e:
            log.err("An unexpected error: " + type(e).__name__ + " has occurred: " + str(e))
            exit()

        else:
            if "token" in self.doc:
                self.token = self.doc["token"]
            else:
                log.err("Token missing in config.mm")
                exit(404)

        try:
            self.prefix = self.doc["prefix"]
            log.f("config", "using prefix: " + self.prefix)
            self.owner = self.doc["owner"]
        except KeyError as e:
            log.err("Missing config item: " + str(e))
            exit(404)
        return


    def get(self, field):
        if field is None:
            return "<poof>"
        else:
            try:
                return self.doc[field]
            except KeyError:
                log.err(field + " is not found in config")
        return None

    def save(self):
        try:
            with open('config.mm', 'w') as fp:
                json.dump(self.doc, fp, sort_keys=True, indent=4)
        except PermissionError:
            log.err("No write access to config.mm")
        except IOError as e:
            log.err("Could not open config.mm")
        except Exception as e:
            log.err("An unexpected exception of type: " + type(e).__name__ + " has occurred")

        return

    def load(self):
        try:
            with open('config.mm', r) as fp:
                self.doc = json.load(fp)
            except IOError as e:
                log.err("Could not open config.mm " + str(e))

            else:
                return self.doc
