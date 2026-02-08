# Punycode

Source: `wire/core/Punycode.php`

Punycode implementation as described in RFC 3492

@link http://tools.ietf.org/html/rfc3492

@link https://github.com/true/php-punycode

Copyright (c) 2014 TrueServer B.V.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

## BASE

Bootstring parameter values

## __construct()

Constructor

@param string $encoding Character encoding

## encode()

Encode a domain to its Punycode version

@param string $input Domain name in Unicode to be encoded

@return string Punycode representation in ASCII

## encodePart()

Encode a part of a domain name, such as tld, to its Punycode version

@param string $input Part of a domain name

@return string Punycode representation of a domain part

## decode()

Decode a Punycode domain name to its Unicode counterpart

@param string $input Domain name in Punycode

@return string Unicode domain name

## decodePart()

Decode a part of domain name, such as tld

@param string $input Part of a domain name

@return string Unicode domain part

## calculateThreshold()

Calculate the bias threshold to fall between TMIN and TMAX

@param integer $k

@param integer $bias

@return integer

## adapt()

Bias adaptation

@param integer $delta

@param integer $numPoints

@param boolean $firstTime

@return integer

## listCodePoints()

List code points for a given input

@param string $input

@return array Multi-dimension array with basic, non-basic and aggregated code points

## charToCodePoint()

Convert a single or multi-byte character to its code point

@param string $char

@return integer

## codePointToChar()

Convert a code point to its single or multi-byte character

@param integer $code

@return string
