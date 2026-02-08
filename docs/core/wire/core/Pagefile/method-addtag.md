# $pagefile->addTag($tag): $this

Source: `wire/core/Pagefile.php`

Add the given tag to this file’s tags (if not already present)

~~~~~
$file = $page->files->first();
$file->addTag('foo'); // add single tag
$file->addTag('foo,bar,baz'); // add multiple tags
$file->addTag(['foo', 'bar', 'baz']); // same as above, using array
~~~~~

## Arguments

- `$tag` `string|array` Tag to add, or array of tags to add, or CSV string of tags to add.

## Return value

$this

## See also

- [Pagefile::tags()](method-tags.md)
- [Pagefile::hasTag()](method-hastag.md)
- [Pagefile::removeTag()](method-removetag.md)

## Since

3.0.17
