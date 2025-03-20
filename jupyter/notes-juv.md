## Use ~~uv~~ uvx and juv to create/run Jupyter notebooks

Discover and install [juv](https://github.com/manzt/juv) - reproducible Jupyter notebooks, powered by uv.

`uv tool install juv`

### Updated use: `uvx`

Wed, 3/19/25:

```
uvx juv lab 2025-03-19_analyze_data.ipynb
```



### OLD

### Create notebook

```
juv init mixer_channel_calcs.ipynb
	Initialized notebook at `mixer_channel_calcs.ipynb`
juv init --python=3.13 mixer_channel_calcs.ipynb
	Initialized notebook at `mixer_channel_calcs.ipynb`
juv add mixer_channel_calcs.ipynb pint numpy matplotlib
	Updated `mixer_channel_calcs.ipynb`
juv stamp mixer_channel_calcs.ipynb
	Stamped `mixer_channel_calcs.ipynb` with 2025-03-06T17:27:40.225242-07:00
juv run mixer_channel_calcs.ipynb
```

### Lock file and tree dependencies

```
juv lock mixer_channel_calcs.ipynb
	Locked `mixer_channel_calcs.ipynb`
juv tree mixer_channel_calcs.ipynb
  pint v0.24.4
  ├── flexcache v0.3
  │   └── typing-extensions v4.12.2
  ├── flexparser v0.4
  │   └── typing-extensions v4.12.2
  ├── platformdirs v4.3.6
  └── typing-extensions v4.12.2
  numpy v2.2.3
  matplotlib v3.10.1
  ├── contourpy v1.3.1
  │   └── numpy v2.2.3
  ├── cycler v0.12.1
  ├── fonttools v4.56.0
  ├── kiwisolver v1.4.8
  ├── numpy v2.2.3
  ├── packaging v24.2
  ├── pillow v11.1.0
  ├── pyparsing v3.2.1
  └── python-dateutil v2.9.0.post0
      └── six v1.17.0
```







# OLD - Obsolete

## Use uv for jupyter lab venv

```
uv init mr1p1_paper
  Initialized project `mr1p1-paper` at `/Users/nordin/Documents/Projects/Papers/2025_MR1.1/calculations/mr1p1_paper`
cd mr1p1_paper/

uv add --dev jupyter pint numpy matplotlib ipykernel

uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=mr1p1_paper
  Installed kernelspec mr1p1_paper in /Users/nordin/Library/Jupyter/kernels/mr1p1_paper
uv run --with jupyter jupyter lab
```

Now select the `mr1p1_paper` kernel to start a notebook.



