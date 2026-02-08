# ProcessPageListerBookmarks

Source: `wire/modules/Process/ProcessPageLister/ProcessPageListerBookmarks.php`

Class ProcessPageListerBookmarks

Helper class for managing ProcessPageLister bookmarks

## __construct()

Construct

@param ProcessPageLister $lister

## bookmarks()

@return ListerBookmarks

## setPage()

Set the Lister page that bookmarks will be for

@param Page $page

## setUser()

Set user that bookmarks will be for

@param User $user

## buildBookmarkListForm()

Build the bookmarks tab and form contained within it

@return InputfieldForm

## buildBookmarkDeleteForm()

Build form for deleting a bookmark

@param int $bookmarkID Bookmark ID

@return InputfieldFieldset

@throws WireException

@throws WirePermissionException

## buildBookmarkEditForm()

Build the form needed to edit/add bookmarks

@param int $bookmarkID Specify bookmark ID if editing existing bookmark

@return InputfieldWrapper

## executeEditBookmark()

Implementation for editing a bookmark, URL segment: ./edit-bookmark/?n=bookmarkID

@return string

@throws WirePermissionException

## executeSaveBookmark()

Save a bookmark posted by ./edit-bookmark/

Performs redirect after saving
