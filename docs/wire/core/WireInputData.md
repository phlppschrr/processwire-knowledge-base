# WireInputData

Source: `wire/core/WireInputData.php`

WireInputData manages one of GET, POST, COOKIE, or whitelist

WireInputData and the WireInput class together form a simple
front end to PHP's $_GET, $_POST, and $_COOKIE superglobals.

Vars retrieved from here will not have to consider magic_quotes.
No sanitization or filtering is done, other than disallowing
multi-dimensional arrays in input.

WireInputData specifically manages one of: get, post, cookie or
whitelist, whereas the WireInput class provides access to the 3
InputData instances.

Each WireInputData is not instantiated unless specifically asked for.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

@link http://processwire.com/api/ref/input/ Offical $input API variable documentation

## other

@method string name($varName) Sanitize to ProcessWire name format

@method string varName($varName) Sanitize to PHP variable name format

@method string fieldName($varName) Sanitize to ProcessWire Field name format

@method string templateName($varName) Sanitize to ProcessWire Template name format

@method string pageName($varName) Sanitize to ProcessWire Page name format

@method string pageNameTranslate($varName) Sanitize to ProcessWire Page name format with translation of non-ASCII characters to ASCII equivalents

@method string filename($varName) Sanitize to valid file basename as used by filenames in ProcessWire

@method string pagePathName($varName) Sanitize to what could be a valid page path in ProcessWire

@method string email($varName) Sanitize email address, converting to blank if invalid

@method string emailHeader($varName) Sanitize string for use in an email header

@method string text($varName, $options = array()) Sanitize to single line of text up to 255 characters (1024 bytes max), HTML markup is removed

@method string textarea($varName) Sanitize to multi-line text up to 16k characters (48k bytes), HTML markup is removed

@method string url($varName) Sanitize to a valid URL, or convert to blank if it can't be sanitized

@method string selectorField($varName) Sanitize a field name for use in a selector string

@method string selectorValue($varName) Sanitize a value for use in a selector string

@method string entities($varName) Return an entity encoded version of the value

@method string purify($varName) Return a value run through HTML Purifier (value assumed to contain HTML)

@method string string($varName) Return a value guaranteed to be a string, regardless of what type $varName is. Does not sanitize.

@method string date($varName, $dateFormat) Validate and return $varName in the given PHP date() or strftime() format.

@method int int($varName, $min = 0, $max = null) Sanitize value to integer with optional min and max. Unsigned if max >= 0, signed if max < 0.

@method int intUnsigned($varName, $min = null, $max = null) Sanitize value to unsigned integer with optional min and max.

@method int intSigned($varName, $min = null, $max = null) Sanitize value to signed integer with optional min and max.

@method float float($varName, $min = null, $max = null, $precision = null) Sanitize value to float with optional min and max values.

@method array array($varName, $sanitizer = null) Sanitize array or CSV String to an array, optionally running elements through specified $sanitizer.

@method array intArray($varName, $min = 0, $max = null) Sanitize array or CSV string to an array of integers with optional min and max values.

@method string|null option($varName, array $allowedValues) Return value of $varName only if it exists in $allowedValues.

@method array options($varName, array $allowedValues) Return all values in array $varName that also exist in $allowedValues.

@method bool bool($varName) Sanitize value to boolean (true or false)

## __construct()

Construct

@param array $input Associative array of variables to store

@param bool $lazy Use lazy loading?

## setArray()

Set associative array of variables to store

@param array $input

@return $this

## getArray()

Get associative array of all input variables

@return array

## __set()

Set an input value

@param string $key

@param mixed $value

## set()

Set a value

@param string $key

@param string|int|float|array|null $value

@return $this

@param array|int|string $options Options not currently used, but available for descending classes or future use

@since 3.0.141 You can also use __set() or set directly for compatibility with all versions

## get()

Get a value

@param string $key

@param array|int|string $options Options not currently used, but available for descending classes or future use

@return string|int|float|array|null $value

@since 3.0.141 You can also get directly or use __get(), both of which are compatible with all versions

## findOne()

Find one input var that matches given pattern in name (or optionally value)

@param string $pattern Wildcard string or PCRE regular expression

@param array|int|string $options
 - `type` (string): Specify "value" to match input value (rather input name), OR prefix pattern with "value=".
 - `sanitizer` (string): Name of sanitizer to run values through (default='', none)
 - `arrays` (bool): Also find on input varibles that are arrays? (default=false)

@return string|int|float|array|null $value Returns value if found or null if not.

@since 3.0.163

## find()

Find all input vars that match given pattern in name (or optionally value)

~~~~~
// find all input vars having name beginning with "title_" (i.e. title_en, title_de, title_es)
$values = $input->post->find('title_*');

// find all input vars having name with "title" anywhere in it (i.e. title, subtitle, titles, title_de)
$values = $input->post->find('*title*');

// find all input vars having value with the term "wire" anywhere, regardless of case
$values = $input->post->find('/wire/i', [ 'type' => 'value' ]);

// example of result from above find operation:
$values = [
  'title' => 'ProcessWire CMS',
  'subtitle' => 'Have plenty of caffeine to make sure you are wired',
  'sidebar' => 'Learn how to rewire a flux capacitor...',
  'summary' => 'All about the $wire API variable',
];
~~~~~

@param string $pattern Wildcard string or PCRE regular expression

@param array $options
 - `type` (string): Specify "value" to match input value (rather input name), OR prefix pattern with "value=".
 - `limit` (int): Maximum number of items to return (default=0, no limit)
 - `sanitizer` (string): Name of sanitizer to run values through (default='', none)
 - `arrays` (bool): Also find on input varibles that are arrays? (default=false)

@return array Returns associative array of values `[ name => value ]` if found, or empty array if none found.

@since 3.0.163

## cleanArray()

Clean an array of data

Support multi-dimensional arrays consistent with `$config->wireInputArrayDepth`
setting (3.0.178+) and remove slashes if applicable/necessary.

@param array $a

@return array

## setStripSlashes()

Set whether or not slashes should be stripped

@param $stripSlashes

## __get()

Get an input value

@param string $key

@return mixed|null

## remove()

Remove a value from input

@param string $key Name of input variable to remove value for

@return $this

## removeAll()

Remove all values from input

@return $this

## ___callUnknown()

Maps to Sanitizer functions

@param string $method

@param array $arguments

@return string|int|array|float|null Returns null when input variable does not exist

@throws WireException
