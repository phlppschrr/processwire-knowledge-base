# $listerBookmarks->getBookmarkUrl($bookmarkID, $user = null): string

Source: `wire/modules/Process/ProcessPageLister/ListerBookmarks.php`

Get the URL for a bookmark

## Usage

~~~~~
// basic usage
$string = $listerBookmarks->getBookmarkUrl($bookmarkID);

// usage with all arguments
$string = $listerBookmarks->getBookmarkUrl($bookmarkID, $user = null);
~~~~~

## Arguments

- `$bookmarkID` `string`
- `$user` (optional) `User|null`

## Return value

- `string`
