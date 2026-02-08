# $wireArray->getItemPropertyValue(Wire $item, $property): mixed

Source: `wire/core/WireArray.php`

Get the value of $property from $item

Used by the WireArray::sort method to retrieve a value from a Wire object.
Primarily here as a template method so that it can be overridden.
Lets it prepare the Wire for any states needed for sorting.

## Usage

~~~~~
// basic usage
$result = $wireArray->getItemPropertyValue($item, $property);

// usage with all arguments
$result = $wireArray->getItemPropertyValue(Wire $item, $property);
~~~~~

## Arguments

- `$item` `Wire`
- `$property` `string`

## Return value

- `mixed`
