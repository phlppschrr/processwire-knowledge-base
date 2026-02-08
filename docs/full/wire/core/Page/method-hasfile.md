# Page::hasFile()

Source: `wire/core/Page.php`

Does Page have given filename in its files directory?

@param string $file File basename or verbose hash

@param array $options
 - `getPathname` (bool): Get full path + filename when would otherwise return boolean true? (default=false)
 - `getPagefile` (bool): Get Pagefile object when would otherwise return boolean true? (default=false)

@return bool|string

@since 3.0.166
