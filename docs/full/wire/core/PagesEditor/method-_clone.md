# $pagesEditor->_clone(Page $page, ?Page $parent = null, $recursive = true, $options = array()): Page|NullPage

Source: `wire/core/PagesEditor.php`

Clone an entire page (including fields, file assets, and optionally children) and return it.

## Arguments

- `$page` `Page` Page that you want to clone
- `$parent` (optional) `Page|null` New parent, if different (default=same parent)
- `$recursive` (optional) `bool` Clone the children too? (default=true)
- `$options` (optional) `array|string` Optional options that can be passed to clone or save - `forceID` (int): force a specific ID - `set` (array): Array of properties to set to the clone (you can also do this later) - `recursionLevel` (int): recursion level, for internal use only.

## Return value

Page|NullPage the newly cloned page or a NullPage() with id=0 if unsuccessful.

## Throws

- WireException|\Exception on fatal error
