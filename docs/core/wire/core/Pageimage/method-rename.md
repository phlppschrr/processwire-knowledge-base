# Pageimage::rename()

Source: `wire/core/Pageimage.php`

Rename this file

Remember to follow this up with a `$page->save()` for the page that the file lives on.


@param string $basename New name to use. Must be just the file basename (no path).

@return string|bool Returns new name (basename) on success, or boolean false if rename failed.
