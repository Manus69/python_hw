import argparse

def _get_parser():
    parser = argpars=argparse.ArgumentParser()
    parser.add_argument("number", type=int, help="Number")
    parser.add_argument("text", type=str, help="String")

    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--repeat", type=int, default=1, help="Number of repeats")

    return parser

if __name__ == "__main__":
    parser = _get_parser()
    args = parser.parse_args()

    if args.verbose: print(f"Args : {args.number}, {args.verbose}, {args.repeat}")

    print(f"Number : {args.number}, String : {args.text * args.repeat}")