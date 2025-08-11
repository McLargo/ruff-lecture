# Ruff lecture

Ruff is a linter and formatter for code written in Python. It is used in many
open source projects.

Develop in Rust, it is fast and efficient, compatibility with latest Python
versions. It offers the following features:

- fix common mistakes in Python code, like unused imports, unused/undefined
  variables, syntax errors and more.
- check code for style issues and formatting, like PEP 8 violations.
- can be installed via `pip` and other package managers like `poetry` and `uv`.
- supports `pyproject.toml` configuration.
- gather together features from other libraries, such as `flake8`, `isort`, and
  `black`.
- implements caches, to avoid re-analyzing unchanged files.
- implements automatic error correction.
- wide ranges of [rules](#rules).
- extension for
  [VSCode](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
  and other editors.

## Installation

To install Ruff, you can use `pip`:

```bash
pip install ruff
```

As mentioned, Ruff can also be installed using other package managers like
`poetry` or `uv` for your Python projects. Use `--dev` flag to install it as a
development dependency.

## Ruff linter

Ruff offers a [lint]((https://docs.astral.sh/ruff/linter/#the-ruff-linter)) to
match your python code according to a set of rules, such as flake8, isort,
pycodestyle and others.

```bash
ruff check --fix /path/to/code
```

- Fix flag is optional, only used to automatically fix issues found in the code.
- `/path/to/code` is optional, if not set, `.` is used as default.
- Arguments send in CLI command have highly priority than file configuration.

## Ruff formatter

Ruff provides a python code [formatter](https://docs.astral.sh/ruff/formatter/)
designed to replace Black.

```bash
ruff format /path/to/code
```

- `/path/to/code` is optional, if not set, `.` is used as default.

> NOTE: Don't use together with Black, as is exists small deviation in output.

## Rules

Ruff supports a huge set of rules that can be used to check your code. By default, there is a set of rules enabled, but you can customize it to fit your needs.

It is important to make your rules explicit to have full control. Try with a
small set of rules, and expand from there.

Whole list of rules can be found in the
[Ruff documentation](https://docs.astral.sh/ruff/rules/), but here are my own selection of rules (will see more details in the example sections):

- ERA: find commented-out code.
- ANN: flake8 annotations.
- S: bandit rules for secure code.
- FBT: detect boolean traps.
- B: flake8 builtins.
- COM: force use of trailing commas.
- C4: flake8 type comprehension.
- DTZ: detect datetime zone incoherence.
- FIX: detect fix, todo and other notes.
- ISC: encourage correct str concatenation.
- LOG: check issues with logging library.
- G: check issues with log format.
- PIE: flake8 misc.
- T20: check usage of print.
- PT: review pytest style.
- Q: encourage uses of double quotes.
- RET: flake8 returning values.
- SLF: private members access.
- SIM: help to make your code simple.
- TC: type checking only for hinting.
- ARG: review unused arguments.
- PTH: correct use of pathlib/os.
- FLY: encourage use of string format instead of join.
- I: isort module.
- N: ensures pep8 naming.
- E,W: pycodestyle.
- DOC: pydoclint supporting docstring styles like numpy, google and sphinx.
- D: check compliances of docstring convention.
- F: pyflakes rules.
- PL, PLC, PLE, PLR, PLW: pylint rules.
- FURB: modernize your python code.

Depending on your project, you can also enable other rules, such as:

- FAST: set of rules for fastapi projects.
- DJ: set of rules for django projects.
- NPY: set of rules for numpy projects.
- PD: set of rules for panda projects.

### Ignoring Errors

Any rule can be ignored in a file, or in a specific line, using comments.

- To ignore one line, add `# noqa: <rule identifier>` at the end of the line.
- To ignore a whole file, add `# ruff: noqa <rule identifier>` at the top of the
  file

Rule identifiers can be found in the Ruff documentation. If no identifier is
specified, all rules will be ignored.

To ensure your noqa directives are correct, there is a special rule, `RUF100`,
that detects unused suppression comments. You can add automatically the
corresponding `noqa` comment, use ruff command with `--add-noqa` flag.

### Format suppression

While formatting code, Ruff can exclude some pieces of code from being
formatted. This is useful when you want to keep a specific formatting style
or when you have code that should not be changed.

```python
fmt: off
...
fmt: on
```

## Configuration

WIP

## Other integrations

WIP

- [pre-commit hook](https://docs.astral.sh/ruff/tutorial/#integrations) and
- [GitHub Actions](https://github.com/astral-sh/ruff-action).

## References

- [Ruff documentation](https://docs.astral.sh/ruff/)
