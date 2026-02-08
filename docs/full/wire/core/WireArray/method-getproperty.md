# $wireArray->getProperty($property): Wire|mixed

Source: `wire/core/WireArray.php`

Get a predefined property of the array, or extra data that has been set.

Default properties include;

- `count` (int): Number of items present in this WireArray.
- `last` (mixed): Last item in this WireArray.
- `first` (mixed): First item in this WireArray.
- `keys` (array): Keys used in this WireArray.
- `values` (array): Values present in this WireArray.

These can also be accessed by direct reference.

## Example

~~~~~
// Get count
$count = $items->getProperty('count');

// Same as above using direct access property
$count = $items->count;
~~~~~

## Usage

~~~~~
// basic usage
$wire = $wireArray->getProperty($property);
~~~~~

## Arguments

- `$property` `string` Name of property to retrieve

## Return value

- `Wire|mixed`
