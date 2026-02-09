# $template->getTabLabel($tab, $language = null): string

Source: `wire/core/Template.php`

Return page tab label for current language (or specified language if provided)

## Usage

~~~~~
// basic usage
$string = $template->getTabLabel($tab);

// usage with all arguments
$string = $template->getTabLabel($tab, $language = null);
~~~~~

## Arguments

- `$tab` `string` Which tab? 'content' or 'children'
- `$language` (optional) `Page|Language` Optional, if not used then user's current language is used

## Return value

- `string` Returns blank if default tab label not overridden
