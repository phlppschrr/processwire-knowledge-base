# Pagefiles::getTag()

Source: `wire/core/Pagefiles.php`

Return the first Pagefile that matches the given tag or NULL if no match

Given tag may be any of the following:

- `foo` (single tag): Will return the first Pagefile object having the specified tag.
- `foo|bar|baz` (multiple OR tags): Will return first Pagefile object having at least one of the tags listed.
- `foo,bar,baz` (multiple AND tags): Will return first Pagefile object having ALL of the tags listed (since 3.0.17).
- `['foo','bar','baz']` (multiple AND tags array): Same as above but can be specified as an array (since 3.0.17).

3.0.17 Added support for multiple AND tags and allow tag specified as an array.

@param string $tag

@return Pagefile|null

@see Pagefiles::findTag(), Pagefile::hasTag(), Pagefile::tags()
