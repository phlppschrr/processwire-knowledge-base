# $templateFile->get($key): mixed

Source: `wire/core/TemplateFile.php`

Get a set property from the template file, typically to check if a template has access to a given variable

## Usage

~~~~~
// basic usage
$result = $templateFile->get($key);
~~~~~

## Arguments

- `$key` `string`

## Return value

- `mixed` Returns the value of the requested property, or NULL if it doesn't exist
