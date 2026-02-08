# $wireArray->eq($num): Wire|null

Source: `wire/core/WireArray.php`

Returns the item at the given index starting from 0, or NULL if it doesn't exist.

Unlike the `WireArray::index()` method, this returns an actual item and not another WireArray.

## Arguments

- int $num Return the n'th item in this WireArray. Specify a negative number to count from the end rather than the start.

## Return value

Wire|null

## See also

- [WireArray::index()](method-index.md)
