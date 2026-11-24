"""Command-line interface for PassGuard."""

import argparse
import sys
from passguard.generator import generate_password
from passguard.analyzer import evaluate_strength
from passguard.exporter import export_analysis_json


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="passguard",
        description="PassGuard: Secure Password Generator & Security Analyzer",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # generate subcommand
    gen_parser = subparsers.add_parser("generate", help="Generate a secure password")
    gen_parser.add_argument(
        "-l", "--length", type=int, default=16, help="Password length (default: 16)"
    )
    gen_parser.add_argument(
        "--no-upper", action="store_true", help="Exclude uppercase letters"
    )
    gen_parser.add_argument(
        "--no-lower", action="store_true", help="Exclude lowercase letters"
    )
    gen_parser.add_argument(
        "--no-digits", action="store_true", help="Exclude numeric digits"
    )
    gen_parser.add_argument(
        "-s", "--symbols", action="store_true", help="Include special symbols"
    )
    gen_parser.add_argument(
        "--avoid-ambiguous",
        action="store_true",
        help="Avoid ambiguous characters (e.g. 1, l, I, 0, O)",
    )

    # analyze subcommand
    eval_parser = subparsers.add_parser(
        "analyze", help="Analyze password strength"
    )
    eval_parser.add_argument("password", type=str, help="Password string to analyze")
    eval_parser.add_argument(
        "--json", action="store_true", help="Output analysis in JSON format"
    )

    return parser


def main(args=None):
    parser = build_parser()
    parsed_args = parser.parse_args(args)

    if parsed_args.command == "generate":
        pwd = generate_password(
            length=parsed_args.length,
            use_upper=not parsed_args.no_upper,
            use_lower=not parsed_args.no_lower,
            use_digits=not parsed_args.no_digits,
            use_symbols=parsed_args.symbols,
            avoid_ambiguous=parsed_args.avoid_ambiguous,
        )
        print(f"Generated Password: {pwd}")
        analysis = evaluate_strength(pwd)
        print(f"Rating: {analysis['rating']} (Score: {analysis['score']})")
    elif parsed_args.command == "analyze":
        analysis = evaluate_strength(parsed_args.password)
        if parsed_args.json:
            print(export_analysis_json(analysis))
        else:
            print(f"Strength Analysis for: {parsed_args.password}")
            print(f"Rating: {analysis['rating']}")
            print(f"Score:  {analysis['score']}")
            print("Details:")
            for item in analysis["details"]:
                print(f"  - {item}")
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
