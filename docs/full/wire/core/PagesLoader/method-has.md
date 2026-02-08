# PagesLoader::has()

Source: `wire/core/PagesLoader.php`

Is there any page that matches the given $selector in the system? (with no exclusions)

- This can be used as an “exists” or “getID” type of method.
- Returns ID of first matching page if any exist, or 0 if none exist (returns array if `$verbose` is true).
- Like with the `get()` method, no pages are excluded, so an `include=all` is not necessary in selector.
- If you need to quickly check if something exists, this method is preferable to using a count() or get().

When `$verbose` option is used, an array is returned instead. Verbose return array includes all columns
from the matching row in the pages table.


@param string|int|array|Selectors $selector

@param bool $verbose Return verbose array with all pages columns rather than just page id? (default=false)

@param array $options Additional options to pass in find() $options argument (not currently applicable)

@return array|int

@since 3.0.153
