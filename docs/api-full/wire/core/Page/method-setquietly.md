# $page->setQuietly($key, $value): $this

Source: `wire/core/Page.php`

Quietly set the value of a page property.

Set a value to a page without tracking changes and without exceptions.
Otherwise same as set().

## Usage

~~~~~
// basic usage
$result = $page->setQuietly($key, $value);
~~~~~

## Arguments

- `$key` `string`
- `$value` `mixed`

## Return value

- `$this`
