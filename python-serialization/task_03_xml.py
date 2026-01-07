#!/usr/bin/python3
"""Serialize/deserialize dictionary to/from XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize 'dictionary' into XML and save to 'filename'."""
    root = ET.Element("data")
    for k, v in dictionary.items():
        child = ET.SubElement(root, str(k))
        child.text = str(v)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Read XML from 'filename' and return a dictionary (string values)."""
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
