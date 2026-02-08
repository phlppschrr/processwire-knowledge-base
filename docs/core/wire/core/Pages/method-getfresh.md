# Pages::getFresh()

Source: `wire/core/Pages.php`

Get a fresh, non-cached copy of a Page from the database

This method is the same as `$pages->get()` except that it skips over all memory caches when loading a Page.
Meaning, if the Page is already in memory, it doesn’t use the one in memory and instead reloads from the DB.
Nor does it place the Page it loads in any memory cache. Use this method to load a fresh copy of a page
that you might need to compare to an existing loaded copy, or to load a copy that won’t be seen or touched
by anything in ProcessWire other than your own code.

~~~~~
$p1 = $pages->get(1234);
$p2 = $pages->get($p1->path);
$p1 === $p2; // true: same Page instance

$p3 = $pages->getFresh($p1);
$p1 === $p3; // false: same Page but different instance
~~~~~


@param Page|string|array|Selectors|int $selectorOrPage Specify Page to get copy of, selector or ID

@param array $options Options to modify behavior

@return Page|NullPage

@since 3.0.172
