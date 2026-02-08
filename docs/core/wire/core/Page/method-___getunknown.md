# $page->___getUnknown($key): null|mixed

Source: `wire/core/Page.php`

Hookable method called when a request to a field was made that didn't match anything

Hooks that want to inject something here should hook after and modify the $event->return.

## Usage

~~~~~
// basic usage
$page->___getUnknown($key);
~~~~~

## Arguments

- `$key` `string` Name of property.

## Return value

- `null|mixed` Returns null if property not known, or a value if it is.
