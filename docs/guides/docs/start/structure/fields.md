# ProcessWire fields and how they work (all custom fields)

Source: https://processwire.com/docs/start/structure/fields/

# Fields and field types in ProcessWire 

Fields in ProcessWire are where the content is actually stored. Any field may be one of many storing content for a Page and its output.
- [What are fields?](#what-are-fields)
- [Defining a field’s type (Fieldtype)](#defining-a-fields-type-fieldtype)
- [Collecting input for a field (Inputfield)](#collecting-input-for-a-field-inputfield)
- [Fieldtypes and Inputfields are plugin modules](#fieldtypes-and-inputfields-are-plugin-modules)

---
[](#)

### What are fields?

Fields store a single type of content. For instance, a base ProcessWire installation has a field named "title" that contains the Title of each Page. Thus there is one Title field per Page. Most ProcessWire installations also have a field called "body" which stores the multi-line Body Copy of a Page.

These fields are defined in ProcessWire, and every installation can have a different set of fields. The relevant fields are added to each template in whatever combination and order the site developer chooses. A given field can be added to one or more templates, so fields are reusable across templates.

When one goes to edit a Page, they see inputs only for the fields that are present on the Page's template. Fields can easily be added or removed from a template as needs change over time.[](#)

### Defining a field’s type (Fieldtype)

Every field has a type, which is referred to as the Fieldtype (1 word). This Fieldtype indicates the type of content that the field is storing. In many cases, the names of the simpler Fieldtypes line up with the names of the HTML inputs they loosely represent. For instance, a multi-line text field would be of type “Textarea”, while a single-line text field would have type of “Text”.[](#)

### Collecting input for a field (Inputfield)

Every field in ProcessWire is defined by its Fieldtype, but the Fieldtype doesn't handle the actual input for that field. This is handled instead by the Inputfield (1 word). An Inputfield actually renders the HTML needed to present an input to the user in a form, and then it handles the processing of that input when the form is submitted.

Most of the time, the Fieldtype defines what type of Inputfield it requires to collect input for it, so you don't often have to consider it. Though in some cases a Fieldtype will let you select the Inputfield. For instance, the Textarea Fieldtype will let you choose either a regular Textarea, or a Rich-Text Editor (i.e. CKEditor) for input.[](#)

### Fieldtypes and Inputfields are plugin modules

One thing that makes fields really flexible is that each Fieldtype and Inputfield is actually a type of plugin/module. The ProcessWire core comes with more than a dozen of them, which cover the most common needs. But any number of additional Fieldtype and/or Inputfield modules can be installed as modules, enabling you to store all kinds of different types of content. Many third party Fieldtype modules come with their own Inputfield modules and are installed together.

### Flexibility

Given that ProcessWire can have any number of pages, any number of custom content types (templates), any number of fields, and any number of field types and inputs, that makes it extremely flexible to handle just about any content management need.
- [Structure](/docs/start/structure/)
- [Pages](/docs/start/structure/pages/)
- [Templates](/docs/start/structure/templates/)
- [Fields](/docs/start/structure/fields/)
- [File system](/docs/start/structure/files/)

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

- [Getting started](/docs/start/)
- [Installation](/docs/start/install/)
- [Structure](/docs/start/structure/)
- [About the API](/docs/start/api/)
- [Template files](/docs/start/templates/)
- [API variables](/docs/start/variables/)
- [API access](/docs/start/api-access/)
- [Output strategies](/docs/front-end/output/)

[Templates](/docs/start/structure/templates/)
[File system](/docs/start/structure/files/)
