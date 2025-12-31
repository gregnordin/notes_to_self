import marimo

__generated_with = "0.18.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    from mohtml import div, p, tailwind_css
    tailwind_css()
    return div, p


@app.cell
def _(div, p):
    class ShowNiceHTML:
        def __init__(self, name):
            self.name = name

        def _display_(self):
            return div(
                p(self.name, klass="font-bold"),
                p("More text", klass="text-sm text-gray-400"),
                klass="bg-gray-200 p-2 rounded-xl"
            )

    ShowNiceHTML("Entered text")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
