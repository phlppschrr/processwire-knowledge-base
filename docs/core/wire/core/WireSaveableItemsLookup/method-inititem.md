# $wireSaveableItemsLookup->initItem(array &$row, ?WireArray $items = null): Saveable|HasLookupItems|WireData|Wire

Source: `wire/core/WireSaveableItemsLookup.php`

Create a new Saveable/Lookup item from a raw array ($row) and add it to $items

## Usage

~~~~~
// basic usage
$saveable = $wireSaveableItemsLookup->initItem($row);

// usage with all arguments
$saveable = $wireSaveableItemsLookup->initItem(array &$row, ?WireArray $items = null);
~~~~~

## Arguments

- `$row` `array`
- `$items` (optional) `WireArray|null`

## Return value

- `Saveable|HasLookupItems|WireData|Wire`

## Since

3.0.194
