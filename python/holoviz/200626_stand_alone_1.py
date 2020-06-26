import panel as pn


checkbox = pn.widgets.Checkbox(name='Checkbox', value=True)

@pn.depends(value=checkbox)
def checkbox_value(value):
    return f"Checkbox value: {value}"

app = pn.Column(checkbox, checkbox_value)

app.servable()
