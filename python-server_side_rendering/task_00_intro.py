def generate_invitations(template, attendees):
    """
    Generate invitation text files from a template and a list of attendee dicts.

    :param template: string template with placeholders:
                     {name}, {event_title}, {event_date}, {event_location}
    :param attendees: list of dictionaries with keys matching placeholders
    """
    # Validate types
    if not isinstance(template, str):
        print("Invalid template type. Expected string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid attendees data. Expected a list of dictionaries.")
        return

    # Validate contents
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    from pathlib import Path

    output_dir = Path(".")
    placeholders = ("name", "event_title", "event_date", "event_location")

    for index, attendee in enumerate(attendees, start=1):
        # Build safe mapping with "N/A" for missing or empty values
        safe_data = {}
        for key in placeholders:
            value = attendee.get(key)
            if value is None or value == "":
                safe_data[key] = "N/A"
            else:
                safe_data[key] = str(value)

        try:
            content = template.format(**safe_data)
        except KeyError as exc:
            # If template contains unexpected placeholder
            missing = str(exc).strip("'")
            print(f"Missing placeholder data for '{missing}', using 'N/A'.")
            safe_data[missing] = "N/A"
            content = template.format(**safe_data)

        file_path = output_dir / f"output_{index}.txt"
        try:
            with file_path.open("w", encoding="utf-8") as file:
                file.write(content)
        except OSError as exc:
            print(f"Failed to write file {file_path}: {exc}")
