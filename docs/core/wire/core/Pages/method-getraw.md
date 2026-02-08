# $pages->getRaw($selector, $field = '', $options = array()): array

Source: `wire/core/Pages.php`

Get single page and return raw data in an associative array

Note that the data returned from this method is raw and unformatted, directly as it exists in the database.
In most cases you should use `$pages->get()` instead, but this method is a convenient alternative for some cases.

Please see the documentation for the `$pages->findRaw()` method, which all applies to this method as well.
The biggest difference is that this method returns data for just 1 page, unlike `$pages->findRaw()` which can
return data for many pages at once.

## Arguments

- string|array|Selectors|int $selector Page matching selector or page ID
- string|array|Field $field Name of field/property to get, or array of them, or omit to get all (default='')
- array $options

## Return value

array
