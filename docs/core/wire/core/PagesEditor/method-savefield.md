# $pagesEditor->saveField(Page $page, $field, $options = array()): bool

Source: `wire/core/PagesEditor.php`

Save just a field from the given page

This is the method used by by the `$page->save($field)` method.

This function is public, but the preferred manner to call it is with `$page->save($field)`

## Arguments

- Page $page
- string|Field $field Field object or name (string)
- array|string $options Specify options: - `quiet` (bool): Specify true to bypass updating of modified_users_id and modified time (default=false). - `noHooks` (bool): Specify true to bypass calling of before/after save hooks (default=false).

## Return value

bool True on success

## Throws

- WireException

## See also

- [Page::save()](../Page/method-save.md)
