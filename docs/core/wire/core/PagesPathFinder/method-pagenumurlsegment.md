# $pagesPathFinder->pageNumUrlSegment($pageNum, $langName = 'default'): string

Source: `wire/core/PagesPathFinder.php`

Get page number segment with given pageNum and and in given language name

## Usage

~~~~~
// basic usage
$string = $pagesPathFinder->pageNumUrlSegment($pageNum);

// usage with all arguments
$string = $pagesPathFinder->pageNumUrlSegment($pageNum, $langName = 'default');
~~~~~

## Arguments

- `$pageNum` `int`
- `$langName` (optional) `string`

## Return value

- `string`
