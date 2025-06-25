#!/usr/bin/env python3
"""Report the size of code vs model artifacts in the repository."""
from __future__ import annotations

import os
from pathlib import Path

CODE_EXT = {".py", ".pyi"}
MODEL_EXT = {".pt", ".onnx", ".bin", ".pkl"}


def accumulate_sizes(root: Path) -> tuple[int, int]:
    code = 0
    model = 0
    for path in root.rglob("*"):
        if path.is_file():
            if path.suffix in CODE_EXT:
                code += path.stat().st_size
            elif path.suffix in MODEL_EXT:
                model += path.stat().st_size
    return code, model


def main() -> None:
    code_size, model_size = accumulate_sizes(Path("."))
    print(f"code_bytes={code_size}")
    print(f"model_bytes={model_size}")
    ratio = model_size / code_size if code_size else 0
    print(f"model_to_code_ratio={ratio:.2f}")
    threshold = float(os.environ.get("MODEL_CODE_RATIO_MAX", "10"))
    if ratio > threshold:
        raise SystemExit(f"Model size ratio {ratio:.2f} exceeds {threshold}")


if __name__ == "__main__":
    main()
