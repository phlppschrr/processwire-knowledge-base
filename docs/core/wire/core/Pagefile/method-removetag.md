# $pagefile->removeTag($tag): $this

Source: `wire/core/Pagefile.php`

Remove the given tag from this file’s tags (if present)

~~~~~
$file = $page->files->first();
$file->removeTag('foo'); // remove single tag
$file->removeTag('foo,bar,baz'); // remove multiple tags
$file->removeTag(['foo', 'bar', 'baz']); // same as above, using array
~~~~~

## Arguments

- string $tag Tag to remove, or array of tags to remove, or CSV string of tags to remove.

## Return value

$this

## See also

- [Pagefile::tags()](method-tags.md)
- [Pagefile::hasTag()](method-hastag.md)
- [Pagefile::addTag()](method-addtag.md)

## Meta

- @since 3.0.17
