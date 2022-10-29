
Nice preprint format: [LaPreprint](https://github.com/roaldarbol/LaPreprint). I had to comment out a lot of stuff to get it to work.

---

**Problem**: When try to use `\ul` to underline text, if there is a `\ref{}` in the text then LaTex will throw an error.  
**Solution**: Enclose `ref{}` in `{}` like this: `{\ref{}}`.  
**See**: [Problems with \ref when using soul for highlighting](https://tex.stackexchange.com/questions/23307/problems-with-ref-when-using-soul-for-highlighting).

**Problem**: When using the `soul` package, `\ul` results in an underline that is too garish for paragraphs of text.  
**Solution**: Instead, use `\hl` from the `soul` package, which puts the text on a yellow background.  
**See**: [Using colors in a LaTeX document](https://texblog.org/2015/05/20/using-colors-in-a-latex-document/), [Changing background color of text in Latex](https://tex.stackexchange.com/questions/136742/changing-background-color-of-text-in-latex)


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
        
