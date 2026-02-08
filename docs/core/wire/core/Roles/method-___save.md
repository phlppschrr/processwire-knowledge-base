# $roles->save(Page $page): bool

Source: `wire/core/Roles.php`

Save a Role

## Usage

~~~~~
// basic usage
$bool = $roles->save($page);

// usage with all arguments
$bool = $roles->save(Page $page);
~~~~~

## Hookable

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `$roles->save()`

## Arguments

- `$page` `Role|Page`

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException`
