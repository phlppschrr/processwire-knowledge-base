# PagesTrash::emptyTrashPass2()

Source: `wire/core/PagesTrash.php`

Secondary pass for trash deletion

This works by finding the children of the trash page and performing a recursive delete on them.

@param array $options Options passed to emptyTrash() method

@param array $result Verbose array, modified directly

@return int
