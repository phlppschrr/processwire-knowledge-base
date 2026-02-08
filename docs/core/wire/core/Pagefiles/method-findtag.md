# $pagefiles->findTag($tag): Pagefiles

Source: `wire/core/Pagefiles.php`

Return all Pagefile objects that have the given tag(s).

Given tag may be any of the following:

- `foo` (single tag): Will return all Pagefile objects having the specified tag.
- `foo|bar|baz` (multiple OR tags): Will return Pagefile objects having at least one of the tags listed.
- `foo,bar,baz` (multiple AND tags): Will return Pagefile objects having ALL of the tags listed (since 3.0.17).
- `['foo','bar','baz']` (multiple AND tags array): Same as above but can be specified as an array (since 3.0.17).

3.0.17 Added support for multiple AND tags and allow tag specified as an array.

## Arguments

- string|array $tag

## Return value

Pagefiles New Pagefiles array with items that matched the given tag(s).

## See also

- [Pagefiles::getTag()](method-gettag.md)
- [Pagefile::hasTag()](../Pagefile/method-hastag.md)
- [Pagefile::tags()](../Pagefile/method-tags.md)
