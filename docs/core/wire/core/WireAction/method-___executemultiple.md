# $wireAction->executeMultiple($items): int

Source: `wire/core/WireAction.php`

Execute the action for multiple items at once

## Usage

~~~~~
// basic usage
$int = $wireAction->executeMultiple($items);
~~~~~

## Hookable

- Hookable method name: `executeMultiple`
- Implementation: `___executeMultiple`
- Hook with: `$wireAction->executeMultiple()`

## Arguments

- `$items` `array|WireArray` Items to operate upon

## Return value

- `int` Returns quantity of items successfully operated upon

## Exceptions

- `WireException` when it receives an unexpected type for $items
