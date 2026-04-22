from __future__ import annotations

import argparse
import sys

from ensemble_rules import __version__, pipeline
from ensemble_rules.errors import PanelError


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="ensemble-rules",
        description="Poll a panel of LLMs for best-practices rules and synthesize the results.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run the elicit → synthesize pipeline for a topic.")
    run_parser.add_argument("topic", help="The topic to elicit rules about (e.g. 'shell scripts').")
    run_parser.add_argument(
        "--description",
        required=True,
        help="One-line context for the topic, passed to each model alongside the topic name.",
    )

    args = parser.parse_args(argv)

    if args.command == "run":
        try:
            run_dir = pipeline.run(args.topic, args.description)
        except PanelError as exc:
            print(f"panel failure: {exc}", file=sys.stderr)
            if exc.run_dir is not None:
                print(str(exc.run_dir))
            return 2
        print(str(run_dir))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
