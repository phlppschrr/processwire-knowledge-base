# $listerBookmarks->getBookmark($bookmarkID, $type = null): array|null

Source: `wire/modules/Process/ProcessPageLister/ListerBookmarks.php`

Get a bookmark by ID (whether public or owned)

## Usage

~~~~~
// basic usage
$array = $listerBookmarks->getBookmark($bookmarkID);

// usage with all arguments
$array = $listerBookmarks->getBookmark($bookmarkID, $type = null);
~~~~~

## Arguments

- `$bookmarkID` `string|int`
- `$type` (optional) `int|null`

## Return value

- `array|null`
