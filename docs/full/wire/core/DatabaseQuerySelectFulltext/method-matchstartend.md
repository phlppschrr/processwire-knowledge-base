# DatabaseQuerySelectFulltext::matchStartEnd()

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Match phrase at start or end of field value (also uses fulltext index when possible)

Ignores whitespace, punctuation and opening/closing tags, enabling it to match
start/end words or phrases surrounded by non-word characters.

@param $value
