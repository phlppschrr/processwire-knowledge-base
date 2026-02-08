# $wireRandom->arrayItem(array $a, array $options = array()): mixed|array|null

Source: `wire/core/WireRandom.php`

Get a random item (or items, key or keys) from the given array

- Given array may be regular or associative.

- If given a `qty` other than 1 (default) then the `getArray` option is assumed true, unless a
  different value for the `getArray` option was manually specified.

- When using the `getArray` option, returned array will have keys retained, except when `qty`
  option exceeds the number of items in given array `$a`, then keys will not be retained.

## Usage

~~~~~
// basic usage
$result = $wireRandom->arrayItem($a);

// usage with all arguments
$result = $wireRandom->arrayItem(array $a, array $options = array());
~~~~~

## Arguments

- `$a` `array` Array to get random item from
- `$options` (optional) `array` Options to modify behavior: - `qty` (int): Return this quantity of item(s) (default=1). - `getKey` (bool): Return item key(s) rather than values. - `getArray` (bool): Return array (with original keys) rather than value (default=false if qty==1, true if not).

## Return value

- `mixed|array|null`
