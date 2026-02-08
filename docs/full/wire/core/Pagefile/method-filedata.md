# $pagefile->filedata($key = '', $value = null): Pagefile|Pageimage|array|string|int|float|bool|null

Source: `wire/core/Pagefile.php`

Get or set filedata

Filedata is any additional data that you want to store with the file’s database record.

- To get a value, specify just the $key argument. Null is returned if request value is not present.
- To get all values, omit all arguments. An associative array will be returned.
- To set a value, specify the $key and the $value to set.
- To set all values at once, specify an associative array for the $key argument.
- To unset, specify boolean false (or null) for $key, and the name of the property to unset as $value.
- To unset, you can also get all values, unset it from the retuned array, and set the array back.

## Arguments

- string|array|false|null $key Specify array to set all file data, or key (string) to set or get a property, Or specify boolean false to remove key specified by $value argument.
- null|string|array|int|float $value Specify a value to set for given property

## Return value

Pagefile|Pageimage|array|string|int|float|bool|null
