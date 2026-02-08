# PagesNames::hasNumberSuffix()

Source: `wire/core/PagesNames.php`

Does the given name or Page have a number suffix? Returns the number if yes, or false if not


@param string|Page $name

@param bool $getNamePrefix Return the name prefix rather than the number suffix? (default=false)

@return int|bool|string Returns false if no number suffix, or int for number suffix or string for name prefix (if requested)
