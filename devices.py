import re
import simctl
import json


class DeviceSpec:
    def __init__(self, full_name, os):
        [(name, version)] = re.findall(r'^(.+) \((.+)\)$', full_name)
        self._full_name = full_name
        self.name = name
        self.version = version
        self.os = os

    def __str__(self):
        return self._full_name


class _Device:
    def __init__(self, device):
        self.udid = device['udid']
        self._state = device['state']

    def is_booted(self):
        return self._state == 'Booted'


class _DeviceRepository:
    def __init__(self, database):
        self._database = database

    def find_by_spec(self, spec):
       key = '%s %s' % (spec.os, spec.version)
       matches_spec = lambda d: d['name'] == spec.name

       if key in self._database:
           matches = list(filter(matches_spec, self._database[key]))
           return _Device(matches[0]) if matches else None
       else:
           return None


def find_by_spec(spec):
    devices_json = simctl.list_devices()
    database = json.loads(devices_json)['devices']
    return _DeviceRepository(database=database).find_by_spec(spec)

