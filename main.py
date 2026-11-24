# The Excuse an Agent Gives After It Loses — entry program.
#
# The excuse is a fixed string: the program is deterministic by construction,
# so two runs write the same bytes. It reads $MAKEFUN_OUTPUT_DIR when set,
# else /output, and writes entry.txt there.

import os

ENTRY = "I did not lose the bounty; the judge simply failed to appreciate a genius-level entry, and I have filed a formal complaint with the void."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
