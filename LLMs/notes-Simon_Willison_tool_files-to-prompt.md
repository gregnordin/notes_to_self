# Purpose

Use Simon Willison's [files-to-prompt](https://github.com/simonw/files-to-prompt) tool to create a single file suitable for LLM ingestion from a directory of files and including subdirectories of files.

# Install tool

```bash
pipx install files-to-prompt
    installed package files-to-prompt 0.6, installed using Python 3.13.1
    These apps are now globally available
      - files-to-prompt
  done! ✨ 🌟 ✨
which files-to-prompt
	/Users/nordin/.local/bin/files-to-prompt
```

# Use tool

```bash
# Output to a text file
files-to-prompt <directory> -o <output file name.txt> --ignore "__pycache__"

# Output in Claude XML format.
files-to-prompt <directory> --cxml -o <output file name.xml> --ignore "__pycache__"

# Output in markdown format.
files-to-prompt <directory> --markdown -o <output file name.md> --ignore "__pycache__"
```

Example:

```bash
files-to-prompt pymfd/ -o temp.txt --ignore "__pycache__"
```



