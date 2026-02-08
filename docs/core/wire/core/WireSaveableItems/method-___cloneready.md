# $wireSaveableItems->___cloneReady(Saveable $item, Saveable $copy)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right before item is to be cloned.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->___cloneReady($item, $copy);

// usage with all arguments
$result = $wireSaveableItems->___cloneReady(Saveable $item, Saveable $copy);
~~~~~

## Arguments

- `$item` `Saveable`
- `$copy` `Saveable`
