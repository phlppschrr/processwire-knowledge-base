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

Methods:
- [`__construct(string $encoding = 'UTF-8')`](method-__construct.md)
- [`encode(string $input): string`](method-encode.md)
- [`encodePart(string $input): string`](method-encodepart.md)
- [`decode(string $input): string`](method-decode.md)
- [`decodePart(string $input): string`](method-decodepart.md)
- [`calculateThreshold(integer $k, integer $bias): integer`](method-calculatethreshold.md)
- [`adapt(integer $delta, integer $numPoints, boolean $firstTime): integer`](method-adapt.md)
- [`listCodePoints(string $input): array`](method-listcodepoints.md)
- [`charToCodePoint(string $char): integer`](method-chartocodepoint.md)
- [`codePointToChar(integer $code): string`](method-codepointtochar.md)

Constants:
- [`BASE`](const-base.md)
