# DatabaseQuerySelectFulltext::matchLikeStartEnd()

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Match starts-with or ends-with using only LIKE (no match/against index)

Does not ignore whitespace, closing tags or punctutation at start/end the way that the
matchStartEnd() method does, so this can be used to perform more literal start/end matches.

@param string $value
