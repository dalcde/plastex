# DEPRECATED

Use `https://github.com/dalcde/tex2html` instead.

# About
This is a fork of `https://github.com/plastex/plastex` incorporating some
changes from gerby-project and some of my own. This is intended to be
continually rebased above `plastex/plastex` `master`, hence will often get
force-pushed. The changelog for the patches applied can be found at
[https://github.com/dalcde/plastex-patches](https://github.com/dalcde/plastex-patches).
Please send all issues and pull requests there.

See [here](http://dec41.user.srcf.net/exp/global_analysis/index.html) for an
example output. Note that all the math is generated during the compilation
step, and the resulting html is javascript-free.

To turn a tex file into html, run
```console
 $ ./tex2html [source.tex] [target directory]
```
If `source.pdf` is present, it will be copied to the target directory as well.

The script `./compile_srcf` is a script I use on my webserver to compile
multiple tex files with some extra configuration. It may serve as a guide for
customization until I write better documentation.

# Install
Install the following python(3) dependencies: `PIL` (or `pillow`), `jinja2`,
`unidecode`, `pyduktape`. Then run the `tex2html` command in this directory.

Please submit a bug report if I am missing any dependencies; it is easy to miss
ones that are already installed in my system.

# plastex.sty
Included in this directory is a LaTeX package `plastex.sty`. This package has
some helper commands and environments:

## The `useimager` environment
Everything in the `useimager` environment will be compiled with LaTeX and then
rendered into SVG. This can be used for parts of the document that cannot be
handled by plastex (yet). The imager is already automatically used for
`tikzpicture`, hence this doesn't have to be wrapped in `useimager.

## \ifplastex
The package defines a new variable `\ifplastex`. This can be used as follows:
```latex
\ifplastex
  % commands to be run when processed by plastex
\else
  % commands to be run when processed by a usual tex engine
\fi
```
## \tph
A version of `\texorpdfstring` that now has three arguments, where the third
argument is what plastex should use.
