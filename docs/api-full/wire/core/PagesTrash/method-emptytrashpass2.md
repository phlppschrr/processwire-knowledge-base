# $pagesTrash->emptyTrashPass2(array $options, &$result): int

Source: `wire/core/PagesTrash.php`

Secondary pass for trash deletion

This works by finding the children of the trash page and performing a recursive delete on them.

## Usage

~~~~~
// basic usage
$int = $pagesTrash->emptyTrashPass2($options, $result);

// usage with all arguments
$int = $pagesTrash->emptyTrashPass2(array $options, &$result);
~~~~~

## Arguments

- `$options` `array` Options passed to emptyTrash() method
- `$result` `array` Verbose array, modified directly

## Return value

- `int`
