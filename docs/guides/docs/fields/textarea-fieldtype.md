# Unknown

Source: https://processwire.com/docs/fields/textarea-fieldtype/

The Textarea Fieldtype is designed to hold any amount of text. Typically Textarea is used for multi-line text values. It is also used for rich text (CKEditor) fields.

Examples include plain text, HTML markup, lightweight markup languages (like Markdown or Textile) or really anything that you might want to store as text. For single-line text values, choose the Text Fieldtype instead.

The Textarea Fieldtype is configured for the Details tab (Setup > Fields > [textarea field] > Details). Below is an outline of available configuration options:

- [Text Formatters](#text-formatters)
- [Inputfield Type](#inputfield-type)
- [Content Type](#content-type)
- [Markup/HTML Options](#markup-html-options)

---

[#](#)

### Text Formatters

If you want to apply any automatic formatting to the field when it is prepared for output, select one or more text formatters here. If you select more than one, drag them into the order they should be applied. For textarea fields that won't contain HTML, we strongly recommend selecting the *HTML Entity Encoder* text formatter.

---

[#](#)

### Inputfield Type

The type of field that will be used to collect input (Textarea is the default). If you using a lightweight markup language or plain text, select "Textarea". For rich text editing, select CKEditor.

---

[#](#)

### Content Type

This tells ProcessWire the type of content that will be contained in this field. If using a rich text editor or using plain HTML, choose one of the "Markup/HTML" options. If using plain text or a lightweight markup language (like Markdown) choose "Unknown".

**Content Type: Unknown**

This option is intended for plain text or lightweight markup languages (like Markdown or Textile). If using plain text, we also recommend that you choose the HTML Entity Encoder for your "Text Formatters", as mentioned earlier on this page.

**Content Type: Markup/HTML**

This option adds checks to ensure that links and image references in your textarea value are not broken by changes in the site root URL. For instance, if your development server runs the site off a sub-directory, and the live server doesn't, this option update any links or image references in the markup at runtime with the correct site root URL.

**Content Type: Markup/HTML with image management**

This option is available for ProcessWire 2.x only. For ProcessWire 3.x, see [Markup/HTML options](#markup-html-options) for the equivalent. This option includes everything in the Markup/HTML option and adds the following:

- Populate blank alt attributes with file description - ensures changes to file description are reflected in img[alt] attribute.
- Automatically re-create image size variations that do not exist, when possible.
- Remove <img> tags that point to files that do not exist and cannot be re-created.
- Record missing image errors to "markup-qa-errors" log file (Setup > Logs > markup-qa-errors).

See also: [Quality assurance with images in textarea fields](/blog/posts/quality-assurance-for-images-in-rich-text-fields/)

---

[#](#)

### Markup/HTML Options

*These options are available for ProcessWire 3.x only. *

**Image Management**

Selecting this option provides the following quality assurance for `<img>` tags:

- Populate blank alt attributes with file description - ensures changes to file description are reflected in img[alt] attribute.
- Automatically re-create image size variations that do not exist, when possible.
- Remove <img> tags that point to files that do not exist and cannot be re-created.
- Record missing image errors to "markup-qa-errors" log file (Setup > Logs > markup-qa-errors).

**Link Abstraction**

Selecting this option enables ProcessWire to provide quality assurance for your internal links referenced by `<a>` tags. When selected, ProcessWire will manage the a[href] attributes, ensuring they always point to the right page. If a link points to a page which has moved, ProcessWire will update the href attribute automatically when the field is rendered, so that it points to the correct location. If a link points to a page which no longer exists (or is in the Trash) ProcessWire will record the error to the "markup-qa-errors" log file (Setup > Logs > markup-qa-errors).

*Note that the link management option works only for page fields saved after the option has been enabled. *

- [Fields, types, input](/docs/fields/)
- [Introduction to fields](/docs/start/structure/fields/)
- [Field dependencies](/docs/fields/dependencies/)
- [Repeaters](/docs/fields/repeaters/)
- [Textarea](/docs/fields/textarea-fieldtype/)
- [Select options](/docs/fields/select-options-fieldtype/)
- [Images](/docs/fields/images/)
- [Multi-language fields](/docs/multi-language-support/multi-language-fields/)
- [CKEditor](/docs/fields/ckeditor/)

- [Docs](/docs/)
- [API reference](/api/ref/)
- [Getting started](/docs/start/)
- [Front-end](/docs/front-end/)
- [Tutorials](/docs/tutorials/)
- [Selectors](/docs/selectors/)
- [Modules & hooks](/docs/modules/)
- [Fields, types, input](/docs/fields/)
- [Access control](/docs/user-access/)
- [Security](/docs/security/)
- [Multi-language](/docs/multi-language-support/)
- [More topics](/docs/more/)
