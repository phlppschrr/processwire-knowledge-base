# $template->getTabLabel($tab, $language = null): string

Source: `wire/core/Template.php`

Return page tab label for current language (or specified language if provided)

## Arguments

- string $tab Which tab? 'content' or 'children'
- Page|Language $language Optional, if not used then user's current language is used

## Return value

string Returns blank if default tab label not overridden
