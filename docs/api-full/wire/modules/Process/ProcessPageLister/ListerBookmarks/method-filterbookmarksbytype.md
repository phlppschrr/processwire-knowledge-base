# $listerBookmarks->filterBookmarksByType(array $allBookmarks, $type): array

Source: `wire/modules/Process/ProcessPageLister/ListerBookmarks.php`

Filter bookmarks, removing those that are not of the requested type

## Usage

~~~~~
// basic usage
$array = $listerBookmarks->filterBookmarksByType($allBookmarks, $type);

// usage with all arguments
$array = $listerBookmarks->filterBookmarksByType(array $allBookmarks, $type);
~~~~~

## Arguments

- `$allBookmarks` `array`
- `$type` `int`

## Return value

- `array`
