# Multi-language field translation export/import

Source: https://processwire.com/blog/posts/language-field-export-import/

## Sections


## Multi-language field translation export/import

5 August 2022 by Ryan Cramer [ 0 Comments](/blog/posts/language-field-export-import/#comments)

In this post we cover the details of a new module that enables export and import capabilities for multi-language fields in ProcessWire.

Typically the way you translate page field values in ProcessWire is to edit a page, view the text in one language, and translate the text into another language, directly in the page editor.

This new *ProcessLanguageFieldExportImport* module provides an alternative to that process, moving the translation task out of the ProcessWire admin and enabling it to be completed with external tools. It does this by making the multi-language field values exportable and importable via JSON and/or CSV files. Translation tools can be as simple as a spreadsheet or something more dedicated that can work with the JSON translation files.

With this module installed, the translators do not need access to the ProcessWire admin environment in order to perform language translation. In addition, because a single translation file can cover any number of pages and fields, it also means that translation can likely be completed much more quickly than it could be in the admin environment.

*Note that this is for exporting/importing page field values, and not static translations of text in PHP files — those already have a built-in export and import function.*


### Acknowledgements

Special thanks to [Update AG](https://update.ch/) and Oliver Arnoczky for providing the support and direction that made this module possible.


### Export/import file formats

This module provides export and import of multi-language field translations in JSON or CSV format. Both files (downloadable and uploadable) and text (copy/paste) are supported for export or import.

The JSON format is useful for importing into external translation tools where the translations can be edited and then imported back into this module. The CSV format is useful if translating from within a spreadsheet.

The primary export/import format used by this module is functionally similar to the [XLIFF](https://en.wikipedia.org/wiki/XLIFF) format except that it is JSON rather than XML, and is applicable to the “web content” context, where each translation is for a specific page and field (or subfield).


### Supported multi-language field types

The most common multi-language Fieldtypes in ProcessWire are currently supported by this module:

- Text (and multi-language types derived from it)
- Textarea (both plain and rich text/markup)
- File/Image (description text only)
- Repeater
- FieldsetPage
- PageTable
- ProFields Repeater Matrix
- ProFields Table
- ProFields Textareas

Support for ProFields Combo (FieldtypeCombo) is also planned. Support for additional types are likely to be added in future versions.


### Standard usage


## Exporting text for translation

This section describes the settings available on the Export tab. Exporting is a 1-step process where you select what you want to export and then click the submit button. An export file (or copy/paste text) is immediately generated.


### Source language and target language

You select a source language and a target language. The source language is the language that the translator will be translating from and the target language is the language you are translating to. For instance, if translating from English to Spanish, the source language will be English and the target language will be spanish.


### Selecting fields to export

You can optionally select which fields you want to include in your export. If you do not select any fields then all supported fields are included in the export.


### Selecting pages to export

This module exports a set of pages matching a selector that you define (using the InputfieldSelector module). This is the same means of selection that you use for the "Filters" in ProcessWire's admin search engine (Lister).


### Export format

Either JSON or CSV export formats are supported. And you can choose whether you want to receive them in a file download or visible text that you can copy/paste. If performing a large export matching hundreds of thousands of pages, chances are that you'll want to use the file download. Whereas copy/paste text is more useful for getting familiar with the format and testing exports.


### Export options


## Importing translated text

Importing is a simple two-step process:


### Select pages to import by template

A list of all found page templates will be shown, enabling you to select which pages you want to import (by template). If you do not select any templates then it will import all pages in the import data.


### Import options

You can check one or more of these options to adjust how the import is performed:


## Translator guidelines

Exports use the UTF-8 character set and import files should maintain this character set.

When an item’s type is indicated as "markup" then HTML and entity encoding are allowed. Otherwise the translation (target) value should contain no markup or entity encoded characters.

Also when the type is "markup" the translator should maintain existing markup while translating the text within the markup.


## File format examples

Note that some values have been truncated for brevity in these examples.


### JSON format example

```
{
  "source_language": "default (English)",
  "target_language": "es (Español)",
  "version": 2,
  "exported": "2022-08-04 11:00:50",
  "items": [
    {
      "page": 3171,
      "field": "title",
      "type": "text",
      "source": "Mosel River Tour Through Time",
      "target": ""
    },
    {
      "page": 3171,
      "field": "browser_title",
      "type": "text",
      "source": "Mosel River Tour Through Time - Germany, France",
      "target": ""
    },
    {
      "page": 3185,
      "field": "title",
      "type": "text",
      "source": "What is a Bike & Barge Tour?",
      "target": "Que es un tour de Bici + barco?"
    },
    {
      "page": 3185,
      "field": "body",
      "type": "markup",
      "source": "<p><strong>It is about the boat…</strong></p>\n\n<p>Just the other day...</p>",
      "target": "<p><strong>Es acerca del barco…</strong></p>\n\n<p>Justo el otro día...</p>"
    },
    {
      "page": 3185,
      "field": "browser_title",
      "type": "text",
      "source": "What is a Bike & Barge Tour? - Travel Tips",
      "target": "Que es un tour en bici + barco? Tips para viajar"
    }
  ],
  "fields": {
    "title": "PageTitleLanguage",
    "body": "TextareaLanguage",
    "browser_title": "TextLanguage"
  }
}
```


### CSV format example

```
page,field,type,"default (English)","es (Español)"
3171,title,text,"Kevin Purdy: Mosel River Tour Through Time",""
3171,browser_title,text,"Mosel River Tour Through Time - Germany, France",""
3185,title,text,"What is a Bike & Barge Tour?","Que es un tour de Bici + barco?"
3185,body,markup,"<p>It is about the boat…</p>","<p>Es acerca del barco…</p>"
```


## Future

I'd like us to be able to also support the [XLIFF 2.0](https://en.wikipedia.org/wiki/XLIFF) format but need help from someone more familiar with this format. Specifically, how to we retain our required "page" and "field" properties in XLIFF, and how do we provide a value for XLIFF's "file" and "skeleton" fields?

Are there any other formats that would be worthwhile to support? I'd be interested in learning about them to see if we might be able to support them.

Support for Combo fields is likely to come next (if there is need/interest). Support for other multi-language field types is also likely to be added where there is interest.


## Download

This module is publicly available for download in the [modules directory](https://processwire.com/modules/process-language-field-export-import/) and on [GitHub](https://github.com/ryancramerdesign/ProcessLanguageFieldExportImport).

This module is also designed to work with several of the ProFields multi-language modules. VIP support is available in the [ProFields](https://processwire.com/talk/forum/28-profields-support/) or [ProDevTools](https://processwire.com/talk/forum/48-prodevtools-support/) support boards.
