## Monday 2017-02-06

I want to document my current thoughts about what tools to use for various tasks. Here they are:

- Notes
    - Record notes in Markdown. 
    - The problem is getting a real-time rendering of a markdown document. Solution: [MacDown](https://macdown.uranusjr.com)
- Journal papers
    - LaTeX, BibTeX
- Documents (proposals, etc.)
    - Microsoft Word (as little as possible), Endnote
    - LaTeX (as much as possible), BibTeX
- Editor
    - Atom
- Python coding
    - Use Anaconda, latest release (python 3.5 for now)
        - Usually install packages into root env, but occasionally make new envs for special purposes and to test new packages
    - Jupyter notebook for code development and code/narrative/documentation bundled together
    - Occasinally make my own packages for various projects
    - GUI code: PyQt & Qt4
- Drawings
    - png
        - Powerpoint
        - LaTex with Tikz
        - Inkscape
    - Webpages & markdown files
        - SVG
            - Raw, written directly in SVG
            - Inkscape
        - Image tag with png or jpeg files
    - Jupyter notebooks
        - SVG
        - png or jpeg files
- Graphing
    - Static 2D
        - Matplotlib in Jupyter notebooks, make png files as needed
    - Static 2D - webpage
        - png file
        - D3.js
    - Interactive 2D - webpage
        - D3.js looks promising, but must use javascript/html/css. See [Hua's example for measured absorber spectra](https://nanomicro.byu.edu:3456/maingroup/12839)
        - In principle, this can be integrated directly into markdown files (?)
    - Animated 2D - kind of have to do this in a browser
        - HTML 5 Canvas drawings
    - Animated 3D
        - three.js with WebGL - browser so anyone can see and use
        - Python with PyQt and Qt4 - but not easily accessible by others
- Web pages
    - Use bootstrap3 and plain vanilla javascript
    - Serve with either github pages or rawgit from a github respository
    - Or, convert Jupyter notebook to html
- Explore
    - Vega or vega-lite for static 2D graphs in browser, [Introduction to Vega-Lite](https://vega.github.io/vega-lite/tutorials/getting_started.html)
    - Sublime Text 3 as editor
    - Need to explore [transcrypt](http://www.transcrypt.org) to write code in python and have it transcribed into javascript so can be seen in a browser. Can use any javascript library, like D3.js and three.js.
    - [plotly](http://moderndata.plot.ly/15-python-and-r-charts-with-interactive-controls-buttons-dropdowns-and-sliders/) as an interactive 2D/3D plotting package (javascript/python/browser?)