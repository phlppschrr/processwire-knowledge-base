# Selectors

Source: `wire/core/Selectors.php`

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

@link https://processwire.com/api/selectors/ Official Selectors Documentation

ProcessWire 3.x, Copyright 2026 by Ryan Cramer
https://processwire.com

@todo Move static helper methods to dedicated API var/class so this class can be more focused

@todo Determine whether Selector array handling methods would be better in separate/descending class

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [init()](method-init.md)
Method: [create()](method-create.md)
Method: [extractString()](method-extractstring.md)
Method: [extractGroup()](method-extractgroup.md)
Method: [extractField()](method-extractfield.md)
Method: [extractOperator()](method-extractoperator.md)
Method: [extractOperators()](method-extractoperators.md)
Method: [extractValueQuick()](method-extractvaluequick.md)
Method: [extractValue()](method-extractvalue.md)
Method: [getAllFields()](method-getallfields.md)
Method: [getAllValues()](method-getallvalues.md)
Method: [matches()](method-matches.md)
Method: [matchesSelector()](method-matchesselector.md)
Method: [matchesOrGroups()](method-matchesorgroups.md)
Method: [getSelectorArrayType()](method-getselectorarraytype.md)
Method: [getOperatorsFromField()](method-getoperatorsfromfield.md)
Method: [makeSelectorArrayItem()](method-makeselectorarrayitem.md)
Method: [getSelectorByField()](method-getselectorbyfield.md)
Method: [getSelectorByFieldValue()](method-getselectorbyfieldvalue.md)
Method: [__toString()](method-__tostring.md)
Method: [__debugInfo()](method-__debuginfo.md)
Method: [debugInfoItem()](method-debuginfoitem.md)
Method: [setCustomVariableValue()](method-setcustomvariablevalue.md)
Method: [___getCustomVariableValue()](method-___getcustomvariablevalue.md)

Constants:
Const: [maxOperatorLength](const-maxoperatorlength.md)
