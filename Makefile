PY?=python3.12
ELF?=build/output.elf
ELF2?=build/compare.elf
BIN?=build/output.bin

.PHONY: help lint test check elf-size elf-to-bin size-diff code-vs-model run-ingest

help:
@echo "Common targets:"
@echo "  lint          - run format and security checks"
@echo "  test          - run unit tests"
@echo "  check         - lint + test"
@echo "  elf-size      - show section sizes for $(ELF)"
@echo "  elf-to-bin    - convert $(ELF) to $(BIN)"
@echo "  size-diff     - diff $(ELF) and $(ELF2) using bloaty"
@echo "  code-vs-model - report repository code vs model size"
@echo "  run-ingest     - start FastAPI with memory-safe settings"

lint:
$(PY) -m black --check .
$(PY) -m isort --check .
$(PY) -m bandit -r core

test:
$(PY) -m pytest -q

check: lint test

elf-size:
arm-none-eabi-size $(ELF)

elf-to-bin:
arm-none-eabi-objcopy -O binary $(ELF) $(BIN)

size-diff:
bloaty $(ELF) $(ELF2)

code-vs-model:
$(PY) scripts/code_vs_model_split.py

run-ingest:
$(PY) -m uvicorn ingestion.adapters.main:app --reload --limit-max-requests 1000
