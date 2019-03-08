import urequests
import json


def createApplication(url, login, rn, label=[]):
    body = {
        "m2m:ae": {
            "api": "app-sensor",
            "rr": "true",
            "lbl": label,
            "rn": rn
        }
    }

    header = {
        'X-M2M-Origin': login,
        'Content-Type': 'application/json;ty=2'
    }
    r = urequests.post(url, data=json.dumps(body), headers=header)
    return r.status_code, r.text, r


def createContainer(url, login, rn, mni=1000):
    body = {
        "m2m:cnt": {
            "rn": rn,
            "mni": mni
        }
    }

    header = {
        'X-M2M-Origin': login,
        'Content-Type': 'application/json;ty=3'
    }

    r = urequests.post(url, data=json.dumps(body), headers=header)
    return r.status_code, r.text, r


def createContentInstance(url, login, con, label=[]):
    body = {
        "m2m:cin": {
            "cnf": "application/json",
            "lbl": label,
            "con": con
        }
    }

    header = {
        'X-M2M-Origin': login,
        'Content-Type': 'application/json;ty=4'
    }

    r = urequests.post(url, data=json.dumps(body), headers=header)
    return r.status_code, r.text, r


def getResource(url, login):
    body = {}

    header = {
        'X-M2M-Origin': login,
        'Content-Type': 'application/json'
    }

    r = urequests.get(url, data=json.dumps(body), headers=header)
    return r.status_code, r.text, r


def deleteResource(url, login):
    body = {}

    header = {
        'X-M2M-Origin': login,
        'Content-Type': 'application/json'
    }

    r = urequests.delete(url, data=json.dumps(body), headers=header)
    return r.status_code, r.text, r


def subscribeResource(url, login, rn, nu):
    body = {
        "m2m:sub": {
            "rn": rn,
            "nu": nu,
            "nct": 2
        }
    }

    header = {
        'X-M2M-Origin': login,
        'Content-Type': 'application/json;ty=23'
    }

    r = urequests.post(url, data=json.dumps(body), headers=header)
    return r.status_code, r.text, r