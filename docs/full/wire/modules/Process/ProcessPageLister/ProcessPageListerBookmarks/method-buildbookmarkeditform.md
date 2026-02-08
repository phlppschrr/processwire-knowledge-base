# $processPageListerBookmarks->buildBookmarkEditForm($bookmarkID = 0): InputfieldWrapper

Source: `wire/modules/Process/ProcessPageLister/ProcessPageListerBookmarks.php`

Build the form needed to edit/add bookmarks

## Usage

~~~~~
// basic usage
$inputfieldWrapper = $processPageListerBookmarks->buildBookmarkEditForm();

// usage with all arguments
$inputfieldWrapper = $processPageListerBookmarks->buildBookmarkEditForm($bookmarkID = 0);
~~~~~

## Arguments

- `$bookmarkID` (optional) `int` Specify bookmark ID if editing existing bookmark

## Return value

- `InputfieldWrapper`
