# $markupQA->getPagePathFromId($pageID, $language = null): string

Source: `wire/core/MarkupQA.php`

Given page ID return the path to it

## Usage

~~~~~
// basic usage
$string = $markupQA->getPagePathFromId($pageID);

// usage with all arguments
$string = $markupQA->getPagePathFromId($pageID, $language = null);
~~~~~

## Arguments

- `$pageID` `int`
- `$language` (optional) `Language|null`

## Return value

- `string`

## Since

3.0.231
