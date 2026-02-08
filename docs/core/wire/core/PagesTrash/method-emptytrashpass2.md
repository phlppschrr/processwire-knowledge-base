# $pagesTrash->emptyTrashPass2(array $options, &$result): int

Source: `wire/core/PagesTrash.php`

Secondary pass for trash deletion

This works by finding the children of the trash page and performing a recursive delete on them.

## Arguments

- array $options Options passed to emptyTrash() method
- array $result Verbose array, modified directly

## Return value

int
