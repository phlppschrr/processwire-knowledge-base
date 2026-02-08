# Selector

Source: `wire/core/Selector.php`

ProcessWire Selector base type and implementation for various Selector types

Selectors hold a field, operator and value and are used in finding things

This file provides the base implementation for a Selector, as well as implementation
for several actual Selector types under the main Selector class.

ProcessWire 3.x, Copyright 2020 by Ryan Cramer
https://processwire.com

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

Groups:
Group: [other](group-other.md)
Group: [properties](group-properties.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [operator()](method-operator.md)
Method: [field()](method-field.md)
Method: [fields()](method-fields.md)
Method: [value()](method-value.md)
Method: [values()](method-values.md)
Method: [get()](method-get.md)
Method: [setField()](method-setfield.md)
Method: [setValue()](method-setvalue.md)
Method: [set()](method-set.md)
Method: [getCompareType()](method-getcomparetype.md)
Method: [getLabel()](method-getlabel.md)
Method: [getDescription()](method-getdescription.md)
Method: [match()](method-match.md)
Method: [matches()](method-matches.md)
Method: [evaluate()](method-evaluate.md)
Method: [sanitizeFieldName()](method-sanitizefieldname.md)
Method: [__toString()](method-__tostring.md)

Constants:
Const: [compareTypeExact](const-comparetypeexact.md)
Const: [compareTypeSort](const-comparetypesort.md)
Const: [compareTypeFind](const-comparetypefind.md)
Const: [compareTypeLike](const-comparetypelike.md)
Const: [compareTypeBitwise](const-comparetypebitwise.md)
Const: [compareTypeExpand](const-comparetypeexpand.md)
Const: [compareTypeCommand](const-comparetypecommand.md)
Const: [compareTypeDatabase](const-comparetypedatabase.md)
Const: [compareTypeFulltext](const-comparetypefulltext.md)
Const: [compareTypePhrase](const-comparetypephrase.md)
Const: [compareTypeWords](const-comparetypewords.md)
Const: [compareTypePartial](const-comparetypepartial.md)
Const: [compareTypeAny](const-comparetypeany.md)
Const: [compareTypeAll](const-comparetypeall.md)
Const: [compareTypeBoundary](const-comparetypeboundary.md)
