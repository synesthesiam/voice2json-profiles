#!/usr/bin/env python3
import math
import json
import os
import sys
from pathlib import Path

import yaml
from yattag import Doc, indent

NATIVE = {
    "de": "Deutsch",
    "nl": "Nederlands",
    "fr": "Français",
    "el-gr": "Ελληνικά",
    "hi": "Devanagari",
    "it": "Italiano",
    "kz": "қазақша",
    "zh": "中文",
    "pl": "polski",
    "pt-br": "Português",
    "ru": "Русский",
    "es": "Español",
    "sv": "svenska",
    "vi": "Tiếng Việt",
}

STAR = "&#9733;"
SAD_FACE = "&#9785;"

# -----------------------------------------------------------------------------


def main():
    yaml.SafeLoader.add_constructor("!env", env_constructor)
    base_dir = Path(__file__).parent.parent

    closed_reports = {}
    open_reports = {}
    profile_yml = {}

    for profile_dir in sys.stdin:
        profile_dir = base_dir / profile_dir.strip()
        profile_name = profile_dir.name

        with open(profile_dir / "profile.yml", "r") as yaml_file:
            profile_yml[profile_name] = yaml.safe_load(yaml_file)

        closed_path = profile_dir / "test" / "closed" / "report.json"
        open_path = profile_dir / "test" / "open" / "report.json"

        if not open_path.is_file():
            # Try alternative name
            open_path = profile_dir / "test" / "open" / "report_open.json"

        if closed_path.is_file():
            with open(closed_path, "r") as closed_file:
                closed_reports[profile_name] = json.load(closed_file)

        if open_path.is_file():
            with open(open_path, "r") as open_file:
                open_reports[profile_name] = json.load(open_file)
        else:
            print("Missing", closed_path, file=sys.stderr)

    rows = []
    for profile_name in profile_yml:
        print("Processing", profile_name, file=sys.stderr)
        profile = profile_yml[profile_name]
        closed_report = closed_reports.get(profile_name)
        open_report = open_reports.get(profile_name)

        row = {
            "name": profile_name,
            "version": profile["version"],
            "language": profile["language"]["name"],
            "locale": profile["language"]["code"],
            "system": profile["speech-to-text"]["acoustic-model-type"],
        }

        if closed_report:
            row["closed_accuracy"] = closed_report["transcription_accuracy"]
            row["closed_speedup"] = closed_report["average_transcription_speedup"]

        if open_report:
            row["open_accuracy"] = open_report["transcription_accuracy"]
            row["open_speedup"] = open_report["average_transcription_speedup"]

        rows.append(row)

    # Convert to HTML
    rows = sorted(rows, key=lambda r: (r["language"], r["locale"]))
    doc, tag, text = Doc().tagtext()

    with tag("table"):
        # Header
        with tag("thead"):
            with tag("tr"):
                with tag("th"):
                    # Download
                    pass

                with tag("th"):
                    text("Language")

                with tag("th"):
                    text("Locale")

                with tag("th"):
                    text("System")

                with tag("th"):
                    text("Closed")

                with tag("th"):
                    text("Open")

        # Body
        with tag("tbody"):
            for row in rows:
                with tag("tr"):

                    # Download
                    with tag("td"):
                        with tag(
                            "a",
                            href=f'https://github.com/synesthesiam/{row["name"]}/archive/v{row["version"]}.tar.gz',
                        ):
                            text("Download")

                    # Language
                    with tag("td"):
                        lang = row["language"]
                        lang = lang[0].upper() + lang[1:]

                        native = NATIVE.get(row["locale"])
                        if native:
                            lang = f"{lang} ({native})"

                        text(lang)

                    # Locale
                    with tag("td"):
                        text(row["locale"])

                    # System
                    with tag("td"):
                        text(row["system"])

                    # Closed
                    with tag("td"):
                        closed_accuracy = row.get("closed_accuracy")

                        if closed_accuracy:
                            closed_text = to_stars(closed_accuracy)
                            closed_speedup = row.get("closed_speedup")
                            if closed_speedup:
                                closed_speedx = int(math.ceil(float(closed_speedup)))
                                closed_text = f"{closed_text} ({closed_speedx}x)"

                            doc.asis(closed_text)
                        else:
                            with tag("strong"):
                                text("UNTESTED")

                    # Open
                    with tag("td"):
                        open_accuracy = row.get("open_accuracy")

                        if open_accuracy:
                            open_text = to_stars(open_accuracy)
                            open_speedup = row.get("open_speedup")
                            if open_speedup:
                                open_speedx = int(math.ceil(float(open_speedup)))
                                open_text = f"{open_text} ({open_speedx}x)"

                            doc.asis(open_text)
                        else:
                            with tag("strong"):
                                text("UNTESTED")

    print(indent(doc.getvalue()))


# -----------------------------------------------------------------------------


def to_stars(accuracy):
    accuracy = float(accuracy)
    if accuracy < 0.75:
        return SAD_FACE

    num_stars = 5

    if accuracy < 0.8:
        num_stars = 1

    if accuracy < 0.85:
        num_stars = 2

    if accuracy < 0.90:
        num_stars = 3

    if accuracy < 0.95:
        num_stars = 4

    return " ".join([STAR] * num_stars)


def env_constructor(loader, node):
    """Expand !env STRING to replace environment variables in STRING."""
    return os.path.expandvars(node.value)


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
