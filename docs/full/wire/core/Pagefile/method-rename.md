# $pagefile->rename($basename): string|bool

Source: `wire/core/Pagefile.php`

Rename this file

Remember to follow this up with a `$page->save()` for the page that the file lives on.

## Arguments

- string $basename New name to use. Must be just the file basename (no path).

## Return value

string|bool Returns new name (basename) on success, or boolean false if rename failed.
