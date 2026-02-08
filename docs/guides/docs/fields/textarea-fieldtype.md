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

Content Type: Unknown

This option is intended for plain text or lightweight markup languages (like Markdown or Textile). If using plain text, we also recommend that you choose the HTML Entity Encoder for your "Text Formatters", as mentioned earlier on this page.

Content Type: Markup/HTML

This option adds checks to ensure that links and image references in your textarea value are not broken by changes in the site root URL. For instance, if your development server runs the site off a sub-directory, and the live server doesn't, this option update any links or image references in the markup at runtime with the correct site root URL.

Content Type: Markup/HTML with image management

This option is available for ProcessWire 2.x only. For ProcessWire 3.x, see Markup/HTML options for the equivalent. This option includes everything in the Markup/HTML option and adds the following:

See also: Quality assurance with images in textarea fields


### Markup/HTML Options

These options are available for ProcessWire 3.x only.

Image Management

Selecting this option provides the following quality assurance for <img> tags:

Link Abstraction

Selecting this option enables ProcessWire to provide quality assurance for your internal links referenced by <a> tags. When selected, ProcessWire will manage the a[href] attributes, ensuring they always point to the right page. If a link points to a page which has moved, ProcessWire will update the href attribute automatically when the field is rendered, so that it points to the correct location. If a link points to a page which no longer exists (or is in the Trash) ProcessWire will record the error to the "markup-qa-errors" log file (Setup > Logs > markup-qa-errors).
