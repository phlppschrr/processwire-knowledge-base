# Pages::___clone()

Source: `wire/core/Pages.php`

Clone entire page and return it

This also clones any file assets assets associated with the page. The clone is recursive
by default, cloning children (and so on) as well. To clone only the page without children,
specify false for the `$recursive` argument.

Warning: this method can fail when recursive and cloning a page with huge amounts of
children (or descendent family), and adequate resources (like memory or time limit) are
not available.

~~~~~
// Clone the Westin Peachtree skyscraper page
$building = $pages->get('/skyscrapers/atlanta/westin-peachtree/');
$copy = $pages->clone($building);

// Bonus: Now that the clone exists, lets move and rename it
$copy->parent = '/skyscrapers/detroit/';
$copy->title = 'Renaissance Center';
$copy->name = 'renaissance-center';
$copy->save();
~~~~~


@param Page $page Page that you want to clone

@param Page|null $parent New parent, if different (default=null, which implies same parent)

@param bool $recursive Clone the children too? (default=true)

@param array|string $options Options that can be passed to modify default behavior of clone or save:
 - `forceID` (int): force a specific ID.
 - `set` (array): Array of properties to set to the clone (you can also do this later).
 - `recursionLevel` (int): recursion level, for internal use only.

@return Page|NullPage The newly cloned Page or a NullPage() with id=0 if unsuccessful.

@throws WireException|\Exception on fatal error
