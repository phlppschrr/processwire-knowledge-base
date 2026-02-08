# WireDatabasePDO::renameColumns()

Source: `wire/core/WireDatabasePDO.php`

Rename table columns without changing type


@param string $table

@param array $columns Associative array with one or more of `[ 'old_name' => 'new_name' ]`

@return int Number of columns renamed

@since 3.0.185

@throws \PDOException
