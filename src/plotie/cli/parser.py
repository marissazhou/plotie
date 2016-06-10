import argparse


def _comma_separated(text):
        return [item for item in text.split(",") if item.strip()]

parser = argparse.ArgumentParser(
    description=(
        "Plotie"
    )
)

parser.add_argument(
    "-d", "--debug",
    dest="is_debugging",
    action="store_true",
    help="Run in debug mode."
)
parser.add_argument(
    "-V", "--version",
    dest="wants_version",
    action="store_true",
    help="Display the version number."
)

parsed_args = parser.parse_args()

__all__ = ("parsed_args", "parser")
