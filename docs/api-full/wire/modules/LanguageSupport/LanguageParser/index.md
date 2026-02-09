# LanguageParser

Source: `wire/modules/LanguageSupport/LanguageParser.php`

Inherits: `Wire`

## Summary

ProcessWire Language Parser

Common methods:
- [`getAlternates()`](method-getalternates.md)
- [`getComments()`](method-getcomments.md)
- [`getUntranslated()`](method-getuntranslated.md)
- [`getNumFound()`](method-getnumfound.md)
- [`getTextFromHash()`](method-gettextfromhash.md)

Parses a PHP file to locate all function calls containing translatable text and their optional comments.

Return the results by calling `$parser->getUntranslated()` and `$parser->getComments()`;

## Methods
- [`__construct(LanguageTranslator $translator, string $file)`](method-__construct.md) Construct the Language Parser
- [`getAlternates(string $hash = ''): array`](method-getalternates.md) Get phrase alternates
- [`getComments(): array`](method-getcomments.md) Return all found comments, indexed by hash
- [`getUntranslated(): array`](method-getuntranslated.md) Return all found phrases (in untranslated form), indexed by hash
- [`getNumFound(): int`](method-getnumfound.md) Return number of phrases found total
- [`getTextFromHash(string $hash): string|bool`](method-gettextfromhash.md) Given a hash, return the untranslated text associated with it
- [`execute(string $file)`](method-execute.md) Begin parsing given file
- [`findArrayTranslations(string &$data)`](method-findarraytranslations.md) Find text array values and place in alternates
- [`parseFile(string $file): array`](method-parsefile.md) Run regexes on file contents to locate all translation functions
- [`buildMatch(array $m, int $key, string $text): array`](method-buildmatch.md) Build the match abstracted away from the preg_match result
- [`processMatch(array $match)`](method-processmatch.md) Process the match and populate `$this->untranslated` and `$this->comments`
- [`unescapeText(string $text): string`](method-unescapetext.md) Replace any escaped characters with non-escaped versions
- [`getTextHash(string $text, string $context): string`](method-gettexthash.md) Get hash for given text + context
