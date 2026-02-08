# Selectors

Source: `wire/core/Selectors.php`

ProcessWire Selectors

Processes a selector string into a WireArray of Selector objects.
Static helper methods useful in analyzing selector strings outside of this class.
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

## other

@method Selector[] getIterator()

@method null|string getCustomVariableValue($name, $property = '')

## maxOperatorLength

Maximum length for a selector operator

## __construct()

Given a selector string, extract it into one or more corresponding Selector objects, iterable in this object.

@param string|null|array $selector Please omit this argument and use a separate init($selector) call instead.

## init()

Set the selector string or array (if not set already from the constructor)

~~~~~
$selectors = new Selectors();
$selectors->init("sale_price|retail_price>100, currency=USD|EUR");
~~~~~

@param string|array $selector

## create()

Create a new Selector object from a field name, operator, and value

This is mostly for internal use, as the Selectors object already does this when you pass it
a selector string in the constructor or init() method.


@param string $field Field name or names (separated by a pipe)

@param string $operator Operator, i.e. "="

@param string|array $value Value or values (separated by a pipe)

@return Selector Returns the correct type of `Selector` object that corresponds to the given `$operator`.

@throws WireException

## extractString()

Given a selector string, populate to Selector objects in this Selectors instance

@param string $str The string containing a selector (or multiple selectors, separated by commas)

## extractGroup()

Given a string like name@field=... or @field=... extract the part that comes before the @

This part indicates the group name, which may also be blank to indicate grouping with other blank grouped items

@param string $str

@return null|string

## extractField()

Given a string starting with a field, return that field, and remove it from $str.

@param string $str

@return string

## extractOperator()

Given a string starting with an operator, return that operator, and remove it from $str.

@param string $str

@param array $operatorChars

@return string

@deprecated Replaced by extractOperators()

@todo this method can be removed once confirmed nothing else uses it

## extractOperators()

Given a string starting with an operator, return that operator, and remove it from $str.

@param string $str

@return array

## extractValueQuick()

Early-exit optimizations for extractValue

@param string $str String to extract value from, $str will be modified if extraction successful

@param string $openingQuote Opening quote character, if string has them, blank string otherwise

@param string $closingQuote Closing quote character, if string has them, blank string otherwise

@return false|string|string[] Returns found value if successful, boolean false if not

## extractValue()

Given a string starting with a value, return that value, and remove it from $str.

@param string $str String to extract value from

@param string $quote Automatically populated with quote type, if found

@return array|string Found values or value (excluding quotes)

## getAllFields()

Return array of all field names referenced in all of the Selector objects here

@param bool $subfields Default is to allow "field.subfield" fields, or specify false to convert them to just "field".

@return array Returned array has both keys and values as field names (same)

## getAllValues()

Return array of all values referenced in all Selector objects here

@return array Returned array has both keys and values as field values (same)

## matches()

Does the given Wire match these Selectors?

@param Wire $item

@return bool

## matchesSelector()

Does the given Wire match these Selector (single)?

@param Selector $selector

@param Wire $item

@return bool

@since 3.0.330

## matchesOrGroups()

Do the given OR-groups match the given Wire?

@param array|string[]|array[] $orGroups

@param Wire $item

@return bool

@since 3.0.330

## getSelectorArrayType()

Return string indicating given data type for use in selector arrays

@param int|string|array $data

@return string

## getOperatorsFromField()

Extract and return operator from end of field name, as used by selector arrays

@param string $field

@return array

## makeSelectorArrayItem()

Return an array of an individual Selector info, for use by setSelectorArray() method

@param string|int $key

@param array $data

@param string $dataType One of 'string', 'array', 'assoc', or 'verbose'

@return array

@throws WireException

## getSelectorByField()

Get the first selector that uses given field name

This is useful for quickly retrieving values of reserved properties like "include", "limit", "start", etc.

Using **$or:** By default this excludes selectors that have fields in an OR expression, like "a|b|c".
So if you specified field "a" it would not be matched. If you wanted it to still match, specify true
for the $or argument.

Using **$all:** By default only the first matching selector is returned. If you want it to return all
matching selectors in an array, then specify true for the $all argument. This changes the return value
to always be an array of Selector objects, or a blank array if no match.

@param string $fieldName Name of field to return value for (i.e. "include", "limit", etc.)

@param bool $or Allow fields that appear in OR expressions? (default=false)

@param bool $all Return an array of all matching Selector objects? (default=false)

@return Selector|array|null Returns null if field not present in selectors (or blank array if $all mode)

## getSelectorByFieldValue()

Get the first selector that uses given field name AND has the given value

Using **$or:** By default this excludes selectors that have fields or values in an OR expression, like "a|b|c".
So if you specified field "a" it would not be matched. If you wanted it to still match, specify true
for the $or argument.

Using **$all:** By default only the first matching selector is returned. If you want it to return all
matching selectors in an array, then specify true for the $all argument. This changes the return value
to always be an array of Selector objects, or a blank array if no match.

@param string $fieldName Name of field to match

@param string|int $value Value that must match

@param bool $or Allow fields and values that appear in OR expressions? (default=false)

@param bool $all Return an array of all matching Selector objects? (default=false)

@return Selector|array|null Returns null if field not present in selectors (or blank array if $all mode)

@since 3.0.142

## __toString()

Value when typecast as string

@return string

## __debugInfo()

Debug info

@return array

## debugInfoItem()

Debug info for Selector item

@param Selector|mixed $item

@return array|mixed|null|string

## setCustomVariableValue()

Set a custom [variable] value available to all Selectors and PageFinder class instances

~~~~
Selectors::setCustomVariableValue('foo', 'bar');
$s = new Selectors("name=[foo]");
echo $s; // outputs: "name=bar"
$pages->find("name=[foo]"); // finds pages with name=bar
~~~~

@param string $name

@param string|int|array|WireData|float|null|bool $value

@since 3.0.255

## ___getCustomVariableValue()

Get the value for a custom [var] to populate in a selector (also works in PageFinder)

This can be useful for cases where the variable would be stored somewhere in
a configuration, like a Lister selector or Page reference field selector, where PHP
variables typically wouldn't be available.

If hooking this method, /site/ready.php is recommended.

@param string $name

@return null|string

@since 3.0.255
