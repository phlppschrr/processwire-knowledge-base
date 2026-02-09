# $listerBookmarks->filterBookmarksByAccess(array $bookmarks): array

Source: `wire/modules/Process/ProcessPageLister/ListerBookmarks.php`

Filter bookmarks, removing those user does not have access to

## Usage

~~~~~
// basic usage
$array = $listerBookmarks->filterBookmarksByAccess($bookmarks);

// usage with all arguments
$array = $listerBookmarks->filterBookmarksByAccess(array $bookmarks);
~~~~~

## Arguments

- `$bookmarks` `array`

## Return value

- `array`
