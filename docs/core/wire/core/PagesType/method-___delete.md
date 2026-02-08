# PagesType::___delete()

Source: `wire/core/PagesType.php`

Permanently delete a page and its fields.

Unlike `$pages->trash()`, pages deleted here are not restorable.

If you attempt to delete a page with children, and don’t specifically set the `$recursive` argument to `true`, then
this method will throw an exception. If a recursive delete fails for any reason, an exception will be thrown.

Hook note:
If you want to hook this method, please hook the `deleteReady`, `deleted`, or `Pages::delete` method
instead, as hooking this method will not hook relevant pages deleted directly through $pages->delete().

@param Page $page

@param bool $recursive If set to true, then this will attempt to delete all children too.

@return bool

@throws WireException
