# $pagesLoader->findShortcut($selector, $options, $loadOptions): bool|Page|PageArray

Source: `wire/core/PagesLoader.php`

Helper for find() method to attempt to shortcut the find when possible

## Usage

~~~~~
// basic usage
$bool = $pagesLoader->findShortcut($selector, $options, $loadOptions);
~~~~~

## Arguments

- `$selector` `string|array|Selectors`
- `$options` `array`
- `$loadOptions` `array`

## Return value

- `bool|Page|PageArray` Returns boolean false when no shortcut available
