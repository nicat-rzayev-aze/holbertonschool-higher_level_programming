#!/usr/bin/python3
"""Module for converting XML data to JSON format."""
import json
import xml.etree.ElementTree as ET


def read_xml_and_convert_to_json(xml_filename, json_filename):
    """Reads an XML file and converts its content to a JSON file.

    Args:
        xml_filename (str): The name of the XML file to read.
        json_filename (str): The name of the JSON file to write.

    Returns:
        bool: True if successful, False if an exception occurs.
    """
    try:
        tree = ET.parse(xml_filename)
        root = tree.getroot()

        data = {}
        for child in root:
            data[child.tag] = child.text

        with open(json_filename, "w", encoding="utf-8") as json_f:
            json.dump(data, json_f)

        return True

    except Exception:
        return False
