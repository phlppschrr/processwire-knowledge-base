# $pageimage->rename($basename): string|bool

Source: `wire/core/Pageimage.php`

Rename this file

Remember to follow this up with a `$page->save()` for the page that the file lives on.

## Usage

~~~~~
// basic usage
$string = $pageimage->rename($basename);
~~~~~

## Arguments

- `$basename` `string` New name to use. Must be just the file basename (no path).

## Return value

- `string|bool` Returns new name (basename) on success, or boolean false if rename failed.
