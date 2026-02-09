# LanguageParser

Source: `wire/modules/LanguageSupport/LanguageParser.php`

Inherits: `Wire`

ProcessWire Language Parser

Parses a PHP file to locate all function calls containing translatable text and their optional comments.

Return the results by calling $parser->getUntranslated() and $parser->getComments();

Methods:
- [`__construct(LanguageTranslator $translator, string $file)`](method-__construct.md)
- [`getAlternates(string $hash = ''): array`](method-getalternates.md)
- [`getComments(): array`](method-getcomments.md)
- [`getUntranslated(): array`](method-getuntranslated.md)
- [`getNumFound(): int`](method-getnumfound.md)
- [`getTextFromHash(string $hash): string|bool`](method-gettextfromhash.md)
- [`execute(string $file)`](method-execute.md)
- [`findArrayTranslations(string &$data)`](method-findarraytranslations.md)
- [`parseFile(string $file): array`](method-parsefile.md)
- [`buildMatch(array $m, int $key, string $text): array`](method-buildmatch.md)
- [`processMatch(array $match)`](method-processmatch.md)
- [`unescapeText(string $text): string`](method-unescapetext.md)
- [`getTextHash(string $text, string $context): string`](method-gettexthash.md)
