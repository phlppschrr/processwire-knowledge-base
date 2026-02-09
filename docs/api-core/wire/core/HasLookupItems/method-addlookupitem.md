# $hasLookupItems->addLookupItem($item, array &$row)

Source: `wire/core/Interfaces.php`

Add a lookup item to this instance

## Usage

~~~~~
// basic usage
$result = $hasLookupItems->addLookupItem($item, $row);

// usage with all arguments
$result = $hasLookupItems->addLookupItem($item, array &$row);
~~~~~

## Arguments

- `$item` `int` The ID of the item to add
- `$row` `array` The row from which it was retrieved (in case you want to retrieve or modify other details)
