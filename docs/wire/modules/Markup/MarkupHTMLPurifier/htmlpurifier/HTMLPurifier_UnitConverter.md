# HTMLPurifier_UnitConverter

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Class for converting between different unit-lengths as specified by
CSS.

## getSigFigs()

Returns the number of significant figures in a string number.
@param string $n Decimal number
@return int number of sigfigs

## add()

Adds two numbers, using arbitrary precision when available.
@param string $s1
@param string $s2
@param int $scale
@return string

## mul()

Multiples two numbers, using arbitrary precision when available.
@param string $s1
@param string $s2
@param int $scale
@return string

## div()

Divides two numbers, using arbitrary precision when available.
@param string $s1
@param string $s2
@param int $scale
@return string

## round()

Rounds a number according to the number of sigfigs it should have,
using arbitrary precision when available.
@param float $n
@param int $sigfigs
@return string

## scale()

Scales a float to $scale digits right of decimal point, like BCMath.
@param float $r
@param int $scale
@return string
