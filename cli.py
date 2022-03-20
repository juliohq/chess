import argparse
import sys
from typing import List, Optional


def main(args: Optional[List[str]] = sys.argv[1:]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="The new way to play chess")

    parser.add_argument("--play-as", metavar="COLOR", type=str, required=True)
    parser.add_argument("--chess960", action="store_true")
    parser.add_argument("--ai", type=str, default="plainfish")

    result = parser.parse_args(args)
    return result
