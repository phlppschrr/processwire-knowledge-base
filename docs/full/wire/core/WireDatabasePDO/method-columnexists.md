# WireDatabasePDO::columnExists()

Source: `wire/core/WireDatabasePDO.php`

Does the given column exist in given table?

~~~~~
// Standard usage:
if($database->columnExists('pages', 'name')) {
  echo "The pages table has a 'name' column";
}

// You can also bundle table and column together:
if($database->columnExists('pages.name')) {
  echo "The pages table has a 'name' column";
}

$exists = $database->columnExists('pages', 'name', true);
if($exists) {
  // associative array with indexes: Name, Type, Null, Key, Default, Extra
  echo "The pages table has a 'name' column and here is verbose info: ";
  print_r($exists);
}
~~~~~


@param string $table Specify table name (or table and column name in format "table.column").

@param string $column Specify column name (or omit or blank string if already specified in $table argument).

@param bool $getInfo Return array of column info (with type info, etc.) rather than true when exists? (default=false)
  Note that the returned array is raw MySQL values from a SHOW COLUMNS command.

@return bool|array

@since 3.0.154

@throws WireDatabaseException
