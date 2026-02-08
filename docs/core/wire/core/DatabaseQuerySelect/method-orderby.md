# DatabaseQuerySelect::orderby()

Source: `wire/core/DatabaseQuerySelect.php`

Add an ORDER BY section to the query

@param string|array $value

@param bool $prepend Should the value be prepended onto the existing value? default is to append rather than prepend.
	Note that $prepend is applicable only when you pass this method a string. $prepend is ignored if you pass an array.

@return $this
