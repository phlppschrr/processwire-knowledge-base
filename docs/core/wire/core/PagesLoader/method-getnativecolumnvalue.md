# PagesLoader::getNativeColumnValue()

Source: `wire/core/PagesLoader.php`

Get value of of a native column in pages table for given page ID


@param int|Page $id Page ID

@param string $column

@return int|string|bool Returns int/string value on success or boolean false if no matching row

@since 3.0.156

@throws \PDOException|WireException
