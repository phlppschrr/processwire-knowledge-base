# $permissions->saved(Page $page, array $changes = array(), $values = array())

Source: `wire/core/Permissions.php`

Hook called when a permission is saved

## Usage

~~~~~
// basic usage
$result = $permissions->saved($page);

// usage with all arguments
$result = $permissions->saved(Page $page, array $changes = array(), $values = array());
~~~~~

## Hookable

- Hookable method name: `saved`
- Implementation: `___saved`
- Hook with: `$permissions->saved()`

## Arguments

- `$page` `Page` Page that was saved
- `$changes` (optional) `array` Array of changed field names
- `$values` (optional) `array` Array of changed field values indexed by name (when enabled)

## Exceptions

- `WireException`
