# $functionsAPI->fields($name = ''): Fields|Field|null

Source: `wire/core/FunctionsAPI.php`

Get or save fields independent of templates ($fields API variable as as function)

This function behaves the same as the `$fields` API variable, though does support
an optional shortcut argument for getting a single field.

~~~~~
$field = fields()->get('title'); // regular syntax
$field = fields('title'); // shortcut syntax
~~~~~

## Arguments

- string $name Optional field name to retrieve

## Return value

Fields|Field|null

## See also

- Fields
