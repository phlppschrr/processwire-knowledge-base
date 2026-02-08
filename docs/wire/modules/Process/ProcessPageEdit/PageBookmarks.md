# PageBookmarks

Source: `wire/modules/Process/ProcessPageEdit/PageBookmarks.php`

Class PageBookmarks

Class for managing Page bookmarks, currently used by ProcessPageEdit and ProcessPageList

## __construct()

@param Process|ProcessPageEdit $process

## initNavJSON()

Initialize/create the $options array for executeNavJSON() in Process modules

@param array $options

@return array

## listBookmarks()

Render list of current bookmarks

@return string

## editBookmarksForm()

Provides the editor for bookmarks and returns InputfieldForm

@return InputfieldForm

@throws WirePermissionException|WireException

## editBookmarks()

Provides the editor or list for bookmarks and returns rendered markup

@return string

@throws WirePermissionException

## checkProcessPage()

Check and update the given process page for hidden/visible status depending on useBookmarks setting

@param Page $page

## addConfigInputfields()

Populate any configuration inputfields to the given $inputfields wrapper for $process

@param InputfieldWrapper $inputfields
