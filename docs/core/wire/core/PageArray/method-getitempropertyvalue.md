# $pageArray->getItemPropertyValue(Wire $item, $property): mixed

Source: `wire/core/PageArray.php`

Get the value of $property from $item

Used by the WireArray::sort method to retrieve a value from a Wire object.
If output formatting is on, we turn it off to ensure that the sorting
is performed without output formatting.

## Arguments

- `$item` `Wire`
- `$property` `string`

## Return value

mixed
