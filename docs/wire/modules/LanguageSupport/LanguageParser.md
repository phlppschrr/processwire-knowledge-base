# LanguageParser

Source: `wire/modules/LanguageSupport/LanguageParser.php`

ProcessWire Language Parser

Parses a PHP file to locate all function calls containing translatable text and their optional comments.

Return the results by calling $parser->getUntranslated() and $parser->getComments();

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## __construct()

Construct the Language Parser

@param LanguageTranslator $translator

@param string $file PHP filename to parse

## getAlternates()

Get phrase alternates

@param string $hash Specify phrase hash to get alternates or omit to get all alternates

@return array

## getComments()

Return all found comments, indexed by hash

@return array

## getUntranslated()

Return all found phrases (in untranslated form), indexed by hash

@return array

## getNumFound()

Return number of phrases found total

@return int

## getTextFromHash()

Given a hash, return the untranslated text associated with it

@param string $hash

@return string|bool Returns untranslated text (string) on success or boolean false if not available

## execute()

Begin parsing given file

@param string $file

## findArrayTranslations()

Find text array values and place in alternates

This method also converts the __(['a','b','c']) array calls to single value calls like __('a')
as a pre-parser for all parsers that follow it, so they do not need to be * aware of array values
for translation calls.

@param string $data

## parseFile()

Run regexes on file contents to locate all translation functions

@param string $file

@return array

## buildMatch()

Build the match abstracted away from the preg_match result

@param array $m

@param int $key

@param string $text

@return array

## processMatch()

Process the match and populate $this->untranslated and $this->comments

@param array $match

## unescapeText()

Replace any escaped characters with non-escaped versions

@param string $text

@return string

## getTextHash()

Get hash for given text + context

@param string $text

@param string $context

@return string
