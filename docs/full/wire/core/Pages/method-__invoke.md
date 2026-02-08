# $pages->__invoke($key): Page|Pages|PageArray

Source: `wire/core/Pages.php`

Enables use of $pages(123), $pages('/path/') or $pages('selector string')

When given an integer or page path string, it calls $pages->get(key);
When given a string, it calls $pages->find($key);
When given an array, it calls $pages->getById($key);

## Arguments

- `$key` `string|int|array`

## Return value

Page|Pages|PageArray
