# LanguagesPageFieldValue

Source: `wire/modules/LanguageSupport/LanguagesPageFieldValue.php`

Inherits: `Wire`
Implements: `LanguagesValueInterface`, `IteratorAggregate`

Serves as a multi-language value placeholder for field values that contain a value in more than one language.

Methods:
- [`__construct(Page|null $page = null, Field|null $field = null, array|string $values = null)`](method-__construct.md)
- [`wired()`](method-wired.md)
- [`setLanguageValue(int|Language|string $languageID, mixed $value): $this`](method-setlanguagevalue.md)
- [`setLanguageValues(array $values, bool $reset = false): self`](method-setlanguagevalues.md)
- [`setFromInputfield(Inputfield $inputfield)`](method-setfrominputfield.md)
- [`setToInputfield(Inputfield $inputfield)`](method-settoinputfield.md)
- [`getLanguageValue($languageID): string|mixed`](method-getlanguagevalue.md)
- [`getDefaultValue(): string`](method-getdefaultvalue.md)
- [`getNonEmptyValue(string $failValue = ''): string`](method-getnonemptyvalue.md)
- [`__toString(): string`](method-__tostring.md)
- [`getStringValue(): string`](method-___getstringvalue.md) (hookable)
- [`setField(Field $field)`](method-setfield.md)
- [`setPage(Page $page)`](method-setpage.md)
- [`getPage(): Page|null`](method-getpage.md)
- [`getField(): Field|null`](method-getfield.md)
- [`__debugInfo(): array`](method-__debuginfo.md)
- [`getArray(): array`](method-getarray.md)
- [`getHash(bool $verbose = false): string`](method-gethash.md)
- [`getIterator(): \ArrayObject`](method-getiterator.md)
- [`languageSupport(): null|LanguageSupport`](method-languagesupport.md)
- [`defaultLanguagePageID(): int`](method-defaultlanguagepageid.md)

Constants:
- [`langBlankInheritDefault`](const-langblankinheritdefault.md)
- [`langBlankInheritNone`](const-langblankinheritnone.md)
