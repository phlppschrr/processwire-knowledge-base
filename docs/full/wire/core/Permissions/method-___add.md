# $permissions->add($name): Permission|NullPage

Source: `wire/core/Permissions.php`

Add a new Permission with the given name and return it

## Usage

~~~~~
// basic usage
$permission = $permissions->add($name);
~~~~~

## Hookable

- Hookable method name: `add`
- Implementation: `___add`
- Hook with: `$permissions->add()`

## Arguments

- `$name` `string` Name of permission you want to add, i.e. "hello-world"

## Return value

- `Permission|NullPage` Returns a Permission page on success, or a NullPage on error
