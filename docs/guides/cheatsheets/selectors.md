# Selector Cheatsheet

Source: https://processwire.com/docs/selectors/
Source: https://processwire.com/docs/selectors/operators/

## Selector Structure

Selectors are simple strings of text that specify fields and values. These selectors are used throughout ProcessWire to find pages (and other types of data).

## Operators

- `=` — [Equal to](/docs/selectors/operators/#equal) — Given value is the same as value compared to.
- `!=` — [Not equal to](/docs/selectors/operators/#not-equal) — Given value is not the same as value compared to.
- `<` — [Less than](/docs/selectors/operators/#less-than) — Compared value is less than given value.
- `>` — [Greater than](/docs/selectors/operators/#greater-than) — Compared value is greater than given value.
- `<=` — [Less than or equal to](/docs/selectors/operators/#less-than-equal) — Compared value is less than or equal to given value.
- `>=` — [Greater than or equal to](/docs/selectors/operators/#greater-than-equal) — Compared value is greater than or equal to given value.
- `*=` — [Contains phrase/text](/docs/selectors/operators/#contains) — Given phrase or word appears in value compared to.
- `~=` — [Contains all words](/docs/selectors/operators/#contains-words) — All given whole words appear in compared value, in any order.
- `%=` — [Contains phrase/text like](/docs/selectors/operators/#contains-like) — Phrase or word appears in value compared to, using like.
- `^=` — [Starts with phrase/text](/docs/selectors/operators/#starts) — Word or phrase appears at start of compared value.
- `$=` — [Ends with phrase/text](/docs/selectors/operators/#ends) — Word or phrase appears at end of compared value.
- `%^=` — [Starts like](#starts-like) — Word or phrase appears at beginning of compared value, using like.
- `%$=` — [Ends like](#ends-like) — Word or phrase appears at end of compared value, using like.
- `#=` — [Advanced text search](/docs/selectors/operators/#contains-advanced) — Match full or partial words and phrases with commands.*
- `*+=` — [Contains phrase expand](/docs/selectors/operators/#contains-expand) — Phrase or word appears in value compared to and expand results.*
- `~*=` — [Contains all partial words](/docs/selectors/operators/#contains-words-partial) — All whole or partial words appear in value, in any order.*
- `~~=` — [Contains all words live](/docs/selectors/operators/#contains-words-live) — All whole words and last partial word appear in any order.*
- `~%=` — [Contain all words like](/docs/selectors/operators/#contains-words-like) — All whole or partial words appear in value using like, in any order.*
- `~+=` — [Contains all words expand](/docs/selectors/operators/#contains-words-expand) — All whole words appear in value and expand results.*
- `~|=` — [Contains any words](/docs/selectors/operators/#contains-any-words) — Any given whole words appear in value, in any order.*
- `~|*=` — [Contains any partial words](/docs/selectors/operators/#contains-any-words-partial) — Any given whole or partial words appear in value, in any order.*
- `~|%=` — [Contains any words like](/docs/selectors/operators/#contains-any-words-like) — Any given whole or partial words appear in value using like, in any order.*
- `~|+=` — [Contains any words expand](/docs/selectors/operators/#contains-any-words-expand) — Any given whole words appear in value and expand results.*
- `**=` — [Contains match](/docs/selectors/operators/#contains-match) — Any given whole words match against value.*
- `**+=` — [Contains match expand](/docs/selectors/operators/#contains-match-expand) — Any given whole words match against value and expand results.*
- `&` — [Bitwise AND](/docs/selectors/operators/#bitwise-and) — Given integer results in positive AND against compared value.
