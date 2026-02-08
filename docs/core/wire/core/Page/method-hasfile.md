# $page->hasFile($file, array $options = array()): bool|string

Source: `wire/core/Page.php`

Does Page have given filename in its files directory?

## Arguments

- string $file File basename or verbose hash
- array $options - `getPathname` (bool): Get full path + filename when would otherwise return boolean true? (default=false) - `getPagefile` (bool): Get Pagefile object when would otherwise return boolean true? (default=false)

## Return value

bool|string

## Meta

- @since 3.0.166
