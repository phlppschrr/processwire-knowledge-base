# $functionsAPI->templates($name = ''): Templates|Template|null

Source: `wire/core/FunctionsAPI.php`

Get or save templates ($templates API variable as a function)

This function behaves the same as the `$templates` API variable, though does support
an optional shortcut argument for getting a single template.

## Example

~~~~~~
$t = templates()->get('basic-page'); // regular syntax
$t = templates('basic-page'); // shortcut syntax
~~~~~~

## Usage

~~~~~
// basic usage
$templates = $functionsAPI->templates();

// usage with all arguments
$templates = $functionsAPI->templates($name = '');
~~~~~

## Arguments

- `$name` (optional) `string` Optional template to retrieve

## Return value

- `Templates|Template|null`

## See Also

- Templates
