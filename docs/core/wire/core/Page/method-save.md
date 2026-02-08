# Page::save()

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


@param Field|string $field Optional field to save (name of field or Field object)

@param array $options See Pages::save() documentation for options. You may also specify $options as the first argument if no $field is needed.

@return bool Returns true on success false on fail

@throws WireException on database error

@see Pages::save(), Page::saveFields(), Pages::saveField(), Pages::saveReady(), Pages::saveFieldReady(), Pages::saved(), Pages::fieldSaved()
