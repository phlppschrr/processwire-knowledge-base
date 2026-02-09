# $pagesPathFinder->segmentLanguage($segment, $getLanguageId = false): Language|null|int

Source: `wire/core/PagesPathFinder.php`

Return language identified by homepage name segment

## Usage

~~~~~
// basic usage
$language = $pagesPathFinder->segmentLanguage($segment);

// usage with all arguments
$language = $pagesPathFinder->segmentLanguage($segment, $getLanguageId = false);
~~~~~

## Arguments

- `$segment` `string`
- `$getLanguageId` (optional) `bool`

## Return value

- `Language|null|int`
