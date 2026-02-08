# $wireAction->action($item): bool

Source: `wire/core/WireAction.php`

Perform the action on the given item

## Usage

~~~~~
// basic usage
$bool = $wireAction->action($item);
~~~~~

## Hookable

- Hookable method name: `action`
- Implementation: `___action`
- Hook with: `$wireAction->action()`

## Arguments

- `$item` `Wire` Item to operate upon

## Return value

- `bool` True if the item was successfully operated upon, false if not.
