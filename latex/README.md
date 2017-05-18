
Helpful links

- [How to write multi-part definitions in LaTeX](https://www.johndcook.com/blog/2009/09/14/latex-multi-part-definitions/)
- [Tables in LaTeX](https://robjhyndman.com/hyndsight/tables-in-latex/)
    - Especially check out the `tabularx` package. Note `\toprule`, `\midrule`, and `\bottomrule`:
        
        \begin{tabularx}{\linewidth}%            {l>{\setlength\hsize{0.67\hsize}}X%
              >{\setlength\hsize{1.33\hsize}}X}
        \toprule
        \Large Label & \Large Text
            & \Large More text\tabularnewline
        \midrule
        One & This is some text without meaning.
            & This is {\huge another} text without meaning,
              just using up some space.\\
        \bottomrule
        \end{tabularx}
        
