#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to filename.
    Values are stored as strings in XML.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = "" if value is None else str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """
    Deserialize XML from filename into a Python dictionary.
    XML values are returned as strings.
    On failure, return an empty dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = "" if child.text is None else child.text
        return result
    except Exception:
        return {}
