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

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [__get()](method-__get.md)
Method: [getQuery()](method-getquery.md)
Method: [tableField()](method-tablefield.md)
Method: [allowOrder()](method-alloworder.md)
Method: [allowStopwords()](method-allowstopwords.md)
Method: [matchType()](method-matchtype.md)
Method: [escapeLike()](method-escapelike.md)
Method: [escapeAgainst()](method-escapeagainst.md)
Method: [value()](method-value.md)
Method: [match()](method-match.md)
Method: [matchArrayFieldName()](method-matcharrayfieldname.md)
Method: [matchArrayValue()](method-matcharrayvalue.md)
Method: [matchEquals()](method-matchequals.md)
Method: [matchIsEmpty()](method-matchisempty.md)
Method: [matchIsNotEmpty()](method-matchisnotempty.md)
Method: [matchLikePhrase()](method-matchlikephrase.md)
Method: [matchLikeStartEnd()](method-matchlikestartend.md)
Method: [matchLikeWords()](method-matchlikewords.md)
Method: [matchWords()](method-matchwords.md)
Method: [matchPhrase()](method-matchphrase.md)
Method: [matchPhraseExpand()](method-matchphraseexpand.md)
Method: [matchRegular()](method-matchregular.md)
Method: [matchStartEnd()](method-matchstartend.md)
Method: [matchCommands()](method-matchcommands.md)
Method: [getBooleanModeWords()](method-getbooleanmodewords.md)
Method: [getBooleanModeAlternateWords()](method-getbooleanmodealternatewords.md)
Method: [getBooleanModeCommands()](method-getbooleanmodecommands.md)
Method: [words()](method-words.md)
Method: [rlikeValue()](method-rlikevalue.md)
Method: [strlen()](method-strlen.md)
Method: [isStopword()](method-isstopword.md)
Method: [isShortword()](method-isshortword.md)
Method: [isIndexableWord()](method-isindexableword.md)
Method: [getScoreFieldName()](method-getscorefieldname.md)
Method: [getMinWordLength()](method-getminwordlength.md)
Method: [getWordAlternates()](method-getwordalternates.md)
Method: [getWordRoot()](method-getwordroot.md)
Method: [forceLike()](method-forcelike.md)

Constants:
Const: [maxQueryValueLength](const-maxqueryvaluelength.md)
