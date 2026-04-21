"""CLI entry point for Brainstorm."""

import argparse


def main():
    parser = argparse.ArgumentParser(prog="brainstorm", description="Brainstorm AI Framework")
    sub = parser.add_subparsers(dest="command")

    init_p = sub.add_parser("init", help="Initialize a new project")
    init_p.add_argument("name", help="Project name")

    train_p = sub.add_parser("train", help="Run training")
    train_p.add_argument("--config", default="config.yaml")
    train_p.add_argument("--epochs", type=int, default=10)

    sub.add_parser("devices", help="List available devices")

    args = parser.parse_args()

    if args.command == "init":
        print(f"Initializing project: {args.name}")
    elif args.command == "devices":
        from brainstorm.compute import list_devices
        for d in list_devices():
            print(f"  {d}")
    elif args.command is None:
        parser.print_help()
    else:
        print(f"Command {args.command} not yet implemented.")


if __name__ == "__main__":
    main()
