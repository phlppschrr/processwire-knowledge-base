# $pageArray->getPage($key): Page|NullPage

Source: `wire/core/PageArray.php`

Like the base get() method but can only return Page objects (whether Page or NullPage)

## Arguments

- `$key` `int|string|array` Provide any of the following: - Key of Page to retrieve. - A selector string or selector array, to return the first item that matches the selector. - A string containing the "name" property of any Page, and the matching Page will be returned.

## Return value

Page|NullPage

## See also

- [WireArray::get()](../WireArray/method-get.md)

## Since

3.0.162
