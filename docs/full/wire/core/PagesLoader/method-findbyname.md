# $pagesLoader->findByName($name, array $options = array()): array|NullPage|Page|PageArray

Source: `wire/core/PagesLoader.php`

Find page(s) by name

This method is optimized just for finding pages by name and it does
not perform any filtering or access checking.

## Arguments

- string $name Match this page name
- array $options - `parent' (int|Page): Match this parent ID (default=0) - `parentName` (string): Match this parent name (default='') - `getArray` (bool): Get PHP info array rather than Page|NullPage|PageArray? (default=false) - `getOne` (bool|int): Get just one match of Page or NullPage? (default=false) When true, if multiple pages match then NullPage will be returned. To instead return the first match, specify int `1` instead of boolean true.

## Return value

array|NullPage|Page|PageArray
