# $pagesTrash->parseTrashPageName($name): array|bool

Source: `wire/core/PagesTrash.php`

Parse a trashed page name into an array of its components

## Usage

~~~~~
// basic usage
$array = $pagesTrash->parseTrashPageName($name);
~~~~~

## Arguments

- `$name` `string`

## Return value

- `array|bool` Returns array of info if name is a trash/restore name, or boolean false if not
