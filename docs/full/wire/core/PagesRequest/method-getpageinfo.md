# PagesRequest::getPageInfo()

Source: `wire/core/PagesRequest.php`

Get array of page info (as provided by PagePathFinder)

See the PagesPathFinder::get() method return value for a description of
what this method returns.

If this method returns a blank array, it means that the getPage()
method has not yet been called or that it did not match a page.

@return array

@since 3.0.242
