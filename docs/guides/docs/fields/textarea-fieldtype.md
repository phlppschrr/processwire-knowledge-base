# Textarea (FieldtypeTextarea) multi-line text

Source: https://processwire.com/docs/fields/textarea-fieldtype/

## Summary

The Textarea Fieldtype is designed to hold any amount of text. Typically Textarea is used for multi-line text values. It is also used for rich text (CKEditor) fields.

## Key Points

- The Textarea Fieldtype is designed to hold any amount of text. Typically Textarea is used for multi-line text values. It is also used for rich text (CKEditor) fields.
- Examples include plain text, HTML markup, lightweight markup languages (like Markdown or Textile) or really anything that you might want to store as text. For single-line text values, choose the Text Fieldtype instead.
- The Textarea Fieldtype is configured for the Details tab (Setup > Fields > [textarea field] > Details). Below is an outline of available configuration options:

## Sections


### Text Formatters

If you want to apply any automatic formatting to the field when it is prepared for output, select one or more text formatters here. If you select more than one, drag them into the order they should be applied. For textarea fields that won't contain HTML, we strongly recommend selecting the HTML Entity Encoder text formatter.


### Inputfield Type

The type of field that will be used to collect input (Textarea is the default). If you using a lightweight markup language or plain text, select "Textarea". For rich text editing, select CKEditor.


### Content Type

This tells ProcessWire the type of content that will be contained in this field. If using a rich text editor or using plain HTML, choose one of the "Markup/HTML" options. If using plain text or a lightweight markup language (like Markdown) choose "Unknown".


### Markup/HTML Options

These options are available for ProcessWire 3.x only.
