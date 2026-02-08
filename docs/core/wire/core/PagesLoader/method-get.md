# PagesLoader::get()

Source: `wire/core/PagesLoader.php`

Returns the first page matching the given selector with no exclusions


@param string|int|array|Selectors $selector

@param array $options See Pages::find method for options

@return Page|NullPage Always returns a Page object, but will return NullPage (with id=0) when no match found
