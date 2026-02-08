# $wireSaveableItems->___saved(Saveable $item, array $changes = array())

Source: `wire/core/WireSaveableItems.php`

Hook that runs right after an item has been saved.

Unlike after(save), when this runs, it has already been confirmed that the item has been saved (no need to error check).

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->___saved($item);

// usage with all arguments
$result = $wireSaveableItems->___saved(Saveable $item, array $changes = array());
~~~~~

## Arguments

- `$item` `Saveable`
- `$changes` (optional) `array`
