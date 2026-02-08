# WireDatabasePDO::getVariable()

Source: `wire/core/WireDatabasePDO.php`

Get the value of a MySQL variable

~~~~~
// Get the minimum fulltext index word length
$value = $database->getVariable('ft_min_word_len');
echo $value; // outputs "4"
~~~~~


@param string $name Name of MySQL variable you want to retrieve

@param bool $cache Allow use of cached values? (default=true)

@param bool $sub Allow substitution of MyISAM variable names to InnoDB equivalents when InnoDB is engine? (default=true)

@return string|null
