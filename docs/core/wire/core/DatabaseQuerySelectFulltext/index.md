# DatabaseQuerySelectFulltext

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

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

Methods:
- [`__construct(DatabaseQuerySelect $query)`](method-__construct.md)
- [`__get(string $name): mixed|string`](method-__get.md)
- [`getQuery(): DatabaseQuerySelect`](method-getquery.md)
- [`tableField(): string`](method-tablefield.md)
- [`allowOrder(null|bool $allow = null): bool|null`](method-alloworder.md)
- [`allowStopwords(null|bool $allow = null): bool`](method-allowstopwords.md)
- [`matchType(): string`](method-matchtype.md)
- [`escapeLike(string $str): string`](method-escapelike.md)
- [`escapeAgainst(string $str): string`](method-escapeagainst.md)
- [`value(string $value): string`](method-value.md)
- [`match(string $tableName, string $fieldName, string $operator, string|int|array $value): $this`](method-match.md)
- [`matchArrayFieldName(array $fieldNames, mixed $value)`](method-matcharrayfieldname.md)
- [`matchArrayValue(array $value)`](method-matcharrayvalue.md)
- [`matchEquals(string $value)`](method-matchequals.md)
- [`matchIsEmpty()`](method-matchisempty.md)
- [`matchIsNotEmpty()`](method-matchisnotempty.md)
- [`matchLikePhrase(string $value)`](method-matchlikephrase.md)
- [`matchLikeStartEnd(string $value)`](method-matchlikestartend.md)
- [`matchLikeWords(string $value)`](method-matchlikewords.md)
- [`matchWords(string $value)`](method-matchwords.md)
- [`matchPhrase(string $value)`](method-matchphrase.md)
- [`matchPhraseExpand(string $value)`](method-matchphraseexpand.md)
- [`matchRegular(string $value)`](method-matchregular.md)
- [`matchStartEnd($value)`](method-matchstartend.md)
- [`matchCommands(string $text)`](method-matchcommands.md)
- [`getBooleanModeWords(string $value, array $options = array()): array`](method-getbooleanmodewords.md)
- [`getBooleanModeAlternateWords(string $word, &$booleanValue, int $minWordLength, array $options): array`](method-getbooleanmodealternatewords.md)
- [`getBooleanModeCommands(string $value): string`](method-getbooleanmodecommands.md)
- [`words(string $value, array $options = array()): array`](method-words.md)
- [`rlikeValue(string $value, array $options = array()): string`](method-rlikevalue.md)
- [`strlen(string $value): int`](method-strlen.md)
- [`isStopword(string $word): bool`](method-isstopword.md)
- [`isShortword(string $word): bool`](method-isshortword.md)
- [`isIndexableWord(string $word): bool`](method-isindexableword.md)
- [`getScoreFieldName(): string`](method-getscorefieldname.md)
- [`getMinWordLength(): int`](method-getminwordlength.md)
- [`getWordAlternates(string $word, int|null $minLength = null): array`](method-getwordalternates.md)
- [`getWordRoot(string $word): string`](method-getwordroot.md)
- [`forceLike(bool|null $forceLike = null): bool`](method-forcelike.md)

Constants:
- [`maxQueryValueLength`](const-maxqueryvaluelength.md)
