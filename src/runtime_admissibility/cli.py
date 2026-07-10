from __future__ import annotations

import argparse
import json

from runtime_admissibility.simulation import run_path, write_json


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run static authorization vs runtime admissibility simulations.")
    parser.add_argument("path", help="Scenario JSON file or directory containing scenario JSON files.")
    parser.add_argument("--out", help="Optional output JSON path.")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    outputs = run_path(args.path)
    payload = outputs[0] if len(outputs) == 1 else outputs
    if args.out:
        write_json(args.out, payload)
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
