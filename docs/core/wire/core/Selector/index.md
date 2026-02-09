# Selector

Source: `wire/core/Selector.php`

Inherits: `WireData`


Groups:
Group: [other](group-other.md)
Group: [properties](group-properties.md)

ProcessWire Selector base type and implementation for various Selector types

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

Methods:
- [`__construct(string|array $field, string|int|array $value)`](method-__construct.md)
- [`operator(): string`](method-operator.md)
- [`field(bool|int $forceString = true): string|array|null`](method-field.md)
- [`fields(): array`](method-fields.md)
- [`value(bool|int $forceString = true): string|array|null`](method-value.md)
- [`values(bool $nonEmpty = false): array`](method-values.md)
- [`get(string $key): array|mixed|null|string`](method-get.md)
- [`setField(string|array $field): self`](method-setfield.md)
- [`setValue(string|int|array|mixed $value): self`](method-setvalue.md)
- [`set(string $key, mixed $value): Selector|WireData`](method-set.md)
- [`getCompareType(): int`](method-getcomparetype.md)
- [`getLabel(): string`](method-getlabel.md)
- [`getDescription(): string`](method-getdescription.md)
- [`match(mixed $value1, string $value2): bool`](method-match.md)
- [`matches(string|int|Wire|array $value): bool`](method-matches.md)
- [`evaluate(bool $matches): bool`](method-evaluate.md)
- [`sanitizeFieldName(string|array $fieldName): string|array`](method-sanitizefieldname.md)
- [`__toString()`](method-__tostring.md)

Constants:
- [`compareTypeExact`](const-comparetypeexact.md)
- [`compareTypeSort`](const-comparetypesort.md)
- [`compareTypeFind`](const-comparetypefind.md)
- [`compareTypeLike`](const-comparetypelike.md)
- [`compareTypeBitwise`](const-comparetypebitwise.md)
- [`compareTypeExpand`](const-comparetypeexpand.md)
- [`compareTypeCommand`](const-comparetypecommand.md)
- [`compareTypeDatabase`](const-comparetypedatabase.md)
- [`compareTypeFulltext`](const-comparetypefulltext.md)
- [`compareTypePhrase`](const-comparetypephrase.md)
- [`compareTypeWords`](const-comparetypewords.md)
- [`compareTypePartial`](const-comparetypepartial.md)
- [`compareTypeAny`](const-comparetypeany.md)
- [`compareTypeAll`](const-comparetypeall.md)
- [`compareTypeBoundary`](const-comparetypeboundary.md)
