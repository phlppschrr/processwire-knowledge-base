# $wireArray->count(): int

Source: `wire/core/WireArray.php`

Returns the number of items in this WireArray.

Fulfills PHP's Countable interface, meaning it also enables this WireArray to be used with PHP's `count()` function.

## Example

~~~~~
// These two are the same
$qty = $items->count();
$qty = count($items);
~~~~~

## Usage

~~~~~
// basic usage
$int = $wireArray->count();
~~~~~

## Return value

- `int`
