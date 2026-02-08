# WireDatabasePDO::isOperator()

Source: `wire/core/WireDatabasePDO.php`

Is the given string a database comparison operator?


~~~~~
if($database->isOperator('>=')) {
  // given string is a valid database operator
} else {
  // not a valid database operator
}
~~~~~

@param string $str 1-2 character operator to test

@param bool|null|int $operatorType Specify a WireDatabasePDO::operatorType* constant (3.0.162+), or any one of the following (3.0.143+):
 - `NULL`: allow all operators (default value if not specified)
 - `FALSE`: allow only comparison operators
 - `TRUE`: allow only bitwise operators

@param bool $get Return the operator rather than true, when valid? (default=false) Added 3.0.162

@return bool True if valid, false if not
