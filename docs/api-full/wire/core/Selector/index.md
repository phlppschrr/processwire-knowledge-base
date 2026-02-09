# Selector

Source: `wire/core/Selector.php`

Inherits: `WireData`

## Summary

ProcessWire Selector base type and implementation for various Selector types

Common methods:
- [`operator()`](method-operator.md)
- [`field()`](method-field.md)
- [`fields()`](method-fields.md)
- [`value()`](method-value.md)
- [`values()`](method-values.md)

Groups:
Group: [other](group-other.md)
Group: [properties](group-properties.md)

Selectors hold a field, operator and value and are used in finding things

This file provides the base implementation for a Selector, as well as implementation
for several actual Selector types under the main Selector class.


Selector maintains a single selector consisting of field name, operator, and value.

- Serves as the base class for the different Selector types (`SelectorEqual`, `SelectorNotEqual`, `SelectorLessThan`, etc.)
- The constructor requires `$field` and `$value` properties which may either be an array or string.
  An array indicates multiple items in an OR condition. Multiple items may also be specified by
  pipe “|” separated strings.
- Operator is determined by the Selector class name, and thus may not be changed without replacing
  the entire Selector.

~~~~~
// very basic usage example
// constructor takes ($field, $value) which can be strings or arrays
$s = new SelectorEqual('title', 'About Us');
// $page can be any kind of Wire-derived object
if($s->matches($page)) {
  // $page has title "About Us"
}
~~~~~
~~~~~
// another usage example
$s = new SelectorContains('title|body|summary', 'foo|bar');
if($s->matches($page)) {
  // the title, body or summary properties of $page contain either the text "foo" or "bar"
}
~~~~~

### List of core selector-derived classes

- `SelectorEqual`
- `SelectorNotEqual`
- `SelectorGreaterThan`
- `SelectorLessThan`
- `SelectorGreaterThanEqual`
- `SelectorLessThanEqual`
- `SelectorContains`
- `SelectorContainsLike`
- `SelectorContainsWords`
- `SelectorContainsWordsPartial` (3.0.160+)
- `SelectorContainsWordsLive` (3.0.160)
- `SelectorContainsWordsLike` (3.0.160)
- `SelectorContainsWordsExpand` (3.0.160)
- `SelectorContainsAnyWords` (3.0.160)
- `SelectorContainsAnyWordsPartial` (3.0.160)
- `SelectorContainsAnyWordsLike` (3.0.160)
- `SelectorContainsExpand` (3.0.160)
- `SelectorContainsMatch` (3.0.160)
- `SelectorContainsMatchExpand` (3.0.160)
- `SelectorContainsAdvanced` (3.0.160)
- `SelectorStarts`
- `SelectorStartsLike`
- `SelectorEnds`
- `SelectorEndsLike`
- `SelectorBitwiseAnd`

## Methods
- [`__construct(string|array $field, string|int|array $value)`](method-__construct.md) Given a field name and value, construct the Selector.
- [`operator(): string`](method-operator.md) Return the operator used by this Selector
- [`field(bool|int $forceString = true): string|array|null`](method-field.md) Get the field(s) of this Selector
- [`fields(): array`](method-fields.md) Return array of field(s) for this Selector
- [`value(bool|int $forceString = true): string|array|null`](method-value.md) Get the value(s) of this Selector
- [`values(bool $nonEmpty = false): array`](method-values.md) Return array of value(s) for this Selector
- [`get(string $key): array|mixed|null|string`](method-get.md) Get a property
- [`setField(string|array $field): self`](method-setfield.md) Set field or fields
- [`setValue(string|int|array|mixed $value): self`](method-setvalue.md) Set selector value(s)
- [`set(string $key, mixed $value): Selector|WireData`](method-set.md) Set a property of the Selector
- [`getCompareType(): int`](method-getcomparetype.md) What type of comparson does Selector perform?
- [`getLabel(): string`](method-getlabel.md) Get short label that describes this Selector
- [`getDescription(): string`](method-getdescription.md) Get longer description that describes this Selector
- [`match(mixed $value1, string $value2): bool`](method-match.md) Does `$value1` match `$value2`?
- [`matches(string|int|Wire|array $value): bool`](method-matches.md) Does this Selector match the given value?
- [`evaluate(bool $matches): bool`](method-evaluate.md) Provides the opportunity to override or NOT the condition
- [`sanitizeFieldName(string|array $fieldName): string|array`](method-sanitizefieldname.md) Sanitize field name
- [`__toString()`](method-__tostring.md) The string value of Selector is always the selector string that it originated from

## Constants
- [`compareTypeExact = 1`](const-comparetypeexact.md)
- [`compareTypeSort = 2`](const-comparetypesort.md)
- [`compareTypeFind = 4`](const-comparetypefind.md)
- [`compareTypeLike = 8`](const-comparetypelike.md)
- [`compareTypeBitwise = 16`](const-comparetypebitwise.md)
- [`compareTypeExpand = 32`](const-comparetypeexpand.md)
- [`compareTypeCommand = 64`](const-comparetypecommand.md)
- [`compareTypeDatabase = 128`](const-comparetypedatabase.md)
- [`compareTypeFulltext = 256`](const-comparetypefulltext.md)
- [`compareTypePhrase = 512`](const-comparetypephrase.md)
- [`compareTypeWords = 1024`](const-comparetypewords.md)
- [`compareTypePartial = 2048`](const-comparetypepartial.md)
- [`compareTypeAny = 4096`](const-comparetypeany.md)
- [`compareTypeAll = 8192`](const-comparetypeall.md)
- [`compareTypeBoundary = 16384`](const-comparetypeboundary.md)
