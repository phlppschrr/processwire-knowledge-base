# PagesNames::pageNameExists()

Source: `wire/core/PagesNames.php`

Is the given name is use by a page?

If the `multilang` option is used, it checks if the page name exists in any language.
IF the `language` option is used, it only checks that particular language (regardless of `multilang` option).


@param string $name

@param array $options
 - `page` (Page|int): Ignore this Page or page ID
 - `parent` (Page|int): Limit search to only this parent.
 - `multilang` (bool): Check other languages if multi-language page names supported? (default=false)
 - `language` (Language|int): Limit check to only this language (default=null)

@return int Returns quantity of pages using name, or 0 if name not in use.
