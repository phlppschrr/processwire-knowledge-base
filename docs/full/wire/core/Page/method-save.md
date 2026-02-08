# $page->save($field = null, array $options = array()): bool

Source: `wire/core/Page.php`

Save the entire page to the database, or just a field from it

This is the same as calling `$pages->save($page);` or `$pages->saveField($page, $field)`, but calling directly
on the $page like this may be more convenient in many instances.

If you want to hook into the save operation, hook into one of the many Pages class hooks referenced in the 'See Also' section.

~~~~~
// Save the page
$page->save();

// Save just the 'title' field from the page
$page->save('title');
~~~~~

## Arguments

- Field|string $field Optional field to save (name of field or Field object)
- array $options See Pages::save() documentation for options. You may also specify $options as the first argument if no $field is needed.

## Return value

bool Returns true on success false on fail

## Throws

- WireException on database error

## See also

- [Pages::save()](../Pages/method-___save.md)
- [Page::saveFields()](method-savefields.md)
- [Pages::saveField()](../Pages/method-___savefield.md)
- [Pages::saveReady()](../Pages/method-___saveready.md)
- [Pages::saveFieldReady()](../Pages/method-___savefieldready.md)
- [Pages::saved()](../Pages/method-___saved.md)
- [Pages::fieldSaved()](../Pages/index.md)
