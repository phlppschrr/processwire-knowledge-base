# WireDatabasePDO::pdoType()

Source: `wire/core/WireDatabasePDO.php`

Return correct PDO instance type (reader or writer) based on given statement

@param string|\PDOStatement $query

@param bool $getName Get name of PDO type rather than instance? (default=false)

@return \PDO|string
