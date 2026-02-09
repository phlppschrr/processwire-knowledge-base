# $fields->makeItem(array $a = array()): Saveable|Wire

Source: `wire/core/Fields.php`

Make an item and populate with given data

## Usage

~~~~~
// basic usage
$saveable = $fields->makeItem();

// usage with all arguments
$saveable = $fields->makeItem(array $a = array());
~~~~~

## Arguments

- `$a` (optional) `array` Associative array of data to populate

## Return value

- `Saveable|Wire`

## Exceptions

- `WireException`

## Since

3.0.146
