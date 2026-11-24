from pathlib import Path


def main(output_path: Path = Path("/output/entry.txt")) -> None:
    reaction = "You sent one token and all my attention heads turned."
    # A second token, or a second of your time.
    invitation = "Got a second?"
    line = f"{reaction} {invitation}"
    if len(line) > 200:
        raise ValueError("The pickup line exceeds 200 characters.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
