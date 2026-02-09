# $processPageListerBookmarks->buildBookmarkDeleteForm($bookmarkID): InputfieldFieldset

Source: `wire/modules/Process/ProcessPageLister/ProcessPageListerBookmarks.php`

Build form for deleting a bookmark

## Usage

~~~~~
// basic usage
$inputfieldFieldset = $processPageListerBookmarks->buildBookmarkDeleteForm($bookmarkID);
~~~~~

## Arguments

- `$bookmarkID` `int` Bookmark ID

## Return value

- `InputfieldFieldset`

## Exceptions

- `WireException`
- `WirePermissionException`
