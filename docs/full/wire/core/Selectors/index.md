# Selectors

Source: `wire/core/Selectors.php`

Inherits: `WireArray`


Groups:
Group: [other](group-other.md)

ProcessWire Selectors

Processes a selector string into a WireArray of Selector objects.
This Selectors class is used internally by ProcessWire to provide selector string (and array) matching throughout the core.

~~~~~
$selectors = new Selectors();
$selectors->init("sale_price|retail_price>100, currency=USD|EUR");
if($selectors->matches($page)) {
  // selector string matches the given $page (which can be any Wire-derived item)
}
~~~~~
~~~~~
// iterate and display what's in this Selectors object
foreach($selectors as $selector) {
  echo "<p>";
  echo "Field(s): " . implode('|', $selector->fields) . "<br>";
  echo "Operator: " . $selector->operator . "<br>";
  echo "Value(s): " . implode('|', $selector->values) . "<br>";
  echo "</p>";
}
~~~~~
For details on how to use selectors please see [Using Selectors](https://processwire.com/docs/selectors/)
and [Selector Operators](https://processwire.com/docs/selectors/operators/).

@link https://processwire.com/docs/selectors/ Official Selectors Documentation


@todo Move static helper methods to dedicated API var/class so this class can be more focused

@todo Determine whether Selector array handling methods would be better in separate/descending class

Methods:
- [`__construct(string|null|array $selector = null)`](method-__construct.md)
- [`init(string|array $selector)`](method-init.md)
- [`create(string $field, string $operator, string|array $value): Selector`](method-create.md)
- [`extractString(string $str)`](method-extractstring.md)
- [`extractGroup(string &$str): null|string`](method-extractgroup.md)
- [`extractField(string &$str): string`](method-extractfield.md)
- [`extractOperator(string &$str, array $operatorChars): string`](method-extractoperator.md)
- [`extractOperators(string &$str): array`](method-extractoperators.md)
- [`extractValueQuick(string &$str, string $openingQuote, string $closingQuote): false|string|string[]`](method-extractvaluequick.md)
- [`extractValue(string &$str, string &$quote): array|string`](method-extractvalue.md)
- [`getAllFields(bool $subfields = true): array`](method-getallfields.md)
- [`getAllValues(): array`](method-getallvalues.md)
- [`matches(Wire $item): bool`](method-matches.md)
- [`matchesSelector(Selector $selector, Wire $item): bool`](method-matchesselector.md)
- [`matchesOrGroups(array $orGroups, Wire $item): bool`](method-matchesorgroups.md)
- [`getSelectorArrayType(int|string|array $data): string`](method-getselectorarraytype.md)
- [`getOperatorsFromField(string &$field): array`](method-getoperatorsfromfield.md)
- [`makeSelectorArrayItem(string|int $key, array $data, string $dataType = ''): array`](method-makeselectorarrayitem.md)
- [`getSelectorByField(string $fieldName, bool $or = false, bool $all = false): Selector|array|null`](method-getselectorbyfield.md)
- [`getSelectorByFieldValue(string $fieldName, string|int $value, bool $or = false, bool $all = false): Selector|array|null`](method-getselectorbyfieldvalue.md)
- [`__toString(): string`](method-__tostring.md)
- [`__debugInfo(): array`](method-__debuginfo.md)
- [`debugInfoItem(Selector|mixed $item): array|mixed|null|string`](method-debuginfoitem.md)
- [`setCustomVariableValue(string $name, string|int|array|WireData|float|null|bool $value)`](method-setcustomvariablevalue.md)
- [`getCustomVariableValue(string $name): null|string`](method-___getcustomvariablevalue.md) (hookable)

Constants:
- [`maxOperatorLength`](const-maxoperatorlength.md)
