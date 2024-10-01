import argparse


def main(filename: str, word: str):

    print(filename, word)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Example.")
    parser.add_argument(
        "-f",
        "--fl",
        dest="file",
        help="The filename.",
        required=True,
    )
    parser.add_argument(
        "-w",
        "--word",
        dest="word",
        help="The word.",
        required=True,
    )

    args = parser.parse_args()

    main(
        args.file,
        args.word,
    )
