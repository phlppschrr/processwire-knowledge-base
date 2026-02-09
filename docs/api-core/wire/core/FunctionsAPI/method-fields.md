# $functionsAPI->fields($name = ''): Fields|Field|null

Source: `wire/core/FunctionsAPI.php`

Get or save fields independent of templates ($fields API variable as as function)

This function behaves the same as the `$fields` API variable, though does support
an optional shortcut argument for getting a single field.

## Example

~~~~~
$field = fields()->get('title'); // regular syntax
$field = fields('title'); // shortcut syntax
~~~~~

## Usage

~~~~~
// basic usage
$fields = $functionsAPI->fields();

// usage with all arguments
$fields = $functionsAPI->fields($name = '');
~~~~~

## Arguments

- `$name` (optional) `string` Optional field name to retrieve

## Return value

- `Fields|Field|null`

## See Also

- Fields
