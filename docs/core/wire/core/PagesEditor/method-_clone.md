# PagesEditor::_clone()

Source: `wire/core/PagesEditor.php`

Clone an entire page (including fields, file assets, and optionally children) and return it.


@param Page $page Page that you want to clone

@param Page|null $parent New parent, if different (default=same parent)

@param bool $recursive Clone the children too? (default=true)

@param array|string $options Optional options that can be passed to clone or save
	- `forceID` (int): force a specific ID
	- `set` (array): Array of properties to set to the clone (you can also do this later)
	- `recursionLevel` (int): recursion level, for internal use only.

@return Page|NullPage the newly cloned page or a NullPage() with id=0 if unsuccessful.

@throws WireException|\Exception on fatal error
