# Selector Cheatsheet

Source: https://processwire.com/docs/selectors/
Source: https://processwire.com/docs/selectors/operators/

## Selector Structure

Selectors are simple strings of text that specify fields and values. These selectors are used throughout ProcessWire to find pages (and other types of data).

## Operators

- = — Equal to — Given value is the same as value compared to.
- != — Not equal to — Given value is not the same as value compared to.
- < — Less than — Compared value is less than given value.
- > — Greater than — Compared value is greater than given value.
- <= — Less than or equal to — Compared value is less than or equal to given value.
- >= — Greater than or equal to — Compared value is greater than or equal to given value.
- *= — Contains phrase/text — Given phrase or word appears in value compared to.
- ~= — Contains all words — All given whole words appear in compared value, in any order.
- %= — Contains phrase/text like — Phrase or word appears in value compared to, using like.
- ^= — Starts with phrase/text — Word or phrase appears at start of compared value.
- $= — Ends with phrase/text — Word or phrase appears at end of compared value.
- %^= — Starts like — Word or phrase appears at beginning of compared value, using like.
- %$= — Ends like — Word or phrase appears at end of compared value, using like.
- #= — Advanced text search — Match full or partial words and phrases with commands.*
- *+= — Contains phrase expand — Phrase or word appears in value compared to and expand results.*
- ~*= — Contains all partial words — All whole or partial words appear in value, in any order.*
- ~~= — Contains all words live — All whole words and last partial word appear in any order.*
- ~%= — Contain all words like — All whole or partial words appear in value using like, in any order.*
- ~+= — Contains all words expand — All whole words appear in value and expand results.*
- ~|= — Contains any words — Any given whole words appear in value, in any order.*
- ~|*= — Contains any partial words — Any given whole or partial words appear in value, in any order.*
- ~|%= — Contains any words like — Any given whole or partial words appear in value using like, in any order.*
- ~|+= — Contains any words expand — Any given whole words appear in value and expand results.*
- **= — Contains match — Any given whole words match against value.*
- **+= — Contains match expand — Any given whole words match against value and expand results.*
- & — Bitwise AND — Given integer results in positive AND against compared value.
