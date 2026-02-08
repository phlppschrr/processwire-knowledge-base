# WireRandom::arrayItem()

Source: `wire/core/WireRandom.php`

Get a random item (or items, key or keys) from the given array

- Given array may be regular or associative.

- If given a `qty` other than 1 (default) then the `getArray` option is assumed true, unless a
  different value for the `getArray` option was manually specified.

- When using the `getArray` option, returned array will have keys retained, except when `qty`
  option exceeds the number of items in given array `$a`, then keys will not be retained.

@param array $a Array to get random item from

@param array $options Options to modify behavior:
 - `qty` (int): Return this quantity of item(s) (default=1).
 - `getKey` (bool): Return item key(s) rather than values.
 - `getArray` (bool): Return array (with original keys) rather than value (default=false if qty==1, true if not).

@return mixed|array|null
