
# Mon, 12/23/19

### Information

- [GraphViz Gallery](https://www.graphviz.org/gallery/)
- [GraphViz Online](https://dreampuf.github.io/GraphvizOnline/#digraph%20G%20%7B%0A%0A%20%20subgraph%20cluster_0%20%7B%0A%20%20%20%20style%3Dfilled%3B%0A%20%20%20%20color%3Dlightgrey%3B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%2Ccolor%3Dwhite%5D%3B%0A%20%20%20%20a0%20-%3E%20a1%20-%3E%20a2%20-%3E%20a3%3B%0A%20%20%20%20label%20%3D%20%22process%20%231%22%3B%0A%20%20%7D%0A%0A%20%20subgraph%20cluster_1%20%7B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%5D%3B%0A%20%20%20%20b0%20-%3E%20b1%20-%3E%20b2%20-%3E%20b3%3B%0A%20%20%20%20label%20%3D%20%22process%20%232%22%3B%0A%20%20%20%20color%3Dblue%0A%20%20%7D%0A%20%20start%20-%3E%20a0%3B%0A%20%20start%20-%3E%20b0%3B%0A%20%20a1%20-%3E%20b3%3B%0A%20%20b2%20-%3E%20a3%3B%0A%20%20a3%20-%3E%20a0%3B%0A%20%20a3%20-%3E%20end%3B%0A%20%20b3%20-%3E%20end%3B%0A%0A%20%20start%20%5Bshape%3DMdiamond%5D%3B%0A%20%20end%20%5Bshape%3DMsquare%5D%3B%0A%7D)


# 11/24/18

See `2018_Projects/181124_try_GraphViz`.

Install

    $ brew install graphviz
    ==> Installing dependencies for graphviz: libtiff and webp
    ==> Installing graphviz dependency: libtiff
    ==> Downloading https://homebrew.bintray.com/bottles/libtiff-4.0.9_5.high_sierra.bottle.tar.gz
    ######################################################################## 100.0%
    ==> Pouring libtiff-4.0.9_5.high_sierra.bottle.tar.gz
    🍺  /usr/local/Cellar/libtiff/4.0.9_5: 246 files, 3.5MB
    ==> Installing graphviz dependency: webp
    ==> Downloading https://homebrew.bintray.com/bottles/webp-1.0.1.sierra.bottle.tar.gz
    ######################################################################## 100.0%
    ==> Pouring webp-1.0.1.sierra.bottle.tar.gz
    🍺  /usr/local/Cellar/webp/1.0.1: 39 files, 2MB
    ==> Installing graphviz
    ==> Downloading https://homebrew.bintray.com/bottles/graphviz-2.40.1.high_sierra.bottle.1.tar.gz
    ######################################################################## 100.0%
    ==> Pouring graphviz-2.40.1.high_sierra.bottle.1.tar.gz
    🍺  /usr/local/Cellar/graphviz/2.40.1: 500 files, 11.2MB
    
    $ which dot
    /usr/local/bin/dot
    $ dot -V
    dot - graphviz version 2.40.1 (20161225.0304)
    
From https://graphviz.gitlab.io/_pages/Gallery/directed/hello.html:

    $ echo "digraph G {Hello->World}" | dot -Tpng >hello.png
    
From http://graphs.grevian.org/example

    # Convert a gv file to png
    $ dot -Tpng rank.gv >rank.png
    
