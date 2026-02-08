# FunctionsWireAPI::wirePageId()

Source: `wire/core/FunctionsWireAPI.php`

Return id for given page or false if it’s not a page

Returns positive int (page id) for page that exists, 0 for NullPage,
or false if given $value is not a Page.

@param Page|mixed $value

@return int|false

@since 3.0.224
