#!/usr/bin/env python3
"""
Task 0: Simple templating program
"""

import os


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list of attendees
    """

    # ----------------------------
    # Validate input types
    # ----------------------------
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # ----------------------------
    # Handle empty inputs
    # ----------------------------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ----------------------------
    # Process each attendee
    # ----------------------------
    for index, attendee in enumerate(attendees, start=1):
        content = template

        # Replace placeholders with values or "N/A"
        content = content.replace("{name}", str(attendee.get("name") or "N/A"))
        content = content.replace("{event_title}", str(attendee.get("event_title") or "N/A"))
        content = content.replace("{event_date}", str(attendee.get("event_date") or "N/A"))
        content = content.replace("{event_location}", str(attendee.get("event_location") or "N/A"))

        # Output file name
        filename = f"output_{index}.txt"

        # Write to file
        try:
            with open(filename, "w") as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
