# $templates->rename(Template $template, $name)

Source: `wire/core/Templates.php`

Rename given template (and its fieldgroup, and file, when possible)

Given template must have its previous 'name' still present, and new name provided in $name
argument to this method.

## Usage

~~~~~
// basic usage
$result = $templates->rename($template, $name);

// usage with all arguments
$result = $templates->rename(Template $template, $name);
~~~~~

## Arguments

- `$template` `Template`
- `$name` `string` New name to use

## Exceptions

- `WireException` if rename cannot be completed

## Since

3.0.170
