# $pageValues->getText(Page $page, $key, $oneLine = false, $entities = null): string

Source: `wire/core/PageValues.php`

Same as getMarkup() except returned value is plain text

If no `$entities` argument is provided, returned value is entity encoded when output formatting
is on, and not entity encoded when output formatting is off.

## Usage

~~~~~
// basic usage
$string = $pageValues->getText($page, $key);

// usage with all arguments
$string = $pageValues->getText(Page $page, $key, $oneLine = false, $entities = null);
~~~~~

## Arguments

- `$page` `Page`
- `$key` `string` Field name or string with field {name} tags in it.
- `$oneLine` (optional) `bool` Specify true if returned value must be on single line.
- `$entities` (optional) `bool|null` True to entity encode, false to not. Null for auto, which follows page's outputFormatting state.

## Return value

- `string`

## See Also

- [Page::getMarkup()](../Page/method-___getmarkup.md)
