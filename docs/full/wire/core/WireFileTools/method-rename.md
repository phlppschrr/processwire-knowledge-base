# WireFileTools::rename()

Source: `wire/core/WireFileTools.php`

Rename a file or directory and update permissions

Note that this method will fail if pathname given by $newName argument already exists.


@param string $oldName Old pathname, must be full disk path.

@param string $newName New pathname, must be full disk path OR can be basename to assume same path as $oldName.

@param array|bool|string $options Options array to modify behavior or substitute `limitPath` (bool or string) option here.
 - `limitPath` (bool|string|array): Limit renames to within this path, or boolean TRUE for site/assets, or FALSE to disable (default=false).
 - `throw` (bool): Throw WireException with verbose details on error? (default=false)
 - `chmod` (bool): Adjust permissions to be consistent with $config after rename? (default=true)
 - `copy` (bool): Use copy-then-delete method rather than a file system rename. (default=false) 3.0.178+
 - `retry` (bool): Retry with 'copy' method if regular rename files, applies only if copy option is false. (default=true) 3.0.178+
 - If given a bool or string for $options the `limitPath` option is assumed.

@return bool True on success, false on fail (or WireException if throw option specified).

@throws WireException If error occurs and $throw argument was true.

@since 3.0.118
