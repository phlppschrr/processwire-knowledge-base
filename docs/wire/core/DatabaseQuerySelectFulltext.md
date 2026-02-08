# DatabaseQuerySelectFulltext

Source: `wire/core/DatabaseQuerySelectFulltext.php`

ProcessWire DatabaseQuerySelectFulltext

A wrapper for SELECT SQL queries using FULLTEXT indexes

Decorates a DatabaseQuerySelect object by providing the WHERE and
ORDER parts for a fulltext query based on the table, field, operator
and value you are searching.

Assumes that you are providing at least the SELECT and FROM portions
of the query.

The intention behind these classes is to have a query that can safely
be passed between methods and objects that add to it without knowledge
of what other methods/objects have done to it. It also means being able
to build a complex query without worrying about correct syntax placement.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## other

@property-read $tableField

## maxQueryValueLength

Max length that we allow for a query

## __construct()

Construct

@param DatabaseQuerySelect|PageFinderDatabaseQuerySelect $query

## __get()

@param string $name

@return mixed|string

## getQuery()

Get the query that was provided to the constructor

@return DatabaseQuerySelect

## tableField()

Get 'tableName.fieldName' string

@return string

## allowOrder()

Get or set whether or not 'ORDER BY' statements are allowed to be added

@param null|bool $allow Specify bool to set or omit to get

@return bool|null Returns bool when known or null when not yet known

@since 3.0.162

## allowStopwords()

Get or set whether fulltext searches can fallback to LIKE searches to match stopwords

@param null|bool $allow Specify bool to set or omit to get

@return bool

@since 3.0.162

## matchType()

@return string

## escapeLike()

Escape string for use in a MySQL LIKE

When applicable, $database->escapeStr() should be applied before this.

@param string $str

@return string

## escapeAgainst()

Additional escape for use in a MySQL AGAINST

When applicable, $database->escapeStr() must also be applied (before or after).

@param string $str

@return string

## value()

@param string $value

@return string

## match()

Update the query (provided to the constructor) to match the given arguments

@param string $tableName

@param string $fieldName

@param string $operator

@param string|int|array $value Value to match. Array value support added 3.0.141 (not used by PageFinder)

@return $this

@throws WireException If given $operator argument is not implemented here

## matchArrayFieldName()

Match when given $fieldName is an array

@param array $fieldNames

@param mixed $value

@since 3.0.169

## matchArrayValue()

Match when given $value is an array

Note: PageFinder uses its own array-to-value conversion, so this case applies only to other usages outside PageFinder,
such as FieldtypeMulti::getLoadQueryWhere()

@param array $value

@since 3.0.141

@throws WireException

## matchEquals()

Match equals, not equals, less, greater, etc.

@param string $value

## matchIsEmpty()

Match is an empty empty string, null or not present

## matchIsNotEmpty()

Match is present, not null and not an empty string

## matchLikePhrase()

Match LIKE phrase

@param string $value

## matchLikeStartEnd()

Match starts-with or ends-with using only LIKE (no match/against index)

Does not ignore whitespace, closing tags or punctutation at start/end the way that the
matchStartEnd() method does, so this can be used to perform more literal start/end matches.

@param string $value

## matchLikeWords()

Match words (plural) LIKE, given words can appear in full or in any part of a word

@param string $value

@since 3.0.160

## matchWords()

Match contains words (full, any or partial)

@param string $value

@since 3.0.160

## matchPhrase()

Match contains entire phrase/string (*=)

@param string $value

## matchPhraseExpand()

Match phrase with query expansion (*+=)

@param string $value

## matchRegular()

Perform a regular scored MATCH/AGAINST query (non-boolean)

@param string $value

## matchStartEnd()

Match phrase at start or end of field value (also uses fulltext index when possible)

Ignores whitespace, punctuation and opening/closing tags, enabling it to match
start/end words or phrases surrounded by non-word characters.

@param $value

## matchCommands()

Match text using boolean mode commands (Advanced search)

@param string $text

@since 3.0.160

## getBooleanModeWords()

Get verbose data array of words identified and prepared for boolean mode

@param string $value

@param array $options
 - `required` (bool): Are given words required in the query? (default=true)
 - `partial` (bool): Is it okay to match a partial value? i.e. can "will" match "willy" (default=false)
 - `partialLast` (bool): Use partial only for last word? (default=null, auto-detect)
 - `partialLess` (bool): Weight partial match words less than full word match? (default=false)
 - `phrase` (bool): Is entire $value a full phrase to match? (default=auto-detect)
 - `useStopwords` (bool): Allow inclusion of stopwords? (default=null, auto-detect)
 - `alternates` (bool): Get word alternates? (default=null, auto-detect)

@return array Value provided to the function with boolean operators added, or verbose array.

## getBooleanModeAlternateWords()

Helper for getBooleanModeWords to handle population of alternate words in boolean value

@param string $word Word to find alternates for

@param string &$booleanValue Existing boolean value which will be updated

@param int $minWordLength

@param array $options

@return array

@since 3.0.162

## getBooleanModeCommands()

Get boolean query value where "+" and "-" and "*" and '"' are allowed in query to affect results

@param string $value

@return string

## words()

Get array of words from given value

@param string $value

@param array $options

@return array

## rlikeValue()

Prepare a word or phrase for use in an RLIKE statement

@param string $value

@param array $options

@return string

## strlen()

@param string $value

@return int

## isStopword()

Is given word a stopword?

@param string $word

@return bool

## isShortword()

Is word too short for fulltext index?

@param string $word

@return bool

## isIndexableWord()

Is given word not a stopword and long enough to be indexed?

@param string $word

@return bool

## getScoreFieldName()

Get unique score field name

@return string

@since 3.0.160

## getMinWordLength()

Get minimum allowed indexable word length

@return int

## getWordAlternates()

Get other variations of given word to search (such as plural, singular, lemmas, etc.)

@param string $word

@param int|null $minLength Minimum length for returned words

@return array

## getWordRoot()

Get root of word (currently not implemented)

@param string $word

@return string

## forceLike()

Call forceLike(true) to force use of LIKE, or omit argument to get current setting

This forces LIKE only for matching operators that have a LIKE equivalent.
This includes these operators: `*=`, `^=`, `$=`, `~=`, `~|=`.

@param bool|null $forceLike

@return bool

@since 3.0.182
