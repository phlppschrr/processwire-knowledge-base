# $permissions->save(Page $page): bool

Source: `wire/core/Permissions.php`

Save a Permission

## Usage

~~~~~
// basic usage
$bool = $permissions->save($page);

// usage with all arguments
$bool = $permissions->save(Page $page);
~~~~~

## Hookable

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `$permissions->save()`

## Arguments

- `$page` `Permission|Page`

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException`
