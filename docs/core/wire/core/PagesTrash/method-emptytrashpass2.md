# $pagesTrash->emptyTrashPass2(array $options, &$result): int

Source: `wire/core/PagesTrash.php`

Secondary pass for trash deletion

This works by finding the children of the trash page and performing a recursive delete on them.

## Arguments

- `$options` `array` Options passed to emptyTrash() method
- `$result` `array` Verbose array, modified directly

## Return value

int
