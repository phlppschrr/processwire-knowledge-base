# PagesType::___add()

Source: `wire/core/PagesType.php`

Adds a new page with the given $name and returns it

- If the page has any other fields, they will not be populated, only the name will.
- Returns a `NullPage` on error, such as when a page of this type already exists with the same name/parent.

Hook note:
If you want to hook this method, please hook the `addReady`, `Pages::add`, or `Pages::addReady` method
instead, as hooking this method will not hook relevant pages added directly through $pages->add().

@param string $name Name to use for the new page

@return Page|NullPage
