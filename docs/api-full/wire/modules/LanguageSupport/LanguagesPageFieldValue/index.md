# LanguagesPageFieldValue

Source: `wire/modules/LanguageSupport/LanguagesPageFieldValue.php`

Inherits: `Wire`
Implements: `LanguagesValueInterface`, `IteratorAggregate`

Serves as a multi-language value placeholder for field values that contain a value in more than one language.

Methods:
- [`__construct(Page|null $page = null, Field|null $field = null, array|string $values = null)`](method-__construct.md) Construct the multi language value
- [`wired()`](method-wired.md) Wired to API
- [`setLanguageValue(int|Language|string $languageID, mixed $value): $this`](method-setlanguagevalue.md) Sets the value for a given language
- [`setLanguageValues(array $values, bool $reset = false): self`](method-setlanguagevalues.md) Set multiple language values at once
- [`setFromInputfield(Inputfield $inputfield)`](method-setfrominputfield.md) Grab language values from Inputfield and populate to this object
- [`setToInputfield(Inputfield $inputfield)`](method-settoinputfield.md) Populate language values from this object to given Inputfield
- [`getLanguageValue($languageID): string|mixed`](method-getlanguagevalue.md) Given a language, returns the value in that language
- [`getDefaultValue(): string`](method-getdefaultvalue.md) Returns the value in the default language
- [`getNonEmptyValue(string $failValue = ''): string`](method-getnonemptyvalue.md) Get non-empty value in this order: current lang, default lang, other lang, failValue
- [`__toString(): string`](method-__tostring.md) The string value is the value in the current user's language
- [`getStringValue(): string`](method-___getstringvalue.md) (hookable) Get string value (for hooks)
- [`setField(Field $field)`](method-setfield.md) Set field that value is for
- [`setPage(Page $page)`](method-setpage.md) Set page that value is for
- [`getPage(): Page|null`](method-getpage.md) Get page that value is for
- [`getField(): Field|null`](method-getfield.md) Get field that value is for
- [`__debugInfo(): array`](method-__debuginfo.md) Debug info
- [`getArray(): array`](method-getarray.md) Get array of language values stored in here
- [`getHash(bool $verbose = false): string`](method-gethash.md) Get hash of all language values stored in here
- [`getIterator(): \ArrayObject`](method-getiterator.md) Allows iteration of the languages values
- [`languageSupport(): null|LanguageSupport`](method-languagesupport.md)
- [`defaultLanguagePageID(): int`](method-defaultlanguagepageid.md)

Constants:
- [`langBlankInheritDefault = 0`](const-langblankinheritdefault.md)
- [`langBlankInheritNone = 1`](const-langblankinheritnone.md)
