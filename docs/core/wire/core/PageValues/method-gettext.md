# $pageValues->getText(Page $page, $key, $oneLine = false, $entities = null): string

Source: `wire/core/PageValues.php`

Same as getMarkup() except returned value is plain text

If no `$entities` argument is provided, returned value is entity encoded when output formatting
is on, and not entity encoded when output formatting is off.

## Arguments

- Page $page
- string $key Field name or string with field {name} tags in it.
- bool $oneLine Specify true if returned value must be on single line.
- bool|null $entities True to entity encode, false to not. Null for auto, which follows page's outputFormatting state.

## Return value

string

## See also

- [Page::getMarkup()](../Page/method-___getmarkup.md)
