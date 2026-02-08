# PagesNames::defaultPageNameFormat()

Source: `wire/core/PagesNames.php`

Get the name format string that should be used for given $page if no name was assigned


@param Page $page

@param array $options
 - `fallbackFormat` (string): Fallback format if another cannot be determined (default='untitled-time').
 - `parent` (Page|null): Optional parent page to use instead of $page->parent (default=null).

@return string
