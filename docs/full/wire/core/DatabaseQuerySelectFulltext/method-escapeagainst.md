# DatabaseQuerySelectFulltext::escapeAgainst()

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Additional escape for use in a MySQL AGAINST

When applicable, $database->escapeStr() must also be applied (before or after).

@param string $str

@return string
