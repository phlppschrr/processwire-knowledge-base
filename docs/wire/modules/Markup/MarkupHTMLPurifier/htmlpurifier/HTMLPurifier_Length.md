# HTMLPurifier_Length

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Represents a measurable length, with a string numeric magnitude
and a unit. This object is immutable.

## make()

@param string $s Unit string, like '2em' or '3.4in'
@return HTMLPurifier_Length
@warning Does not perform validation.

## validate()

Validates the number and unit.
@return bool

## toString()

Returns string representation of number.
@return string

## getN()

Retrieves string numeric magnitude.
@return string

## getUnit()

Retrieves string unit.
@return string

## isValid()

Returns true if this length unit is valid.
@return bool

## compareTo()

Compares two lengths, and returns 1 if greater, -1 if less and 0 if equal.
@param HTMLPurifier_Length $l
@return int
@warning If both values are too large or small, this calculation will
         not work properly
