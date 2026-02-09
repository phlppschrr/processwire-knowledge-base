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
- [`__construct(string|null|array $selector = null)`](method-__construct.md) Given a selector string, extract it into one or more corresponding Selector objects, iterable in this object.
- [`init(string|array $selector)`](method-init.md) Set the selector string or array (if not set already from the constructor)
- [`create(string $field, string $operator, string|array $value): Selector`](method-create.md) Create a new Selector object from a field name, operator, and value
- [`extractString(string $str)`](method-extractstring.md) Given a selector string, populate to Selector objects in this Selectors instance
- [`extractGroup(string &$str): null|string`](method-extractgroup.md) Given a string like name@field=... or @field=... extract the part that comes before the @
- [`extractField(string &$str): string`](method-extractfield.md) Given a string starting with a field, return that field, and remove it from $str.
- [`extractOperator(string &$str, array $operatorChars): string`](method-extractoperator.md) Given a string starting with an operator, return that operator, and remove it from $str.
- [`extractOperators(string &$str): array`](method-extractoperators.md) Given a string starting with an operator, return that operator, and remove it from $str.
- [`extractValueQuick(string &$str, string $openingQuote, string $closingQuote): false|string|string[]`](method-extractvaluequick.md) Early-exit optimizations for extractValue
- [`extractValue(string &$str, string &$quote): array|string`](method-extractvalue.md) Given a string starting with a value, return that value, and remove it from $str.
- [`getAllFields(bool $subfields = true): array`](method-getallfields.md) Return array of all field names referenced in all of the Selector objects here
- [`getAllValues(): array`](method-getallvalues.md) Return array of all values referenced in all Selector objects here
- [`matches(Wire $item): bool`](method-matches.md) Does the given Wire match these Selectors?
- [`matchesSelector(Selector $selector, Wire $item): bool`](method-matchesselector.md) Does the given Wire match these Selector (single)?
- [`matchesOrGroups(array $orGroups, Wire $item): bool`](method-matchesorgroups.md) Do the given OR-groups match the given Wire?
- [`getSelectorArrayType(int|string|array $data): string`](method-getselectorarraytype.md) Return string indicating given data type for use in selector arrays
- [`getOperatorsFromField(string &$field): array`](method-getoperatorsfromfield.md) Extract and return operator from end of field name, as used by selector arrays
- [`makeSelectorArrayItem(string|int $key, array $data, string $dataType = ''): array`](method-makeselectorarrayitem.md) Return an array of an individual Selector info, for use by setSelectorArray() method
- [`getSelectorByField(string $fieldName, bool $or = false, bool $all = false): Selector|array|null`](method-getselectorbyfield.md) Get the first selector that uses given field name
- [`getSelectorByFieldValue(string $fieldName, string|int $value, bool $or = false, bool $all = false): Selector|array|null`](method-getselectorbyfieldvalue.md) Get the first selector that uses given field name AND has the given value
- [`__toString(): string`](method-__tostring.md) Value when typecast as string
- [`__debugInfo(): array`](method-__debuginfo.md) Debug info
- [`debugInfoItem(Selector|mixed $item): array|mixed|null|string`](method-debuginfoitem.md) Debug info for Selector item
- [`setCustomVariableValue(string $name, string|int|array|WireData|float|null|bool $value)`](method-setcustomvariablevalue.md) Set a custom [variable] value available to all Selectors and PageFinder class instances
- [`getCustomVariableValue(string $name): null|string`](method-___getcustomvariablevalue.md) (hookable) Get the value for a custom [var] to populate in a selector (also works in PageFinder)

Constants:
- [`maxOperatorLength`](const-maxoperatorlength.md)
