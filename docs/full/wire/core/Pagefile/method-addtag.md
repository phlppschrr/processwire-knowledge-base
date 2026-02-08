# Pagefile::addTag()

Source: `wire/core/Pagefile.php`

Add the given tag to this file’s tags (if not already present)

~~~~~
$file = $page->files->first();
$file->addTag('foo'); // add single tag
$file->addTag('foo,bar,baz'); // add multiple tags
$file->addTag(['foo', 'bar', 'baz']); // same as above, using array
~~~~~


@param string|array $tag Tag to add, or array of tags to add, or CSV string of tags to add.

@return $this

@since 3.0.17

@see Pagefile::tags(), Pagefile::hasTag(), Pagefile::removeTag()
