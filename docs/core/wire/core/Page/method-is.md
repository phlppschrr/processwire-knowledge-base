# $page->is($status): bool

Source: `wire/core/Page.php`

Does this page have the specified status number or template name?

See status flag constants at top of Page class.
You may also use status names: hidden, locked, unpublished, system, systemID

## Arguments

- `$status` `int|string|Selectors` Status number, status name, or Template name or selector string/object

## Return value

bool
