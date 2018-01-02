#-*- coding: utf-8 -*-
"""
helper function for parsing xml file
"""
from xml.dom.minidom import parse

def getText(nodelist):
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc


def get_config(fname):
    host = ""
    port =""
    domf = parse(fname)
    config_element = domf.getElementsByTagName("config")[0]
    host_element = config_element.getElementByTagName("host")
    for item in host_element:
        host +=getText(item.childNodes)
    port_element = config_element.getElementByTagName("port")
    for item in port_element:
        port += getText(item.childNodes)
    return str(host),int(port)