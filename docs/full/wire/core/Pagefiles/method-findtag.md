# Pagefiles::findTag()

Source: `wire/core/Pagefiles.php`

Return all Pagefile objects that have the given tag(s).

Given tag may be any of the following:

- `foo` (single tag): Will return all Pagefile objects having the specified tag.
- `foo|bar|baz` (multiple OR tags): Will return Pagefile objects having at least one of the tags listed.
- `foo,bar,baz` (multiple AND tags): Will return Pagefile objects having ALL of the tags listed (since 3.0.17).
- `['foo','bar','baz']` (multiple AND tags array): Same as above but can be specified as an array (since 3.0.17).

3.0.17 Added support for multiple AND tags and allow tag specified as an array.

@param string|array $tag

@return Pagefiles New Pagefiles array with items that matched the given tag(s).

@see Pagefiles::getTag(), Pagefile::hasTag(), Pagefile::tags()
