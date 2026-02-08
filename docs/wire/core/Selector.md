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

## other

@property array $fields Fields that were present in selector (same as $field, but always an array).

@property string|array $field Field or fields present in the selector (string if single, or array of strings if multiple). Preferable to use $fields property instead.

@property-read string $operator Operator used by the selector.

@property array $values Values that were present in selector (same as $value, but always array).

@property string|array $value Value or values present in the selector (string if single, or array of strings if multiple). Preferable to use $values property instead.

## properties

@property bool $not Is this a NOT selector? Indicates the selector returns the opposite if what it would otherwise.

@property string|null $group Group name for this selector (if field was prepended with a "group_name@").

@property string $quote Type of quotes value was in, or blank if it was not quoted. One of: '"[{(

@property-read string $str String value of selector, i.e. “a=b”.

@property null|bool $forceMatch When boolean, forces match (true) or force non-match (false). (default=null)

@property array $altOperators Alternate operators to use when primary fails match, supported only by compareTypeFind. Since 3.0.161 (default=[])

## compareTypeExact

Comparison type: Exact (value equals this or value does not equal this)

## compareTypeSort

Comparison type: Sort (matches based on how it would sort among given value)

## compareTypeFind

Comparison type: Find (text value is found within another text value)

## compareTypeLike

Comparison type: Like (text value is like another, combined with compareTypeFind)

## compareTypeBitwise

Comparison type: Bitwise

## compareTypeExpand

Comparison type: Expand (value can be expanded to include other results when supported)

## compareTypeCommand

Comparison type: Command (value can contain additional commands interpreted by the Selector)

## compareTypeDatabase

Comparison type: Database (Selector is only applicable for database-driven comparisons)

## compareTypeFulltext

Comparison type: Fulltext index required when used with database queries

## compareTypePhrase

Comparison type: Perform phrase match (1+ words in order)

## compareTypeWords

Comparison type: Match as words independent of order (opposite of phrase)

## compareTypePartial

Comparison type: Partial matches allowed, such as partial words or phrases

## compareTypeAny

Comparison type: If multiple items in query, ANY of them may match

## compareTypeAll

Comparison type: If multiple items in query, ALL of them may match

## compareTypeBoundary

Comparison type: Matches at boundary (start or end)

## __construct()

Given a field name and value, construct the Selector.

If the provided $field is an array or pipe "|" separated string, Selector may match any of them (OR field condition)
If the provided $value is an array of pipe "|" separated string, Selector may match any one of them (OR value condition).

If only one field is provided as a string, and that field is prepended by an exclamation point, i.e. !field=something
then the condition is reversed.

@param string|array $field

@param string|int|array $value

## operator()

Return the operator used by this Selector

@return string

@since 3.0.42 Prior versions just supported the 'operator' property.

## field()

Get the field(s) of this Selector

Note that if calling this as a property (rather than a method) it can return either a string or an array.

@param bool|int $forceString Specify one of the following:
 - `true` (bool): to only return a string, where multiple-fields will be split by pipe "|". (default)
 - `false` (bool): to return string if 1 field, or array of multiple fields (same behavior as field property).
 - `1` (int): to return only the first value (string).

@return string|array|null

@since 3.0.42 Prior versions only supported the 'field' property.

@see Selector::fields()

## fields()

Return array of field(s) for this Selector

@return array

@see Selector::field()

@since 3.0.42 Prior versions just supported the 'fields' property.

## value()

Get the value(s) of this Selector

Note that if calling this as a property (rather than a method) it can return either a string or an array.

@param bool|int $forceString Specify one of the following:
 - `true` (bool): to only return a string, where multiple-values will be split by pipe "|". (default)
 - `false` (bool): to return string if 1 value, or array of multiple values (same behavior as value property).
 - `1` (int): to return only the first value (string).

@return string|array|null

@since 3.0.42 Prior versions only supported the 'value' property.

@see Selector::values()

## values()

Return array of value(s) for this Selector

@param bool $nonEmpty If empty array will be returned, forces it to return array with one blank item instead (default=false).

@return array

@see Selector::value()

@since 3.0.42 Prior versions just supported the 'values' property.

## get()

Get a property

@param string $key Property name

@return array|mixed|null|string Property value

## setField()

Set field or fields

@param string|array $field

@return self

@since 3.0.160

## setValue()

Set selector value(s)

@param string|int|array|mixed $value

@return self

@since 3.0.160

## set()

Set a property of the Selector

@param string $key

@param mixed $value

@return Selector|WireData

## getCompareType()

What type of comparson does Selector perform?

@return int Returns a Selector::compareType* constant or 0 if not defined

@since 3.0.154

## getLabel()

Get short label that describes this Selector

@return string

@since 3.0.160

## getDescription()

Get longer description that describes this Selector

@return string

@since 3.0.160

## match()

Does $value1 match $value2?

@param mixed $value1 Dynamic comparison value

@param string $value2 User-supplied value to compare against

@return bool

## matches()

Does this Selector match the given value?

If the value held by this Selector is an array of values, it will check if any one of them matches the value supplied here.

@param string|int|Wire|array $value If given a Wire, then matches will also operate on OR field=value type selectors, where present

@return bool

## evaluate()

Provides the opportunity to override or NOT the condition

Selectors should include a call to this in their matches function

@param bool $matches

@return bool

## sanitizeFieldName()

Sanitize field name

@param string|array $fieldName

@return string|array

@todo This needs testing and then to be used by this class

## __toString()

The string value of Selector is always the selector string that it originated from
