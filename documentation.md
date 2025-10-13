# Project Documentation

## Overview

This repository demonstrates a simple Python "Hello, World" project with a flat package layout. It is designed to help new employees quickly understand the structure, usage, and workflows of the project.

### Key Files and Structure
- `helloworld.py`: Entry-point script to run the program.
- `helloworld/`: Package directory containing:
  - `main.py`: Main implementation of the hello world logic and CLI.
  - `__init__.py`: Loads the package version from `VERSION.txt`.
  - `VERSION.txt`: Stores the package version.
- `README.md`: Basic usage instructions and installation guide.
- `.github/workflows/documentation_updater.yml`: GitHub Actions workflow to automatically update documentation when pull requests are merged.

## How It Works
- Running `helloworld.py` or installing the package and running `helloworld_in_python` prints "Hello, world".
- The version is managed in `helloworld/VERSION.txt` and loaded at runtime.
- The CLI supports `--version` and `--help` flags.

## Development Workflow
1. **Clone the repository** and install dependencies (if any).
2. **Make changes** to code or documentation as needed.
3. **Commit and push** changes to a feature branch.
4. **Create a pull request** to merge changes into `main`.
5. **Merge the pull request** after review.
6. **Documentation Agent Workflow**: When a PR is merged into `main`, the GitHub Actions workflow `.github/workflows/documentation_updater.yml` automatically updates `documentation.md` with details of the merged PR.

## Automated Documentation Workflow
- The workflow triggers on closed pull requests targeting `main`.
- If the PR was merged, it checks out the repo, sets up a bot user, and appends PR details to `documentation.md`.
- This ensures a running log of changes and contributors for easy onboarding.

## Getting Started
- See `README.md` for installation and usage.
- Review `documentation.md` for a history of changes and merged PRs.
- Explore the code in `helloworld/` for implementation details.

## Contact
For questions, reach out to the repository owner or check the latest entries in `documentation.md` for recent contributors.
