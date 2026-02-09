# DatabaseQuerySelectFulltext

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Inherits: `Wire`

## Summary

ProcessWire DatabaseQuerySelectFulltext

Common methods:
- [`getQuery()`](method-getquery.md)
- [`tableField()`](method-tablefield.md)
- [`allowOrder()`](method-alloworder.md)
- [`allowStopwords()`](method-allowstopwords.md)
- [`matchType()`](method-matchtype.md)

Groups:
Group: [other](group-other.md)

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

## Methods
- [`__construct(DatabaseQuerySelect $query)`](method-__construct.md) Construct
- [`__get(string $name): mixed|string`](method-__get.md)
- [`getQuery(): DatabaseQuerySelect`](method-getquery.md) Get the query that was provided to the constructor
- [`tableField(): string`](method-tablefield.md) Get 'tableName.fieldName' string
- [`allowOrder(null|bool $allow = null): bool|null`](method-alloworder.md) Get or set whether or not 'ORDER BY' statements are allowed to be added
- [`allowStopwords(null|bool $allow = null): bool`](method-allowstopwords.md) Get or set whether fulltext searches can fallback to LIKE searches to match stopwords
- [`matchType(): string`](method-matchtype.md)
- [`escapeLike(string $str): string`](method-escapelike.md) Escape string for use in a MySQL LIKE
- [`escapeAgainst(string $str): string`](method-escapeagainst.md) Additional escape for use in a MySQL AGAINST
- [`value(string $value): string`](method-value.md)
- [`match(string $tableName, string $fieldName, string $operator, string|int|array $value): $this`](method-match.md) Update the query (provided to the constructor) to match the given arguments
- [`matchArrayFieldName(array $fieldNames, mixed $value)`](method-matcharrayfieldname.md) Match when given $fieldName is an array
- [`matchArrayValue(array $value)`](method-matcharrayvalue.md) Match when given $value is an array
- [`matchEquals(string $value)`](method-matchequals.md) Match equals, not equals, less, greater, etc.
- [`matchIsEmpty()`](method-matchisempty.md) Match is an empty empty string, null or not present
- [`matchIsNotEmpty()`](method-matchisnotempty.md) Match is present, not null and not an empty string
- [`matchLikePhrase(string $value)`](method-matchlikephrase.md) Match LIKE phrase
- [`matchLikeStartEnd(string $value)`](method-matchlikestartend.md) Match starts-with or ends-with using only LIKE (no match/against index)
- [`matchLikeWords(string $value)`](method-matchlikewords.md) Match words (plural) LIKE, given words can appear in full or in any part of a word
- [`matchWords(string $value)`](method-matchwords.md) Match contains words (full, any or partial)
- [`matchPhrase(string $value)`](method-matchphrase.md) Match contains entire phrase/string (*=)
- [`matchPhraseExpand(string $value)`](method-matchphraseexpand.md) Match phrase with query expansion (*+=)
- [`matchRegular(string $value)`](method-matchregular.md) Perform a regular scored MATCH/AGAINST query (non-boolean)
- [`matchStartEnd($value)`](method-matchstartend.md) Match phrase at start or end of field value (also uses fulltext index when possible)
- [`matchCommands(string $text)`](method-matchcommands.md) Match text using boolean mode commands (Advanced search)
- [`getBooleanModeWords(string $value, array $options = array()): array`](method-getbooleanmodewords.md) Get verbose data array of words identified and prepared for boolean mode
- [`getBooleanModeAlternateWords(string $word, &$booleanValue, int $minWordLength, array $options): array`](method-getbooleanmodealternatewords.md) Helper for getBooleanModeWords to handle population of alternate words in boolean value
- [`getBooleanModeCommands(string $value): string`](method-getbooleanmodecommands.md) Get boolean query value where "+" and "-" and "*" and '"' are allowed in query to affect results
- [`words(string $value, array $options = array()): array`](method-words.md) Get array of words from given value
- [`rlikeValue(string $value, array $options = array()): string`](method-rlikevalue.md) Prepare a word or phrase for use in an RLIKE statement
- [`strlen(string $value): int`](method-strlen.md)
- [`isStopword(string $word): bool`](method-isstopword.md) Is given word a stopword?
- [`isShortword(string $word): bool`](method-isshortword.md) Is word too short for fulltext index?
- [`isIndexableWord(string $word): bool`](method-isindexableword.md) Is given word not a stopword and long enough to be indexed?
- [`getScoreFieldName(): string`](method-getscorefieldname.md) Get unique score field name
- [`getMinWordLength(): int`](method-getminwordlength.md) Get minimum allowed indexable word length
- [`getWordAlternates(string $word, int|null $minLength = null): array`](method-getwordalternates.md) Get other variations of given word to search (such as plural, singular, lemmas, etc.)
- [`getWordRoot(string $word): string`](method-getwordroot.md) Get root of word (currently not implemented)
- [`forceLike(bool|null $forceLike = null): bool`](method-forcelike.md) Call forceLike(true) to force use of LIKE, or omit argument to get current setting

## Constants
- [`maxQueryValueLength = 500`](const-maxqueryvaluelength.md)
