# Template::getTabLabel()

Source: `wire/core/Template.php`

Return page tab label for current language (or specified language if provided)


@param string $tab Which tab? 'content' or 'children'

@param Page|Language $language Optional, if not used then user's current language is used

@return string Returns blank if default tab label not overridden
