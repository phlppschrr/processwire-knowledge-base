# ProcessWire Selector Operators

Source: https://processwire.com/docs/selectors/operators/

## Sections


## Selector Operators in ProcessWire

A selector like “field=value” consists of three parts—the field (or fields) you are looking for, an operator (like an equals “=” sign), and the value (or values) you want to match. On this page all of the available operators are covered in depth.


## Operator index

|  |  |  |
| --- | --- | --- |
| `=` | [Equal to](/docs/selectors/operators/#equal) | Given value is the same as value compared to. |
| `!=` | [Not equal to](/docs/selectors/operators/#not-equal) | Given value is not the same as value compared to. |
| `<` | [Less than](/docs/selectors/operators/#less-than) | Compared value is less than given value. |
| `>` | [Greater than](/docs/selectors/operators/#greater-than) | Compared value is greater than given value. |
| `<=` | [Less than or equal to](/docs/selectors/operators/#less-than-equal) | Compared value is less than or equal to given value. |
| `>=` | [Greater than or equal to](/docs/selectors/operators/#greater-than-equal) | Compared value is greater than or equal to given value. |
| `*=` | [Contains phrase/text](/docs/selectors/operators/#contains) | Given phrase or word appears in value compared to. |
| `~=` | [Contains all words](/docs/selectors/operators/#contains-words) | All given whole words appear in compared value, in any order. |
| `%=` | [Contains phrase/text like](/docs/selectors/operators/#contains-like) | Phrase or word appears in value compared to, using like. |
| `^=` | [Starts with phrase/text](/docs/selectors/operators/#starts) | Word or phrase appears at start of compared value. |
| `$=` | [Ends with phrase/text](/docs/selectors/operators/#ends) | Word or phrase appears at end of compared value. |
| `%^=` | [Starts like](#starts-like) | Word or phrase appears at beginning of compared value, using like. |
| `%$=` | [Ends like](#ends-like) | Word or phrase appears at end of compared value, using like. |
| `#=` | [Advanced text search](/docs/selectors/operators/#contains-advanced) | Match full or partial words and phrases with commands.* |
| `*+=` | [Contains phrase expand](/docs/selectors/operators/#contains-expand) | Phrase or word appears in value compared to and expand results.* |
| `~*=` | [Contains all partial words](/docs/selectors/operators/#contains-words-partial) | All whole or partial words appear in value, in any order.* |
| `~~=` | [Contains all words live](/docs/selectors/operators/#contains-words-live) | All whole words and last partial word appear in any order.* |
| `~%=` | [Contain all words like](/docs/selectors/operators/#contains-words-like) | All whole or partial words appear in value using like, in any order.* |
| `~+=` | [Contains all words expand](/docs/selectors/operators/#contains-words-expand) | All whole words appear in value and expand results.* |
| `~\|=` | [Contains any words](/docs/selectors/operators/#contains-any-words) | Any given whole words appear in value, in any order.* |
| `~\|*=` | [Contains any partial words](/docs/selectors/operators/#contains-any-words-partial) | Any given whole or partial words appear in value, in any order.* |
| `~\|%=` | [Contains any words like](/docs/selectors/operators/#contains-any-words-like) | Any given whole or partial words appear in value using like, in any order.* |
| `~\|+=` | [Contains any words expand](/docs/selectors/operators/#contains-any-words-expand) | Any given whole words appear in value and expand results.* |
| `**=` | [Contains match](/docs/selectors/operators/#contains-match) | Any given whole words match against value.* |
| `**+=` | [Contains match expand](/docs/selectors/operators/#contains-match-expand) | Any given whole words match against value and expand results.* |
| `&` | [Bitwise AND](/docs/selectors/operators/#bitwise-and) | Given integer results in positive AND against compared value. |

* Operators with asterisk require ProcessWire 3.0.160 or newer.


## General operators

These operators can generally be used anywhere in ProcessWire and with and kind of data.


### `=` Equals

```php
$pages->find("name=about");
```

Given value is the same as value compared to.


### `!=` Not equals

```php
$pages->find("id!=1");
```

Given value is not the same as value compared to.


### `>` Greater than

```php
$pages->find("children.count>0");
```

Compared value is greater than given value.


### `<` Less than

```php
$pages->find("price<100");
```

Compared value is less than given value.


### `>=` Greater than or equal

```php
$pages->find("price>=100");
```

Compared value is greater than or equal to given value.


### `<=` Less than or equal

```php
$pages->find("price<=100");
```

Compared value is less than or equal to given value.


## Phrase matching operators

When given search value contains only one word, these operators match that word partially or in full. When given search value contains more than one word, then the words are matched as a phrase, meaning they only match if they appear in the exact order given. So a search for “foo bar” would only match documents that contain those two words alongside each other in that order. The last word in a phrase may be a partial match, meaning a search for “foo bar” would match the literal phrase “foo bar” but also “foo bars”, “foo barn”, “foo barnyard”, etc.


### `*=` Contains phrase

```php
$pages->find("title*=wire tool");
```

Given phrase or word appears in value compared to. Uses “fulltext” index. Can partial match the last word in given phrase from beginning, meaning a search for “wire tool” can match “wire toolbox” but not “processwire tools”.


### `%=` Contains text like

```php
$pages->find("title%=wire tool");
```

Given phrase or word appears in value compared to. Matches using “like”. Can partial match first word from end and last word from beginning, meaning a search for “wire tool” can match both “processwire tools” and “wire toolbox”.


### `*+=` Contains phrase expand

```php
$pages->find("title*+=CDN");
```

Given phrase or word appears in value compared to. Expand to include potentially related terms and word variations. Uses “fulltext” index. Available in ProcessWire 3.0.160 or newer. This behaves exactly the same as the “contains phrase” operator except that it adds in MySQL query expansion (and optionally related words) to include other potentially related results that don't exactly match the phrase. Expanded matches come after exact matches. As an example, a search for "CDN" may also match pages about ProCache, even if they don't mention CDNs in the title (the database found the relation since ProCache provides CDN features).


### `^=` Starts with

```php
$pages->find("body^=Lorem Ipsum");
```

Given word or phrase appears at beginning of compared value. Uses “fulltext” index. Ignores leading HTML markup, punctutation or whitespace in searched documents.


### `%^=` Starts like

```php
$pages->find("body%^=Lorem Ipsum");
```

Given word or phrase appears at beginning of compared value. Matches using only “like”, bypassing the index for special cases. Does not ignore leading HTML markup or punctuation in searched documents.


### `$=` Ends with

```php
$pages->find("body$=mollit anim id est laborum");
```

Given word or phrase appears at end of compared value. Uses “fulltext” index. Ignores trailing HTML markup, punctutation or whitespace in searched documents.


### `%$=` Ends like

```php
$pages->find("body%$=mollit anim id est laborum.");
```

Given word or phrase appears at end of compared value. Matches using only “like”, bypassing the index for special cases. Can be useful if you need a search like “in the bookstore” to match a document containing “within the bookstore” since “like” can perform a partial match on the first word.


## Word matching operators

The primary difference between word and phrase matching operators is that word matching operators match words in any order. This means a search for “foo bar” will match anything that contains the words “foo” and “bar”, no matter where they appear.


### `~=` Contains all words

```php
$pages->find("title~=foo bar");
```

All given words appear in compared value, in any order. Matches whole words only. Uses “fulltext” index.


### `~*=` Contains all partial words

```php
$pages->find("title~*=web image");
```

All given words appear in compared value, in any order. Matches whole or partial words. Partial matches from beginning of words. Uses “fulltext” index. Available in ProcessWire 3.0.160 or newer. This is like the existing "match words" ~= operator except that rather than just matching whole words, it can match partial words as well. Meaning that a search for "web image" will match terms like "WebP" and "images" (plural), rather than only matching "web" and "image" (singular).


### `~~=` Contains all words live

```php
$pages->find("title~~=api pro");
```

All given words appear in compared value, in any order. Partial matches last word in given value. Uses “fulltext” index. Available in ProcessWire 3.0.160 or newer. This operator is designed to work exactly like the existing "match words" ~= operator except that the last word is considered a "partial match" word rather than a full match word. That makes this particular operator useful in live-search situations where you are returning results as someone types.


### `~%=` Contains all words like

```php
$pages->find("title~%=build site");
```

All given words appear in compared value, in any order. Matches whole or partial words. Partial matches anywhere within words. Matches using “like”. Available in ProcessWire 3.0.160 or newer. This operator matches all words in the query in full or in part. It can perform partial matches not just from the beginning of the word, but anywhere within the word. That means that a word like "build" can match words like "building" and "rebuild", and words like "site" can match words like "website" and "sites".


### `~+=` Contains all words expand

```php
$pages->find("title~+=books");
```

All given words appear in compared value, in any order. Matches whole words. Expand to include potentially related terms and word variations. Uses “fulltext” index. Available in ProcessWire 3.0.160 or newer. This operator works exactly like the regular "match words" ~= operator except that it also adds in "query expansion". This is a feature of MySQL fulltext indexes where in the best case it seems to magically come up with related matches, even if they don't contain the original search terms. It analyzes the matching results and looks for words in the match that might be fairly unique, checks if those words appear on any other items, and bundles them into the results when they do. As an example, a search for the term "books" on this site can match "Canongate Books" and a related blog post that doesn't even mention the term "books" in the title. Note however that the longer the query, the more likely that query expansion is to introduce noise into the results, but that's to be expected.


### `~|=` Contains any words

```php
$pages->find("title~|=architecture engineering construction");
```

Any given words appear in compared value, in any order. Matches whole words. Uses “fulltext” index. Available in ProcessWire 3.0.160 or newer. This is different from all of the above mentioned word matching operators, which require that all words be present.


### `~|*=` Contains any partial words

```php
$pages->find("title~|*=auth edit");
```

Any given words appear in compared value, in any order. Matches whole or partial words. Partial matches from beginning of words. Uses “fulltext” index. Available in ProcessWire 3.0.160 or newer. This is just like the "contains any words" operator above, except that it can also match partial words. This means that words like "auth" will match "author" and "authentication", and words like "edit" will match "editor" and "editing".


### `~|%=` Contains any words like

```php
$pages->find("title~|%=grade port");
```

Any given words appear in compared value, in any order. Matches whole or partial words. Partial matches anywhere within words. Matches using “like”. Available in ProcessWire 3.0.160 or newer. This is just like the above mentioned "contains any partial words" operator except that it uses LIKE rather than the fulltext index to perform matches. This means it can be slower (at scale) but can match anywhere in words, rather than just from the beginning of them. For example a term like "grade" can also match "upgrade", and a term like "port" can match "import", "export", "portal", etc.


### `~|+=` Contains any words expand

```php
$pages->find("title~|+=login register");
```

Any given words appear in compared value, in any order. Expand to include potentially related terms and word variations. Uses “fulltext” index. Available in ProcessWire 3.0.162 or newer. This is the same as the "contains any words" operator except that it adds in query expansion to include other potentially related documents that may not contain the words searched for. Documents containing the words come before the expanded results that might not.


### `**=` Contains match

```php
$pages->find("title**=hook selectors");
```

Any given words match against compared value. Matches whole words. Uses “fulltext” index. Available in ProcessWire 3.0.160 or newer. This uses something more like the standard fulltext MATCH/AGAINST logic included with MySQL than most of the other operators. For those that want this more traditional search logic, this operator provides it. It behaves in an OR fashion with the words, but ranks results according to how many of the requested words appear.


### `**+=` Contains match expand

```php
$pages->find("title**+=login register");
```

Any given words match against compared value. Matches whole words. Expand to include potentially related terms and word variations. Uses “fulltext” index. Available in ProcessWire 3.0.160 or newer. This is just like the "contains match" operator mentioned above, except that it also adds in MySQL query expansion, discussed in earlier operators.


## Advanced operators


### `#=` Advanced text search

```php
$pages->find('title#="+image* -file*"');
```

Searches using this operator recognize special command characters that designate what is, and is not included. Available in ProcessWire 3.0.160 or newer. When "+" is prefixed to a word or quoted phrase, it indicates that term must be included. When "-" is prefixed to a quoted word or phrase, it indicates that term must NOT be included. When there is no prefix, then it means the term or phrase is optional but its presence will increase ranking. Any word can be appended with an asterisk "*" to indicate that you also want to match any words that begin with the term. For example "bar*" will match not just bar, but also barn, barbell, barge, etc. To perform phrase matches, surround the phrase with parenthesis or double quotes. For example "+(foo bar)" must match phrase "foo bar", "-(foo bar)" must not match that phrase, and "(foo bar)" makes the phrase optional but documents matching it are ranked higher.

- `+word` MUST appear
- `-word` MUST NOT appear
- `word` (no prefix) MAY appear (increases rank)
- `bar*` or `+bar*` matches bar, barn, barge
- `-bar*` prevents matching bar, barn, barge, etc.
- `+(foo bar)` or `+"foo bar"` indicates the phrase "foo bar" MUST appear
- `-(foo bar)` or `-"foo bar"` indicates the phrase "foo bar" MUST NOT appear
- `(foo bar)` indicates the phrase MAY appear (increases rank)

When using the advanced text search, we recommend surrounding the query text/commands in double quotes, or in ProcessWire 3.0.182 or newer, the [selectorValueAdvanced() sanitizer method](../../../full/wire/core/Sanitizer/method-selectorvalueadvanced.md) will take care of preparing and quoting the $value for you.


### `&` Bitwise AND*

```php
$pages->find("status&1024");
```

Given integer value matches bitwise AND with compared integer value. Note that this operator can only be used in specific cases where matching against a flags value.


## Using more than one operator at a time

In ProcessWire 3.0.161 and newer, you can use more than one operator in any `field=value` selector expression. It works anywhere that you might use a selector, whether querying the database or something in memory. The best way to explain it is with an example. Let's say that you want to find all pages with a title containing the phrase "hello world" — you'd do this using the "contains text/phrase" operator: ***= **

```php
$pages->find("title*=hello world");
```

But let's also say that if you don't find any matches, you want to fallback to find any pages that contain the words "hello" and "world" anywhere in the title, in any order. We'd use the "contains all words" operator "~=" to do that. So now you can add that operator to the existing one, and it'll fallback to it if the first operator fails to match. So we'll append the "contains all words" operator to the previous one: **~=**

```php
$pages->find("title*=~=hello world");
```

Great! But maybe we still aren't finding any matches, so we want to fallback to something even broader. So if the phrase match fails, and the words match fails, now we want to fallback to find any pages that contain the words "hello" OR "world", rather than requiring them both. For that we can use our "contains any words" operator: **~|= **

```php
$pages->find("title*=~=~|=hello world");
```

This example is getting a bit contrived now, but let's say that if we still haven't found a match, we want it to find any pages that have *any* words starting with "hello" or "world", so it would find pages with words like "helloes", "worlds", "worldwide", etc. That's a job for our new "contains any partial words" operator: **~|*=**

```php
$pages->find("title*=~=~|=~|*=hello world");
```

Okay last one I promise—you probably wouldn't stack this many in real life, but stay with me here. Let's say the query still didn't find anything, and as a final fallback, we want it to find any words LIKE "hello" or "world", so that those terms can match anywhere in words, enabling us to find pages with words like in the previous example, but also words like "phellogen", "othello", "underworld", "otherworldly", etc., and that's a job for our "contains any words like" operator: **~|%=**

```php
$pages->find("title*=~=~|=~|*=~|%=hello world");
```

So that looks like a pretty complex operator there, but as you've seen by following the example, it's just these 5 appended operators to each other:

- `*=` Contains phrase
- `~=` Contains all whole words
- `~|=` Contains any whole words
- `~|*=` Contains any partial words
- `~|%=` Contains any words like

I think a more likely scenario in a site search is that you might stack two operators, such as the *= followed by the ~|*=, or whatever combination suits your need. So long as you are running ProcessWire 3.0.161 or newer, you can do this with any operators, not just the text searching ones.
