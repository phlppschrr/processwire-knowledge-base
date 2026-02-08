# Using multi-language fields

Source: https://processwire.com/docs/fields/multi-language-fields/

## Summary

Here we look in detail at multi-language fields and language-alternate fields, as well as how to use them. Also includes a video overview and examples of how to use language fields to create full multi-language websites.

## Key Points

- Here we look in detail at multi-language fields and language-alternate fields, as well as how to use them. Also includes a video overview and examples of how to use language fields to create full multi-language websites.
- ProcessWire supports the use of multi-language fields and language-alternate fields. A multi-language field is a single field that supports multiple languages, and these are typically text-based fields. Language-alternate fields are separate fields where the value of one can substitute for another, when the user's language justifies it. Below is a short video that demonstrates the use of both.
- This is an old video, but all the concepts still apply in current versions of ProcessWire.

## Sections


## Getting started


### How to install

To use multi-language fields or language-alternate fields, you must first install the "Language Support - Fields" module, included with ProcessWire 2.2 or newer. To do this, click "install" for "Language Support - Fields" from the Modules menu.


### When and where to use language fields

Language fields (whether multi-language or language-alternate) enable your site's template files to deal with just one field name while the value is affected by the current user's language. In fact, your template files don't even need to know about languages. This makes it a relatively simple matter to support languages in existing sites.


## Multi-language fields

ProcessWire 2.2 includes 3 new fieldtypes that support multiple languages:


### Converting an existing field to multi-language

To convert an existing field to a multi-language field, it must be a Text, Textarea or PageTitle field. Edit the field settings in Setup > Fields > Your Field. Change the "Type" to be: TextLanguage, TextareaLanguage or PageTitleLanguage. Because this change involves adding new columns to the field's database table, it will ask you to confirm the schema change. While this is a safe process, any time something modifies existing database tables, it's a good idea to make sure you have a backup of your database. When ready, confirm the change, and your field will now support all languages installed in the system. Should you want to convert back, repeat the same process but choose the non multi-language fieldtype instead.


### Creating a new multi-language field

To create a new multi-language field, all you need to do is go to Setup > Fields > Add New. When it asks you to select a field type, choose either TextLanguage or TextareaLanguage.


## Language-alternate fields

Language-alternate fields allow for the value of one field to replace the value of another when the user's language is something other than the default. Unlike multi-language fields, language-alternate fields are actually separate fields that you create on your own. ProcessWire identifies them based on the name you give them. The name is a combination of an existing field in the system combined with the language name.


### Creating a language-alternate field

If you wanted a Dutch version of your "body" field, you would name your new field "body_dutch". Meaning, a language alternate field should be named with the original field name, followed by an underscore and the language name.
