# $wireArray->getItemThatMatches($key, $value): Wire|null

Source: `wire/core/WireArray.php`

Return the first item in this WireArray having a property named $key with $value, or NULL if not found.

Used internally by get() and has() methods.

## Usage

~~~~~
// basic usage
$wire = $wireArray->getItemThatMatches($key, $value);
~~~~~

## Arguments

- `$key` `string` Property to match.
- `$value` `string|int|object` $value to match.

## Return value

- `Wire|null`
