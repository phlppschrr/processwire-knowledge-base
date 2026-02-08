# $wireSaveableItems->deleted(Saveable $item)

Source: `wire/core/WireSaveableItems.php`

Hook that runs right after an item has been deleted.

Unlike after(delete), it has already been confirmed that the item was indeed deleted.

## Usage

~~~~~
// basic usage
$result = $wireSaveableItems->deleted($item);

// usage with all arguments
$result = $wireSaveableItems->deleted(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `deleted`
- Implementation: `___deleted`
- Hook with: `$wireSaveableItems->deleted()`

## Arguments

- `$item` `Saveable`
