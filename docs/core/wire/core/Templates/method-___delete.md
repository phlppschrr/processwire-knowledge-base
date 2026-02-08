# $templates->delete(Saveable $item): bool

Source: `wire/core/Templates.php`

Delete a Template

## Usage

~~~~~
// basic usage
$bool = $templates->delete($item);

// usage with all arguments
$bool = $templates->delete(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `$templates->delete()`

## Arguments

- `$item` `Template|Saveable` Template to delete

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException` Thrown when you attempt to delete a template in use, or a system template.
