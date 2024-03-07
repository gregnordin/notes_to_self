# Information

## Website

[Datasette](https://datasette.io/) - a tool for exploring and publishing data. It helps people take data of any shape, analyze and explore it, and publish it as an interactive website and accompanying API.

## Videos

- [Introduction to Datasette and sqlite-utils](https://www.youtube.com/watch?v=7kDFBnXaw-c) by Simon Willison.
- [Datasette: a big bag of tricks for solving interesting problems using SQLite](https://www.youtube.com/watch?v=B55hcKYye_c) by Simon Willison.
- [Datasette - an ecosystem of tools for working with small data](https://www.youtube.com/watch?v=Lig2gxPEZPo) by Simon Willison.
- [Datasette is my data hammer](https://www.jeremiak.com/blog/datasette-the-data-hammer/).

# How-to

## Create database from CSV file

- Open Datasette app
- Menu: File &rarr; New Empty Database...
- At top left of new window, click on button `Import CSV`

# Log

## Tue, 3/5/24

### Install Datasette & plug-ins

[Basic Installation](https://docs.datasette.io/en/stable/installation.html#installation).

```bash
brew install datasette

which datasette
	/opt/homebrew/bin/datasette
datasette --version
	datasette, version 0.64.6
	
datasette install datasette-vega
datasette install datasette-cluster-map
datasette install csvs-to-sqlite
datasette install datasette-upload-csvs
datasette install datasette-search-all
datasette install datasette-bplist
```

### Install `sqlite-utils`

[sqlite-utils documentation](https://sqlite-utils.datasette.io/en/stable/).

```
brew install sqlite-utils
```

### Install `csvs-to-sqlite`

[csvs-to-sqlite](https://datasette.io/tools/csvs-to-sqlite) documentation.

```
pipx install csvs-to-sqlite
```

