# $wireSaveableItems->makeItem(array $a = array()): Saveable|WireData|Wire

Source: `wire/core/WireSaveableItems.php`

Make an item and populate with given data

## Usage

~~~~~
// basic usage
$saveable = $wireSaveableItems->makeItem();

// usage with all arguments
$saveable = $wireSaveableItems->makeItem(array $a = array());
~~~~~

## Arguments

- `$a` (optional) `array` Associative array of data to populate

## Return value

- `Saveable|WireData|Wire`

## Exceptions

- `WireException`

## Since

3.0.146
