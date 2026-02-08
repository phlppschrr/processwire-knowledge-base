# $templates->get($key): Template|null|string

Source: `wire/core/Templates.php`

Get a template by name or ID

Given a template ID or name, return the matching template or NULL if not found.

## Usage

~~~~~
// basic usage
$template = $templates->get($key);
~~~~~

## Arguments

- `$key` `string|int` Template name or ID

## Return value

- `Template|null|string`
