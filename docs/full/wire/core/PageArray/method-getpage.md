# PageArray::getPage()

Source: `wire/core/PageArray.php`

Like the base get() method but can only return Page objects (whether Page or NullPage)

@param int|string|array $key Provide any of the following:
 - Key of Page to retrieve.
 - A selector string or selector array, to return the first item that matches the selector.
 - A string containing the "name" property of any Page, and the matching Page will be returned.

@return Page|NullPage

@since 3.0.162

@see WireArray::get()
