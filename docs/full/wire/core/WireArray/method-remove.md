# $wireArray->remove($key): $this

Source: `wire/core/WireArray.php`

Removes the given item or index from the WireArray (if it exists).

## Usage

~~~~~
// basic usage
$result = $wireArray->remove($key);
~~~~~

## Arguments

- `$key` `int|string|Wire` Item to remove (object), or index of that item, or (3.0.196+) selector string.

## Return value

- `$this` This instance.
