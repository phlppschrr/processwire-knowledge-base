# $wireArray->isIdentical(WireArray $items, $strict = true): bool

Source: `wire/core/WireArray.php`

Is the given WireArray identical to this one?

## Arguments

- `$items` `WireArray`
- `$strict` (optional) `bool|int` Use strict mode? Optionally specify one of the following: `true` (boolean): Default. Compares items, item object instances, order, and any other data contained in WireArray. `false` (boolean): Compares only that items in the WireArray resolve to the same order and values (though not object instances).

## Return value

bool True if identical, false if not.
