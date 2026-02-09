# $fields->initItem(array &$row, ?WireArray $items = null): Saveable|WireData|Wire

Source: `wire/core/Fields.php`

Create a new Saveable item from a raw array ($row) and add it to $items

## Usage

~~~~~
// basic usage
$saveable = $fields->initItem($row);

// usage with all arguments
$saveable = $fields->initItem(array &$row, ?WireArray $items = null);
~~~~~

## Arguments

- `$row` `array`
- `$items` (optional) `WireArray|null`

## Return value

- `Saveable|WireData|Wire`

## Since

3.0.194
