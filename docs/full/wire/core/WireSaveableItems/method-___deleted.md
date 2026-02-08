# $wireSaveableItems->___deleted(Saveable $item)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right after an item has been deleted.

Unlike after(delete), it has already been confirmed that the item was indeed deleted.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->___deleted($item);

// usage with all arguments
$result = $wireSaveableItems->___deleted(Saveable $item);
~~~~~

## Arguments

- `$item` `Saveable`
