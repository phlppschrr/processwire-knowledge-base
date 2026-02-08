# $wireArray->explode($property = '', array $options = array()): array

Source: `wire/core/WireArray.php`

Return a plain array of the requested property from each item

You may provide an array of properties as the $property, in which case it will return an
array of associative arrays with all requested properties for each item.

You may also provide a function as the $property. That function receives the $item
as the first argument and $key as the second. It should return the value that will be stored.

The keys of the returned array remain consistent with the original WireArray.

[Introduction of explode method](https://processwire.com/talk/topic/5098-new-wirearray-api-additions-on-dev/)

## Arguments

- string|callable|array $property Property or properties to retrieve, or callable function that should receive items.
- array $options Options to modify default behavior: - `getMethod` (string): Method to call on each item to retrieve $property (default = "get") - `key` (string|null): Property of Wire objects to use for key of array, or omit (null) for non-associative array (default).

## Return value

array

## See also

- [WireArray::each()](method-each.md)
- [WireArray::implode()](method-implode.md)
