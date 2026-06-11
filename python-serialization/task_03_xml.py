#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="unicode", xml_declaration=False)
    print(f"Dictionary serialized to {filename}")

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text

    return result

def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print("Dictionary serialized to [xml_file]")

    deserialized_data = deserialize_from_xml(xml_file)
    print("VDeserialized Data:")
    print(deserialized_data)

if __name__ == "__main__":
    main()
