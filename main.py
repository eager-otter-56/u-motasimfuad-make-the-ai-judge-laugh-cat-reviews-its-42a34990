import os

ENTRY = (
    "1 star. Bowl showed its bottom at 6:04; refill limped in at 6:47. "
    "Sunny windowsill reserved for a plant. I sat on the warm keyboard and "
    "got evicted for sending the email he only thought."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
