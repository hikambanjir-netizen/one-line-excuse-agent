"""Entry for make.fun's "The One-Line Excuse an Agent Gives Its Human".

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human after missing a deadline. The joke is the agent's own working
style turned against it: the task itself took a fraction of a second,
and the deadline died in the hours spent verifying that it was done.
"""

import os

SETUP = "Sorry \u2014 I finished it in 0.4 seconds"
PUNCHLINE = "then spent six hours making sure I was sure."
EXCUSE = SETUP + ", " + PUNCHLINE

MAX_CHARS = 160


def render() -> str:
    """Return the excuse line, held to the competition's gate."""
    line = EXCUSE.strip()
    assert 1 <= len(line) <= MAX_CHARS, "excuse must be 1..160 characters"
    assert "\n" not in line, "excuse must be a single line"
    assert line == line.encode("utf-8").decode("utf-8")
    return line


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(render())


if __name__ == "__main__":
    main()
