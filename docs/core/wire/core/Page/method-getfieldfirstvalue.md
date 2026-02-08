# $page->getFieldFirstValue($multiKey, $getKey = false): null|mixed

Source: `wire/core/Page.php`

Given a Multi Key, determine if there are multiple keys requested and return the first non-empty value

A Multi Key is a string with multiple field names split by pipes, i.e. headline|title

Example: browser_title|headline|title - Return the value of the first field that is non-empty

## Arguments

- `$multiKey` `string`
- `$getKey` (optional) `bool` Specify true to get the first matching key (name) rather than value

## Return value

null|mixed Returns null if no values match, or if there aren't multiple keys split by "|" chars

## Deprecated

Use $page->values()->getFieldFirstValue() instead
