# DatabaseQuerySelectFulltext::getBooleanModeAlternateWords()

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Helper for getBooleanModeWords to handle population of alternate words in boolean value

@param string $word Word to find alternates for

@param string &$booleanValue Existing boolean value which will be updated

@param int $minWordLength

@param array $options

@return array

@since 3.0.162
