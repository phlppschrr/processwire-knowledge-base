# Using Selectors

Source: https://processwire.com/docs/selectors/

## Summary

Selectors are simple strings of text that specify fields and values. These selectors are used throughout ProcessWire to find pages (and other types of data).

## Key Points

- Selectors are simple strings of text that specify fields and values. These selectors are used throughout ProcessWire to find pages (and other types of data).
- For example, name=karena is a simple selector that says: “find items that have the name karena.” Selectors in ProcessWire are loosely based around the idea and syntax of attribute selectors in jQuery.
- An individual selector consists of three parts: the field you are looking for, an operator (like an equals '=' sign), and the value you want to match. For example, a basic selector might be:

## Sections


### The components of a selector

An individual selector consists of three parts: the field you are looking for, an operator (like an equals '=' sign), and the value you want to match. For example, a basic selector might be:


### Where do you use selectors?

Selectors are used throughout ProcessWire, typically for getting and finding pages with the $page and $pages variables. Below is a list of the most common functions where selectors are used:


### Selector fields

The field portion of a selector may refer to any field of a page. If you want to know what fields you can use for matching, see "Setup > Fields" in your ProcessWire admin. All custom fields are typically optimized for fast matches.


### Selector operators

The operator portion of a selector may be one of the following:

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


### Selector values

After the operator comes the selector value that we want to match. At the basic level, little explanation is needed and the examples in the above section (operators) make that clear. But because selector values can contain nearly anything (including text submitted from user input, like a search for example), we need to take some special care with string-based selector values. If your selector value needs to contain a comma, you should surround your selector value in quotes, i.e.


### Specifying multiple selectors

A selector string can match more than one field. You may specify multiple selectors together by separating each with a comma. For example, the following selector would match all pages with a year of 2010 and the word "Hanna" appearing somewhere in the body:


### OR selectors: matching one value or another

In instances where you need to match values in a single field with an either-or expression, the values should be split with the "or" operator, which is the pipe character "|". The following examples demonstrates its usage:


### OR selectors, matching one field or another

This was already described in the selector fields section above, but is repeated here for reference. Field names may be separated by a pipe "|" to indicate an OR condition:
