# Sanitizer

Source: `wire/core/Sanitizer.php`

ProcessWire Sanitizer

Sanitizer provides shared sanitization functions as commonly used throughout ProcessWire core and modules

Provides methods for sanitizing and validating user input, preparing data for output, and more.
Sanitizer is useful for sanitizing input or any other kind of data that you need to match a particular type or format.
The Sanitizer methods are accessed from the `$sanitizer` API variable and/or `sanitizer()` API variable/function.
For example:
~~~~~~
$cleanValue = $sanitizer->text($dirtyValue);
~~~~~~
You can replace the `text()` call above with any other sanitizer method. Many sanitizer methods also accept additional
arguments—see each individual method for details.

### Sanitizer and input

Sanitizer methods are most commonly used with user input. As a result, the methods in this class are also accessible
from the `$input->get`, `$input->post` and `$input->cookie` API variables, in the same manner that they are here.
This is a useful shortcut for instances where you don’t need to provide additional arguments to the sanitizer method.
Below are a few examples of this usage:
~~~~~
// get GET variable 'id' as integer
$id = $input->get->int('id');

// get POST variable 'name' as 1-line plain text
$name = $input->post->text('name');

// get POST variable 'comments' as multi-line plain text
$comments = $input->post->textarea('comments');
~~~~~
In ProcessWire 3.0.125 and newer you can also perform the same task as the above with one less `->` level like the
example below:
~~~~~
$comments = $input->post('comments','textarea');
~~~~~
This is more convenient in some IDEs because it’ll never be flagged as an unrecognized function call. Though outside
of that it makes little difference how you call it, as they both do the same thing.

See the `$input` API variable for more details on how to call sanitizers directly from $input.

### Adding your own sanitizers

You can easily add your own new sanitizers via ProcessWire hooks. Hooks are commonly added in a /site/ready.php file,
or from a Module, though you may add them wherever you want. The following example adds a sanitizer method called
`zip()` which enforces a 5 digit zip code:
~~~~~
$sanitizer->addHook('zip', function(HookEvent $event) {
  $sanitizer = $event->object;
  $value = $event->arguments(0); // get first argument given to method
  $value = $sanitizer->digits($value, 5); // allow only digits, max-length 5
  if(strlen($value) < 5) $value = ''; // if fewer than 5 digits, it is not a zip
  $event->return = $value;
});

// now you can use your zip sanitizer
$dirtyValue = 'Decatur GA 30030';
$cleanValue = $sanitizer->zip($dirtyValue);
echo $cleanValue; // outputs: 30030
~~~~~

### Additional options (3.0.125 or newer)

In ProcessWire 3.0.125+ you can also combine sanitizer methods in a single call. These are defined by separating each
sanitizer method with an understore. The example below runs the value through the text sanitizer and then through the
entities sanitizer:
~~~~~
$cleanValue = $sanitizer->text_entities($dirtyValue);
~~~~~
If you append a number to any sanitizer call that returns a string, it is assumed to be maximum allowed length. For
example, the following would sanitize the value to be text of no more than 20 characters:
~~~~~
$cleanValue = $sanitizer->text20($dirtyValue);
~~~~~
The above technique also works for any user-defined sanitizers you’ve added via hooks. We like this strategy for
storage of sanitizer calls that are executed at some later point, like those you might store in a module config. It
essentially enables you to define loose data types for sanitization. In addition, if there are other cases where you
need multiple sanitizers to clean a particular value, this strategy can do it with a lot less code than you would
with multiple sanitizer calls.

Most methods in the Sanitizer class focus on sanitization rather than validation, with a few exceptions. You can
convert a sanitizer call to validation call by calling the `validate()` method with the name of the sanitizer and the
value. A validation call simply implies that if the value is modified by sanitization then it is considered invalid
and thus it’ll return a non-value rather than a sanitized value. See the `Sanitizer::validate()` and
`Sanitizer::valid()` methods for usage details.


ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

@link https://processwire.com/api/variables/sanitizer/ Offical $sanitizer API variable Documentation

## other

@method array($value, $sanitizer = null, array $options = array())

@method array testAll($value)

## translate

Constant used for the $beautify argument of name sanitizer methods to indicate transliteration may be used.

## __construct()

Construct the sanitizer

## nameFilter()

**********************************************************************************************************
STRING SANITIZERS

## name()

Sanitize in "name" format (ASCII alphanumeric letters/digits, hyphens, underscores, periods)

Default behavior:

- Allows both upper and lowercase ASCII letters.
- Limits maximum length to 128 characters.
- Replaces non-name format characters with underscore "_".

~~~~~
$test = "Foo+Bar Baz-123"
echo $sanitizer->name($test); // outputs: Foo_Bar_Baz-123
~~~~~


@param string $value Value that you want to convert to name format.

@param bool|int $beautify Beautify the returned name?
 - Beautify makes returned name prettier by getting rid of doubled punctuation, leading/trailing punctuation and such.
 - Should be TRUE when creating a resource using the name for the first time (default is FALSE).
 - You may also specify the constant `Sanitizer::translate` (or integer 2) for the this argument, which will make it
   translate letters based on name format settings in ProcessWire.

@param int $maxLength Maximum number of characters allowed in the name (default=128).

@param string $replacement Replacement character for invalid characters. Should be either "_", "-" or "." (default="_").

@param array $options Extra options to replace default 'beautify' behaviors
 - `allowAdjacentExtras` (bool): Whether to allow [-_.] characters next to each other (default=false).
 - `allowDoubledReplacement` (bool): Whether to allow two of the same replacement chars [-_] next to each other (default=false).
 - `allowedExtras (array): Specify extra allowed characters (default=`['-', '_', '.']`).

@return string Sanitized value in name format

@see Sanitizer::pageName()

## names()

Sanitize a string or array containing multiple names

- Default behavior is to sanitize to ASCII alphanumeric and hyphen, underscore, and period.
- If given a string, multiple names may be separated by a delimeter (which is a space by default).
- Return value will be of the same type as the given value (i.e. string or array).


@param string|array $value Value(s) to sanitize to name format.

@param string $delimeter Character that delimits values, if $value is a string (default=" ").

@param array $allowedExtras Additional characters that are allowed in the value (default=['-', '_', '.']).

@param string $replacementChar Single character replacement value for invalid characters (default='_').

@param bool $beautify Whether or not to beautify returned values (default=false). See Sanitizer::name() for beautify options.

@return string|array Returns string if given a string for $value, returns array if given an array for $value.

## attrName()

Sanitize to an ASCII-only HTML attribute name


@param string $value

@param int $maxLength

@return string

@since 3.0.133

## htmlClass()

Sanitize string to ASCII-only HTML class attribute value

Note that this does not support all possible characters in an HTML class attribute
and instead focuses on the most commonly used ones. Characters allowed in HTML class
attributes from this method include: `-_:@a-zA-Z0-9`. This method does not allow
values that have no letters or digits.

@param string $value

@return string

@since 3.0.212

## htmlClasses()

Sanitize string to ASCII-only space-separated HTML class attribute values with no duplicates

See additional notes in `Sanitizer::htmlClass()` method.

@param string|array $value

@param bool $getArray Get array rather than string? (default=false)

@return string|array

@since 3.0.212

## fieldName()

Sanitize consistent with names used by ProcessWire fields and/or PHP variables

- Allows upper and lowercase ASCII letters, digits and underscore.
- ProcessWire field names follow the same conventions as PHP variable names, though digits may lead.
- This method is the same as the varName() sanitizer except that it supports beautification and max length.
- Unlike other name formats, hyphen and period are excluded because they aren't allowed characters in PHP variables.

~~~~~
$test = "Hello world";
echo $sanitizer->fieldName($test); // outputs: Hello_world
~~~~~


@param string $value Value you want to sanitize

@param bool|int $beautify Should be true when using the name for a new field (default=false).
 You may also specify constant `Sanitizer::translate` (or number 2) for the $beautify param, which will make it translate letters
 based on the system page name translation settings.

@param int $maxLength Maximum number of characters allowed in the name (default=128).

@return string Sanitized string

## fieldSubfield()

Sanitize as a field name but with optional subfield(s) like “field.subfield”

- Periods must be present to indicate subfield(s), otherwise behaves same as fieldName() sanitizer.
- By default allows just one subfield. To allow more, increase the $limit argument.
- To allow any quantity of subfields, specify -1.
- To reduce a `field.subfield...` combo to just `field` specify 0 for limit argument.
- Maximum length of returned string is (128 + ($limit * 128)).

~~~~~~
echo $sanitizer->fieldSubfield('a.b.c'); // outputs: a.b (default behavior)
echo $sanitizer->fieldSubfield('a.b.c', 2); // outputs: a.b.c
echo $sanitizer->fieldSubfield('a.b.c', 0); // outputs: a
echo $sanitizer->fieldSubfield('a.b.c', -1); // outputs: a.b.c (any quantity)
echo $sanitizer->fieldSubfield('foo bar.baz'); // outputs: foo_bar.baz
echo $sanitizer->fieldSubfield('foo bar baz'); // outputs: foo_bar_baz
~~~~~~


@param string $value Value to sanitize

@param int $limit Max allowed quantity of subfields, or use -1 for any quantity (default=1).

@return string

@since 3.0.126

## pageName()

Sanitize as a ProcessWire page name

- Page names by default support lowercase ASCII letters, digits, underscore, hyphen and period.

- Because page names are often generated from a UTF-8 title, UTF-8 to ASCII conversion will take place when `$beautify` is enabled.

- You may optionally omit the `$beautify` and/or `$maxLength` arguments and substitute the `$options` array instead.

- When substituted, the beautify and maxLength options can be specified in $options as well.

- If `$config->pageNameCharset` is "UTF8" then non-ASCII page names will be converted to punycode ("xn-") ASCII page names,
  rather than converted, regardless of `$beautify` setting.

~~~~~
$test = "Hello world!";
echo $sanitizer->pageName($test, true); // outputs: hello-world
~~~~~


@param string $value Value to sanitize as a page name

@param bool|int|array $beautify This argument accepts a few different possible values (default=false):
 - `true` (boolean): Make it pretty. Use this when using a pageName for the first time.
 - `$options` (array): You can optionally specify the $options array for this argument instead.
 - `Sanitizer::translate` (constant): This will make it translate non-ASCII letters based on *InputfieldPageName* module config settings.
 - `Sanitizer::toAscii` (constant): Convert UTF-8 characters to punycode ASCII.
 - `Sanitizer::toUTF8` (constant): Convert punycode ASCII to UTF-8.
 - `Sanitizer::okUTF8` (constant): Allow UTF-8 characters to appear in path (implied if $config->pageNameCharset is 'UTF8').

@param int|array $maxLength Maximum number of characters allowed in the name.
 You may also specify the $options array for this argument instead.

@param array $options Array of options to modify default behavior. See Sanitizer::name() method for available options, plus:
 - `punycodeVersion` (int): Punycode version to use with UTF-8 page names, see Sanitizer::getPunycodeVersion() method for details.

@return string

@see Sanitizer::name()

## pageNameTranslate()

Name filter for ProcessWire Page names with transliteration

This is the same as calling pageName with the `Sanitizer::translate` option for the `$beautify` argument.


@param string $value Value to sanitize

@param int $maxLength Maximum number of characters allowed in the name

@return string Sanitized value

## pageNameUTF8()

Sanitize and allow for UTF-8 characters in page name

- If `$config->pageNameCharset` is not `UTF8` then this function just passes control to the regular page name sanitizer.
- Allowed UTF-8 characters are determined from `$config->pageNameWhitelist`.
- This method does not convert to or from UTF-8, it only sanitizes it against the whitelist.
- If given a value that has only ASCII characters, this will pass control to the regular page name sanitizer.


@param string $value Value to sanitize

@param int $maxLength Maximum number of characters allowed

@return string Sanitized value

## punyDecodeName()

Decode a PW-punycode'd name value

@param string $value

@param int $version 0=auto-detect, 1=original/buggy, 2=punycode library, 3=php idn function

@return string

## punyEncodeName()

Encode a name value to PW-punycode

@param string $value

@param int $version 0=auto-detect, 1=original/buggy, 2=punycode library, 3=php idn function

@return string

## getPunycodeVersion()

Get internal Punycode version to use

0: Auto-detect from current environment.
1: PHP IDN function used by all PW versions prior to 3.0.244, but buggy PHP 7.4+.
2: Dedicated Punycode PHP library (no known issues at present).
3: PHP IDN function call updated for PHP 7.4+ (default in new installations after January 2025).

@param int $version

@return int 1=PHP DN but buggy after PHP 7.4+, 2=Punycode library, 3=PHP IDN function PHP 7.4+

@since 3.0.244

## punycode()

@return Punycode

## filename()

Name filter for ProcessWire filenames (basenames only, not paths)

This sanitizes a filename to be consistent with the name format in ProcessWire,
ASCII-alphanumeric (a-z A-Z 0-9), hyphens, underscores and periods. Note that
filenames may contain mixed case (a-z A-Z) so if you require lowercase then
run the return value through a `strtolower()` function.

~~~~~
// outputs: FileName.jpg
echo $sanitizer->filename('©®™FileName.jpg');

// outputs: c_r_tmfilename.jpg
echo strtolower($sanitizer->filename('©®™filename.jpg', Sanitizer::translate));
~~~~~


@param string $value Filename to sanitize

@param bool|int $beautify Should be true when creating a file's name for the first time. Default is false.
 You may also specify Sanitizer::translate (or number 2) for the $beautify param, which will make it translate letters
 based on the InputfieldPageName custom config settings.

@param int $maxLength Maximum number of characters allowed in the filename

@return string Sanitized filename

## path()

Validate the given path, return path if valid, or false if not valid

Returns the given path if valid, or boolean false if not.

Path is validated per ProcessWire "name" convention of ascii only [-_./a-z0-9]
As a result, this function is primarily useful for validating ProcessWire paths,
and won't always work with paths outside ProcessWire.

This method validates only and does not sanitize. See `$sanitizer->pagePathName()` for a similar
method that does sanitiation.


@param string $value Path to validate

@param int|array $options Options to modify behavior, or maxLength (int) may be specified.
 - `allowDotDot` (bool): Whether to allow ".." in a path (default=false)
 - `maxLength` (int): Maximum length of allowed path (default=1024)

@return bool|string Returns false if invalid, actual path (string) if valid.

@see Sanitizer::pagePathName()

## pagePathName()

Sanitize a page path name

Returned path is not guaranteed to be valid or match a page, just sanitized.


@param string $value Value to sanitize

@param bool|int $beautify Beautify the value? (default=false). Maybe any of the following:
- `true` (bool): Beautify the individual page names in the path to remove redundant and trailing punctuation and more.
- `false` (bool): Do not perform any conversion or attempt to make it more pretty, just sanitize (default).
- `Sanitizer::translate` (constant): Translate UTF-8 characters to visually similar ASCII (using InputfieldPageName module settings).
- `Sanitizer::toAscii` (constant): Convert UTF-8 characters to punycode ASCII.
- `Sanitizer::toUTF8` (constant): Convert punycode ASCII to UTF-8.
- `Sanitizer::okUTF8` (constant): Allow UTF-8 characters to appear in path (implied if $config->pageNameCharset is 'UTF8').

@param int $maxLength Maximum length (default=2048)

@return string Sanitized path name

## pagePathNameUTF8()

Sanitize a UTF-8 page path name (does not perform ASCII/UTF8 conversions)

- If `$config->pageNameCharset` is not `UTF8` then this does the same thing as `$sanitizer->pagePathName()`.
- Returned path is not guaranteed to be valid or match a page, just sanitized.


@param string $value Path name to sanitize

@return string

@see Sanitizer::pagePathName()

## alpha()

Sanitize to ASCII alpha (a-z A-Z)


@param string $value Value to sanitize

@param bool|int $beautify Whether to beautify (See Sanitizer::translate option too)

@param int $maxLength Maximum length of returned value (default=1024)

@return string

## alphanumeric()

Sanitize to ASCII alphanumeric (a-z A-Z 0-9)


@param string $value Value to sanitize

@param bool|int $beautify Whether to beautify (See Sanitizer::translate option too)

@param int $maxLength Maximum length of returned value (default=1024)

@return string

## digits()

Sanitize string to contain only ASCII digits (0-9)


@param string $value Value to sanitize

@param int $maxLength Maximum length of returned value (default=1024)

@return string

## email()

Sanitize and validate an email address

Returns valid email address, or blank string if it isn’t valid.


@param string $value Email address to sanitize and validate.

@param array $options All options require 3.0.208+
 - `allowIDN` (bool|int): Allow internationalized domain names? (default=false)
    Specify int 2 to also allow UTF-8 in local-part of email [SMTPUTF8] (i.e. `bøb`).
 - `getASCII` (bool): Returns ASCII encoded version of email when host is IDN (default=false)
    Does not require the allowIDN option since returned email host will be only ASCII.
    Not meant to be combined with allowIDN=2 option since local-part of email does not ASCII encode.
 - `getUTF8` (bool): Converts ASCII-encoded IDNs to UTF-8, when present (default=false)
 - `checkDNS` (bool): Check that host part of email has a valid DNS record? (default=false)
    Warning: this slows things down a lot and should not be used in time sensitive cases.
 - `throw` (bool): Throw WireException on fail with details on why it failed (default=false)

@return string Sanitized, valid email address, or blank string on failure.

## emailHeader()

Returns a value that may be used in an email header

This method is designed to prevent one email header from injecting into another.


@param string $value

@param bool $headerName Sanitize a header name rather than header value? (default=false) Since 3.0.132

@return string

## word()

Return first word in given string


@param string $value String containing one or more words

@param array $options Options to adjust behavior:
 - `keepNumbers` (bool): Allow numbers as return value? (default=true)
 - `keepNumberFormat` (bool): Keep minus/comma/period in numbers rather than splitting into words? Also requires keepNumbers==true. (default=false)
 - `keepUnderscore` (bool): Keep underscores as part of words? (default=false)
 - `keepHyphen` (bool): Keep hyphenated words? (default=false)
 - `keepChars` (array): Specify any of these to also keep as part of words ['.', ',', ';', '/', '*', ':', '+', '<', '>', '_', '-' ] (default=[])
 - `minWordLength` (int): Minimum word length (default=1)
 - `maxWordLength` (int): Maximum word length (default=80)
 - `maxWords` (int): Maximum words (default=1 or 99 if a seperator option is specified)
 - `maxLength` (int): Maximum returned string length (default=1024)
 - `stripTags` (bool): Strip markup tags so they don’t contribute to returned word? (default=true)
 - `separator' (string): Merge multiple words into one word split by this character? (default='', disabled) 3.0.195+
 - `ascii` (bool): Allow only ASCII word characters? (default=false)
 - `beautify` (bool): Make ugly strings more pretty? This collapses and trims redundant separators (default=false)

@return string

@see Sanitizer::wordsArray()

@since 3.0.162

## words()

Given string return a new string containing only words


@param $value

@param array $options
 - `separator` (string): String to use to separate words (default=' ')
 - `ascii` (string): Only allow ASCII characters in words? (default=false)
 - `keepUnderscore` (bool): Keep underscores as part of words? (default=false)
 - `keepHyphen` (bool): Keep hyphenated words? (default=false)
 - `keepChars` (array): Additional non word characters to keep (default=[])
 - `maxWordLength` (int): Maximum word length (default=80)
 - `minWordLength` (int): Minimum word length (default=1)
 - `maxLength` (int): Maximum return value length (default=1024)
 - `beautify` (bool): Make ugly strings more pretty? This collapses and trims redundant separators (default=true)

@since 3.0.195

@return string

## text()

Sanitize short string of text to single line without HTML

- This sanitizer is useful for short strings of input text like like first and last names, street names, search queries, etc.

- Please note the default 255 character max length setting.

- If using returned value for front-end output, be sure to run it through `$sanitizer->entities()` first.

~~~~~
$str = "
  <strong>Hello World</strong>
  How are you doing today?
";

echo $sanitizer->text($str);
// outputs: Hello World How are you doing today?
~~~~~


@param string $value String value to sanitize

@param array $options Options to modify default behavior:
- `maxLength` (int): maximum characters allowed, or 0=no max (default=255).
- `maxBytes` (int): maximum bytes allowed (default=0, which implies maxLength*4).
- `stripTags` (bool): strip markup tags? (default=true).
- `stripMB4` (bool): strip emoji and other 4-byte UTF-8? (default=false).
- `stripQuotes` (bool): strip out any "quote" or 'quote' characters? Specify true, or character to replace with. (default=false)
- `stripSpace` (bool|string): strip whitespace? Specify true or character to replace whitespace with (default=false). Since 3.0.105
- `reduceSpace` (bool|string): reduce consecutive whitespace to single? Specify true or character to reduce to (default=false).
   Note that the reduceSpace option is an alternative to the stripSpace option, they should not be used together. Since 3.0.105
- `allowableTags` (string): markup tags that are allowed, if stripTags is true (use same format as for PHP's `strip_tags()` function.
- `multiLine` (bool): allow multiple lines? if false, then $newlineReplacement below is applicable (default=false).
- `convertEntities` (bool): convert HTML entities to equivalent character(s)? (default=false). Since 3.0.105
- `newlineReplacement` (string): character to replace newlines with, OR specify boolean true to remove extra lines (default=" ").
- `truncateTail` (bool): if truncate necessary for maxLength, truncate from end/tail? Use false to truncate head (default=true). Since 3.0.105
- `inCharset` (string): input character set (default="UTF-8").
- `outCharset` (string): output character set (default="UTF-8").

@return string

@see Sanitizer::textarea(), Sanitizer::line()

## textarea()

Sanitize input string as multi-line text without HTML tags

- This sanitizer is useful for user-submitted text from a plain-text `<textarea>` field,
  or any other kind of string value that might have multiple-lines.

- Don’t use this sanitizer for values where you want to allow HTML (like rich text fields).
  For those values you should instead use the `$sanitizer->purify()` method.

- If using returned value for front-end output, be sure to run it through `$sanitizer->entities()` first.


@param string $value String value to sanitize

@param array $options Options to modify default behavior
- `maxLength` (int): maximum characters allowed, or 0=no max (default=16384 or 16kb).
- `maxBytes` (int): maximum bytes allowed (default=0, which implies maxLength*4 or 64kb).
- `stripTags` (bool): strip markup tags? (default=true).
- `stripMB4` (bool): strip emoji and other 4-byte UTF-8? (default=false).
- `stripIndents` (bool): Remove indents (space/tabs) at the beginning of lines? (default=false). Since 3.0.105
- `reduceSpace` (bool|string): reduce consecutive whitespace to single? Specify true or character to reduce to (default=false). Since 3.0.105
- `allowableTags` (string): markup tags that are allowed, if stripTags is true (use same format as for PHP's `strip_tags()` function.
- `convertEntities` (bool): convert HTML entities to equivalent character(s)? (default=false). Since 3.0.105
- `truncateTail` (bool): if truncate necessary for maxLength, truncate from end/tail? Use false to truncate head (default=true). Since 3.0.105
- `allowCRLF` (bool): allow CR+LF newlines (i.e. "\r\n")? (default=false, which means "\r\n" is replaced with "\n").
- `inCharset` (string): input character set (default="UTF-8").
- `outCharset` (string): output character set (default="UTF-8").

@return string

@see Sanitizer::text(), Sanitizer::purify()

## line()

Sanitize any string of text to single line, no HTML, and no specific max-length (unless given)

This is the same as the text() sanitizer but does not impose a maximum character length (or
byte length) unless given one in the `$maxLength` argument. This is useful in cases where the
text sanitizer’s built in 255 character max length (1020 max bytes) is not enough, or when you
want to specify a max length as part of the method arguments.

Please note that like with the text sanitizer, the max length refers to a maximum number of
characters, not bytes. The maxBytes is automatically set to the maxLength * 4, or can be
specifically set via the `maxBytes` option.


@param string $value String to sanitize

@param int|array $maxLength Maximum length in characters, omit (0) for no max-length, or substitute $options array

@param array $options Options to modify behavior, see text() sanitizer for all options.

@return string

@see Sanitizer::text(), Sanitizer::lines()

@since 3.0.157

## lines()

Sanitize input string as multi-line text, no HTML tags, and no specific max length (unless given)

This is the same as the textarea() sanitizer but does not impose a maximum character length (or
byte length) unless given one in the `$maxLength` argument. This is useful in cases where the
textarea sanitizer’s built in 16kb character max length (64kb max bytes) is not enough, or when you
want to specify a max length as part of the method arguments.

Please note that like with the textarea sanitizer, the max length refers to a maximum number of
characters, not bytes. The maxBytes is automatically set to the maxLength * 4, or can be
specifically set via the `maxBytes` option.


@param string $value String value to sanitize

@param int|array $maxLength Maximum length in characters, omit (0) for no max-length, or substitute $options array

@param array $options Options to modify behavior, see textarea() sanitizer for all options.

@return string

@see Sanitizer::textarea(), Sanitizer::purify(), Sanitizer::line()

@since 3.0.157

## markupToText()

Convert a string containing markup or entities to be plain text

This is one implementation but there is also a better one that you may prefer with the
`WireTextTools::markupToText()` method. Try both to determine which suits your needs
best:

~~~~~
$markup = '<html>a bunch of HTML here</html>';
// try both to see what you prefer:
$text1 = $sanitizer->markupToText($html);
$text2 = $sanitizer->getTextTools()->markupToText();
~~~~~


@param string $value String you want to convert

@param array $options Options to modify default behavior:
  - `newline` (string): Character(s) to replace newlines with (default="\n").
  - `separator` (string): Character(s) to separate HTML `<li>` items with (default="\n").
  - `entities` (bool): Entity encode returned value? (default=false).
  - `trim` (string): Character(s) to trim from beginning and end of value (default=" -,:;|\n\t").

@return string Converted string of text

@see WireTextTools::markupToText(), Sanitizer::markupToLine()

## markupToLine()

Convert a string containing markup or entities to be a single line of plain text

This is the same as the `$sanitizer->markupToText()` method except that the return
value is always just a single line.


@param string $value Value to convert

@param array $options Options to modify default behavior:
  - `newline` (string): Character(s) to replace newlines with (default=" ").
  - `separator` (string): Character(s) to separate HTML <li> items with (default=", ").
  - `entities` (bool): Entity encode returned value? (default=false).
  - `trim` (string): Character(s) to trim from beginning and end of value (default=" -,:;|\n\t").

@return string Converted string of text on a single line

## url()

Sanitize and validate given URL or return blank if it can’t be made valid

- Performs some basic sanitization like adding a scheme to the front if it's missing, but leaves alone local/relative URLs.
- URL is not required to conform to ProcessWire conventions unless a relative path is given.
- Please note that URLs should always be entity encoded in your output. Many evil things are technically allowed in a valid URL,
  so your output should always entity encoded any URLs that came from user input.

~~~~~~
$url = $sanitizer->url('processwire.com/api/');
echo $sanitizer->entities($url); // outputs: http://processwire.com/api/
~~~~~~


@param string $value URL to validate

@param bool|array $options Array of options to modify default behavior, including:
 - `allowRelative` (boolean): Whether to allow relative URLs, i.e. those without domains (default=true).
 - `allowIDN` (boolean): Whether to allow internationalized domain names (default=false).
 - `allowQuerystring` (boolean): Whether to allow query strings (default=true).
 - `allowSchemes` (array): Array of allowed schemes, lowercase (default=[] any).
 - `disallowSchemes` (array): Array of disallowed schemes, lowercase (default=['file']).
 - `requireScheme` (bool): Specify true to require a scheme in the URL, if one not present, it will be added to non-relative URLs (default=true).
 - `convertEncoded` (boolean): Convert most encoded hex characters characters (i.e. “%2F”) to non-encoded? (default=true)
 - `encodeSpace` (boolean): Encoded space to “%20” or allow “%20“ in URL? Only useful if convertEncoded is true. (default=false)
 - `stripTags` (bool): Specify false to prevent tags from being stripped (default=true).
 - `stripQuotes` (bool): Specify false to prevent quotes from being stripped (default=true).
 - `maxLength` (int): Maximum length in bytes allowed for URLs (default=4096).
 - `throw` (bool): Throw exceptions on invalid URLs (default=false).

@return string Returns a valid URL or blank string if it can’t be made valid.

@throws WireException on invalid URLs, only if `$options['throw']` is true.

## httpUrl()

URL with http or https scheme required


@param string $value URL to validate

@param array $options See the url() method for all options.

@return string Returns valid URL or blank string if it cannot be made valid.

@since 3.0.129

## filterValidateURL()

Implementation of PHP's FILTER_VALIDATE_URL with IDN and underscore support (will convert to valid)

Example: http://трикотаж-леко.рф

@param string $url

@param array $options Specify ('allowIDN' => false) to disallow internationalized domain names

@return string

## selectorValue()

Sanitizes a string value that needs to go in a ProcessWire selector

Always use this to sanitize any string values you are inserting in selector strings.
This ensures that the value can't be confused for another component of the selector string.
This method may remove characters, escape characters, or surround the string in quotes.

~~~~~
// Sanitize text for a search on title and body fields
$q = $input->get->text('q'); // text search query
$results = $pages->find("title|body%=" . $sanitizer->selectorValue($q));

// In 3.0.127 you can also provide an array for the $value argument
$val = $sanitizer->selectorValue([ 'foo', 'bar', 'baz' ]);
echo $val; // outputs: foo|bar|baz
~~~~~


@param string|array $value String value to sanitize (assumed to be UTF-8),
  or in 3.0.127+ you may use an array and it will be sanitized to an OR value string.

@param array|int $options Options to modify behavior. Note version 1 supports only `maxLength` and `useQuotes` options.
  - `version` (int): Version 1 or 2 (default=2). Version 2 available in 3.0.156+. Note option is remembered between calls.
  - `maxLength` (int): Maximum number of allowed characters (default=100). This may also be specified instead of $options array.
  - `useQuotes` (bool): Allow selectorValue() function to add quotes if it deems them necessary? (default=true)
  - All following options are only supported in version 2 (available in 3.0.156+):
  - `allowArray` (bool): Allow arrays to convert to OR-strings? If false, only 1st item in arrays is used. (default=true)
  - `allowSpace` (bool): Allow spaces? False to remove or true to allow (default=true) 3.0.168+
  - `operator` (string): Operator being used in selector, optionally apply for operator-specific filtering.
  - `emptyValue` (string): Value to return if selector reduced to blank. Optionally use this to return something
     that could never match, or return something for you to evaluate yourself, like boolean false. (default=blank string)
  - `blacklist` (array): Additional characters you want to disallow. (default=[])
  - `whitelist` (array): Characters that are in default blacklist that you still want to allow. (default=[])
  - `quotelist` (array): Additional characters that should always trigger quoted value. (default=[])
  - If an integer is specified for $options, it is assumed to be the maxLength value.

@return string|int|bool|mixed Value ready to be used as the value component in a selector string.
  Always returns string unless you specify something different for 'emptyValue' option.

## selectorValueAdvanced()

Sanitize selector value for advanced text search operator (#=)

The [advanced text search operator](https://processwire.com/docs/selectors/operators/#contains-advanced)
`#=` supports some characters that are typically excluded from selector values, so this method enables
you to prepare a selector value for use with it. This method should not be used for sanitizing any other
kinds of selector values.

Characters that have meaning to the advanced text search operator include `+-*()"` and thus their
appearance in the `$value` argument is assumed to be a command rather than text to search for. Though
note that non-matching double quotes or parenthesis are removed.

*Note: If double quotes are used in your selector value, this method will convert them to matching
parenthesis, i.e. `+"phrase"` gets converted to `+(phrase)`.*


@param string|array $value

@param array $options See options for Sanitizer::selectorValue() method

@return bool|mixed|string

@since 3.0.182

@see Sanitizer::selectorValue()

@see https://processwire.com/docs/selectors/operators/#contains-advanced

## selectorValueArray()

Wrapper for selectorValueV2() when it receives an array

@param array $value

@param array $options See options for selectorValue()

@return string Always returns string unless you specify something different for 'emptyValue'

## selectorValueV2()

Sanitize selector value (version 2, 3.0.156+)

This version is a little more thorough and has more options than version 1.

@param string|array $value

@param array $options

@return bool|mixed|string Always returns string unless you specify something different for 'emptyValue'

## selectorValueV1()

Sanitize selector value (original, version 1)

@param $value

@param array $options

@return string

## entities()

Entity encode a string for output

Wrapper for PHP's `htmlentities()` function that contains typical ProcessWire usage defaults

The arguments used here are identical to those for
[PHP's htmlentities](http://www.php.net/manual/en/function.htmlentities.php) function,
except that the ProcessWire defaults for encoding quotes and using UTF-8 are already populated.

~~~~~
$test = "ain't <em>nothing</em> perfect but our brokenness";
echo $sanitizer->entities($test);
// result: ain&apos;t &lt;em&gt;nothing&lt;/em&gt; perfect but our brokenness
~~~~~


@param string $str String to entity encode

@param int|bool $flags See PHP htmlentities() function for flags.

@param string $encoding Encoding of string (default="UTF-8").

@param bool $doubleEncode Allow double encode? (default=true).

@return string Entity encoded string

@see Sanitizer::entities1(), Sanitizer::unentities()

## entities1()

Entity encode a string and don’t double encode it if already encoded


@param string $str String to entity encode

@param int|bool $flags See PHP htmlentities() function for flags.

@param string $encoding Encoding of string (default="UTF-8").

@return string Entity encoded string

@see Sanitizer::entities(), Sanitizer::unentities()

## entitiesA()

Entity encode with support for [A]rrays and other non-string values

This is similar to the existing entities() method with the following differences:

- Array values that are strings are encoded recursively to any depth and array is returned.
- Associative array keys (strings) are entity encoded, integer keys are left as-is.
- Objects that implement __toString() are converted to string and entity encoded.
- Objects that do not implement __toString() are converted to a class name.
- If given an int, float, bool, array or string, that is also the type returned.


@param array|string|int|float|object|bool $value

@param int $flags

@param string $encoding

@param bool $doubleEncode

@return array|string|int|float|bool

@since 3.0.194

@see Sanitizer::entitiesA1(), Sanitizer::entities()

## entitiesA1()

Same as entitiesA() but does not double encode


@param array|string|int|float|object|bool $value

@param int $flags

@param string $encoding

@return array|string|int|float|bool

@since 3.0.194

@see Sanitizer::entitiesA(), Sanitizer::entities1()

## entitiesMarkdown()

Entity encode while translating some markdown tags to HTML equivalents

If you specify boolean TRUE for the `$options` argument, full markdown is applied. Otherwise,
only basic markdown allowed, as outlined in the examples.

The primary reason to use this over full-on Markdown is that it has less overhead
and is faster then full-blown Markdown, for when you don't need it. It's also safer
for text coming from user input since it doesn't allow any other HTML. But if you just
want full markdown, then specify TRUE for the `$options` argument.

Basic allowed markdown currently includes:
- `**strong**`
- `*emphasis*`
- `[anchor-text](url)`
- `~~strikethrough~~`
- code surrounded by backticks

~~~~~
// basic markdown
echo $sanitizer->entitiesMarkdown($str);

// full markdown
echo $sanitizer->entitiesMarkdown($str, true);
~~~~~


@param string $str String to apply markdown to

@param array|bool|int $options Options include the following, or specify boolean TRUE to apply full markdown.
 - `fullMarkdown` (bool): Use full markdown rather than basic? (default=false) when true, most options no longer apply.
   Note: A markdown flavor integer may also be supplied for the fullMarkdown option.
 - `flags` (int): PHP htmlentities() flags. Default is ENT_QUOTES.
 - `encoding` (string): PHP encoding type. Default is 'UTF-8'.
 - `doubleEncode` (bool): Whether to double encode (if already encoded). Default is true.
 - `allow` (array): Only markdown that translates to these tags will be allowed. Default is most inline HTML tags.
 - `disallow` (array): Specified tags (in the default allow list) that won't be allowed. Default=[] empty array.
   (Note: The 'disallow' is an alternative to the default 'allow'. No point in using them both.)
 - `linkMarkup` (string): Markup to use for links. Default=`<a href="{url}" rel="nofollow" target="_blank">{text}</a>`.
 - `allowBrackets` (bool): Allow some inline-level bracket tags, i.e. `[span.detail]text[/span]` ? (default=false)

@return string Formatted with a flavor of markdown

## bracketTagsToHtml()

Convert HTML bracket tags [tag]...[/tag] to HTML - helper method for entitiesMarkdown()

@param string $str String containing bracket tags, should be entity encoded ahead of time

@param array $options

@return string

## unentities()

Remove entity encoded characters from a string.

Wrapper for PHP's `html_entity_decode()` function that contains typical ProcessWire usage defaults.

The arguments used here are identical to those for PHP’s (except `$flags` can be boolean true):
[html_entity_decode](http://www.php.net/manual/en/function.html-entity-decode.php) function.

For the `$flags` argument, specify boolean `true` if you want to perform a more comprehensive entity
decode than what PHP does. That will make it convert all UTF-8 entities (including decimal and hex numbered
entities), and it will remove any remaining entity sequences if the could not be converted, ensuring there
are no entities possible in returned value.


@param string $str String to remove entities from

@param int|bool $flags See PHP html_entity_decode function for flags,
  OR specify boolean true to convert all entities and remove any that cannot be converted (since 3.0.105).

@param string $encoding Encoding (default="UTF-8").

@return string String with entities removed.

@see Sanitizer::entities()

## purify()

Purify HTML markup using HTML Purifier

See: [htmlpurifier.org](http://htmlpurifier.org)


@param string $str String to purify

@param array $options See [config options](http://htmlpurifier.org/live/configdoc/plain.html).

@return string Purified markup string.

## purifier()

Return a new HTML Purifier instance

See: [htmlpurifier.org](http://htmlpurifier.org)


@param array $options See [config options](http://htmlpurifier.org/live/configdoc/plain.html).

@return MarkupHTMLPurifier

## removeNewlines()

Remove newlines from the given string and return it


@param string $str String to remove newlines from

@param string $replacement Character to replace newlines with (default=" ")

@return string String without newlines

## removeWhitespace()

Remove or replace all whitespace from string


@param string $str String to remove whitespace from

@param array|string $options Options to modify behavior, or specify string for `replace` option:
 - `replace` (string): Character(s) to replace whitespace with (default='').
 - `collapse` (bool): If using replace, collapse consecutive replace chars to single? (default=true)
 - `trim` (bool): If using replace, trim it from beginning and end? (default=true)
 - `html` (bool): Remove/replace HTML whitespace entities too? (default=true)
 - `allow` (array): Array of whitespace characters that may remain. (default=[])

@return string

@since 3.0.105

## trim()

Trim off all known UTF-8 whitespace types (or given chars) from beginning and ending of string

Like PHP’s trim() but works with multibyte strings and recognizes all types of UTF-8 whitespace
as well as HTML whitespace entities. This method also optionally accepts an array for $chars argument
which enables you to trim out string sequences greater than one character long.

If you do not need an extensive multibyte trim, use PHP’s trim() instead because this takes more overhead.
PHP multibyte support (mb_string) is strongly recommended if using this function.


@param string $str

@param string|array $chars Array or string of chars to trim, or omit (blank string) for all whitespace (includes UTF-8 and HTML-entity whitespace too).

@param string $method Trim method, one of "trim" (both), "rtrim" (right-only) or "ltrim" (left-only). Or just "t", "r", "l" is also fine. 3.0.168+

@return string

@since 3.0.124

## truncate()

Truncate string to given maximum length without breaking words

This method can truncate between words, sentences, punctuation or blocks (like paragraphs).
See the `type` option for details on how it should truncate. By default it truncates between
words. Description of types:

- word: truncate to closest word.
- punctuation: truncate to closest punctuation within sentence.
- sentence: truncate to closest sentence.
- block: truncate to closest block of text (like a paragraph or headline).

Note that if your specified `type` is something other than “word”, and it cannot be matched
within the maxLength, then it will attempt a different type. For instance, if you specify
“sentence” as the type, and it cannot match a sentence, it will try to match to “punctuation”
instead. If it cannot match that, then it will attempt “word”.

HTML will be stripped from returned string. If you want to keep some tags use the `keepTags` or `keepFormatTags`
options to specify what tags are allowed to remain. The `keepFormatTags` option that, when true, will make it
retain all HTML inline text formatting tags.

~~~~~~~
// Truncate string to closest word within 150 characters
$s = $sanitizer->truncate($str, 150);

// Truncate string to closest sentence within 300 characters
$s = $sanitizer->truncate($str, 300, 'sentence');

// Truncate with options
$s = $sanitizer->truncate($str, [
  'type' => 'punctuation',
  'maxLength' => 300,
  'visible' => true,
  'more' => '…'
]);
~~~~~~~


@param string $str String to truncate

@param int|array $maxLength Maximum length of returned string, or specify $options array here.

@param array|string $options Options array, or specify `type` option (string).
 - `type` (string): Preferred truncation type of word, punctuation, sentence, or block. (default='word')
      This is a “preferred type”, not an absolute one, because it will adjust to match what it can within your maxLength.
 - `maxLength` (int): Max characters for truncation, used only if $options array substituted for $maxLength argument.
 - `maximize` (bool): Include as much as possible within specified type and max-length? (default=true)
      If you specify false for the maximize option, it will truncate to first word, puncutation, sentence or block.
 - `visible` (bool): When true, invisible text (markup, entities, etc.) does not count towards string length. (default=false)
 - `trim` (string): Characters to trim from returned string. (default=',;/ ')
 - `noTrim` (string): Never trim these from end of returned string. (default=')]>}”»')
 - `more` (string): Append this to truncated strings that do not end with sentence punctuation. (default='…')
 - `keepTags` (array): HTML tags that should be kept in returned string. (default=[])
 - `keepFormatTags` (bool): Keep HTML text-formatting tags? Simpler alternative to keepTags option. (default=false)
 - `collapseLinesWith` (string): String to collapse lines with where the first is not punctuated. (default=' … ')
 - `convertEntities` (bool): Convert HTML entities to non-entity characters? (default=false)
 - `noEndSentence` (string): Strings that sentence may not end with, space-separated values (default='Mr. Mrs. …')

@return string

@since 3.0.101

## trunc()

Truncate string to given maximum length without breaking words and with no added visible extras

This is a shortcut to the truncate() sanitizer, sanitizing to nearest word with the `more` option
disabled and the `collapseLinesWith` set to 1 space (rather than ellipsis).


@param string $str String to truncate

@param int|array $maxLength Maximum allowed length in characters, or substitute $options argument here

@param array $options See options for truncate() method or specify `type` option (word, punctuation, sentence, block).

@return string

@since 3.0.157

## removeMB4()

Removes 4-byte UTF-8 characters (like emoji) that produce error with with MySQL regular “UTF8” encoding

Returns the same value type that it is given. If given something other than a string or array, it just
returns it without modification.


@param string|array $value String or array containing strings

@param array $options Options to modify behavior, 3.0.169+ only:
 - `replaceWith` (string): Replace MB4+ characters with this character, may not be blank (default='�')
 - `version` (int): Replacement method version (default=2)

@return string|array

## hyphenCase()

Convert string to be all hyphenated-lowercase (aka kabab-case, hyphen-case, dash-case, etc.)

For example, "Hello World" or "helloWorld" becomes "hello-world".


@param string $value

@param array $options
 - `hyphen` (string): Character to use as the hyphen (default='-')
 - `allow` (string): Characters to allow or range of characters to allow, for placement in regex (default='a-z0-9').
 - `allowUnderscore` (bool): Allow underscores? (default=false)

@return string

## kebabCase()

Alias of hyphenCase()


@param string $value

@param array $options See hyphenCase()

@return string

## snakeCase()

Convert string to be all snake_case (lowercase and underscores)

For example, "Hello World" or "hello-world" becomes "hello_world".


@param string $value

@param array $options
 - `allow` (string): Characters to allow or range of characters to allow, for placement in regex (default='a-z0-9').
 - `hyphen` (string): Character to use as the hyphen (default='-')

@return string

## camelCase()

Convert string to be all camelCase

For example, "Hello World" becomes "helloWorld" or "foo-bar-baz" becomes "fooBarBaz".


@param string $value

@param array $options
 - `allow` (string): Characters to allow or range of characters to allow, for placement in regex (default='a-zA-Z0-9').
 - `allowUnderscore` (bool): Allow underscore characters? (default=false)
 - `startLowercase` (bool): Always start return value with lowercase character? (default=true)
 - `startNumber` (bool): Allow return value to begin with a number? (default=false)

@return string

## pascalCase()

Convert string to PascalCase (like camelCase, but first letter always uppercase)

For example, "hello world" becomes "HelloWorld" or "foo-bar-baz" becomes "FooBarBaz".


@param string $value

@param array $options See options for camelCase() method

@return string

## chars()

Sanitize string value to have only the given characters

You must provide a string of allowed characters in the `$allow` argument. If not provided then
the only [ a-z A-Z 0-9 ] are allowed. You may optionally specify `[alpha]` to refer to any
ASCII alphabet character, or `[digit]` to refer to any digit.

~~~~~
echo $sanitizer->chars('foo123barBaz456', 'barz1'); // Outputs: 1baraz
echo $sanitizer->chars('(800) 555-1234', '[digit]', '.');  // Outputs: 800.555.1234
echo $sanitizer->chars('Decatur, GA 30030', '[alpha]', '-'); // Outputs: Decatur-GA
echo $sanitizer->chars('Decatur, GA 30030', '[alpha][digit]', '-'); // Outputs: Decatur-GA-30030
~~~~~


@param string $value Value to sanitize

@param string|array $allow Allowed characters string. If omitted then only alphanumeric [ a-z A-Z 0-9 ] are allowed.
 Use shortcut `[alpha]` to refer to any “a-z A-Z” char or `[digit]` to refer to any digit.

@param string $replacement Replace disallowed chars with this char or string, or omit for blank. (default='')

@param bool $collapse Collapse multiple $replacement chars to one and trim from return value? (default=true)

@param bool|null $mb Specify bool to force use of multibyte on or off, or omit to auto-detect. (default=null)

@return string

@since 3.0.126

## string()

Sanitize value to string

Note that this makes no assumptions about what is a "safe" string, so you should always apply another
sanitizer to it.


@param string|int|array|object|bool|float $value Value to sanitize as string

@param string|null Optional sanitizer method (from this class) to apply to the string before returning

@return string

## date()

Sanitize a date or date/time string, making sure it is valid, and return it

- If no date $format is specified, date will be returned as a unix timestamp.
- If given date in invalid format and can’t be made valid, or date is empty, NULL will be returned.
- If $value is an integer or string of all numbers, it is always assumed to be a unix timestamp.
- If $format and “strict” option specified, date will also validate for format and no out-of-bounds values will be converted.


@param string|int $value Date string or unix timestamp

@param string|null $format Format of date string ($value) in any wireDate(), date() or strftime() format.

@param array $options Options to modify behavior:
 - `returnFormat` (string): wireDate() format to return date in. If not specified, then the $format argument is used.
 - `min` (string|int): Minimum allowed date in $format or unix timestamp format. Null is returned when date is less than this.
 - `max` (string|int): Maximum allowed date in $format or unix timestamp format. Null is returned when date is more than this.
 - `default` (mixed): Default value to return if no value specified.
 - `strict` (bool): Force dates that don’t match given $format, or out of bounds, to fail. Requires $format. (default=false)

@return string|int|null

## textdomain()

Sanitize as language textdomain


@param string $value

@return string

@since 3.0.181

## match()

Validate that given value matches regex pattern.

If given value matches, value is returned. If not, blank is returned.


@param string $value Value to match

@param string $regex PCRE regex pattern (same as you would provide to PHP's `preg_match()`)

@return string Value you supplied if it matches, or blank string if it doesn't

## int()

**********************************************************************************************************************
NUMBER SANITIZERS

## int()

Sanitized an integer (unsigned, unless you specify a negative minimum value)


@param mixed $value Value you want to sanitize as an integer

@param array $options Optionally specify any one or more of the following to modify behavior:
	- `min` (int|null): Minimum allowed value (default=0)
 - `max` (int|null): Maximum allowed value (default=PHP_INT_MAX)
	- `blankValue` (mixed): Value that you want to use when provided value is null or blank string (default=0)

@return int Returns integer, or specified blankValue (which doesn't necessarily have to be an integer)

## intUnsigned()

Sanitize to unsigned (0 or positive) integer

This is an alias to the int() method with default min/max arguments.


@param mixed $value

@param array $options Optionally specify any one or more of the following to modify behavior:
	- `min` (int|null): Minimum allowed value (default=0)
 - `max` (int|null): Maximum allowed value (default=PHP_INT_MAX)
	- `blankValue` (mixed): Value that you want to use when provided value is null or blank string (default=0)

@return int Returns integer, or specified blankValue (which doesn't necessarily have to be an integer)

@return int

## intSigned()

Sanitize to signed integer (negative or positive)


@param mixed $value

@param array $options Optionally specify any one or more of the following to modify behavior:
	- `min` (int|null): Minimum allowed value (default=negative PHP_INT_MAX)
 - `max` (int|null): Maximum allowed value (default=PHP_INT_MAX)
	- `blankValue` (mixed): Value that you want to use when provided value is null or blank string (default=0)

@return int

## range()

Sanitize value to be within the given min and max range

If float or decimal string specified for $min or $max arguments, return value will be a float,
otherwise an integer is returned.

~~~~~
$n = 10;
$sanitizer->range($n, 100, 200); // returns 100
$sanitizer->range($n, 0, 1.0); // returns 1.0
$sanitizer->range($n, 1.1, 100.5); // returns 10.0
~~~~~


@param int|float|string $value

@param int|float|string|null $min Minimum allowed value or null for no minimum (default=null)

@param int|float|string|null $max Maximum allowed value or null for no maximum (default=null)

@return int|float

@since 3.0.125

## min()

Sanitize to have a minimum value

If float or decimal string specified for $min argument, return value will be a float,
otherwise an integer is returned.

~~~~~
$n = 10;
$sanitizer->min(100); // returns 100
$sanitizer->min(5); // returns 10
$sanitizer->min(1.0); // returns 10.0
~~~~~


@param int|float|string $value

@param int|float|string $min Minimum allowed value

@return int|float

@since 3.0.125

@see Sanitizer::max()

## max()

Sanitize to have a maximuim value

If float or decimal string specified for $max argument, return value will be a float,
otherwise an integer is returned.

~~~~~
$n = 10;
$sanitizer->max(5); // returns 5
$sanitizer->max(100); // returns 10
$sanitizer->max(100.0); // returns 10.0
~~~~~


@param int|float|string $value

@param int|float|string $max Maximum allowed value

@return int|float

@since 3.0.125

@see Sanitizer::min()

## float()

Sanitize to floating point value

Values for `getString` argument:

- `false` (bool): do not return string value (default). 3.0.171+
- `true` (bool): locale aware floating point number string. 3.0.171+
- `f` (string): locale aware floating point number string (same as true). 3.0.193+
- `F` (string): non-locale aware floating point number string. 3.0.193+
- `e` (string): lowercase scientific notation (e.g. 1.2e+2). 3.0.193+
- `E` (string): uppercase scientific notation (e.g. 1.2E+2). 3.0.193+


@param float|string|int $value

@param array $options Optionally specify one or more options in an associative array:
	- `precision` (int|null): Optional number of digits to round to (default=null)
	- `mode` (int): Mode to use for rounding precision (default=PHP_ROUND_HALF_UP);
	- `blankValue` (null|int|string|float): Value to return (whether float or non-float) if provided $value is an empty non-float (default=0.0)
	- `min` (float|null): Minimum allowed value, excluding blankValue (default=null)
	- `max` (float|null): Maximum allowed value, excluding blankValue (default=null)
 - `getString (bool|string): Return a string rather than float value? 3.0.171+ (default=false). See value options in method description.

@return float|string

## ___array()

********************************************************************************************************************
ARRAY SANITIZERS

## ___array()

Sanitize array or CSV string to array of values, optionally sanitized by given method

If given a string, delimiter may be pipe ("|"), or comma (","), unless overridden with the `delimiter`
or `delimiters` options.


@param array|string|mixed $value Accepts an array or CSV string.
  If given something else, it becomes first item in array.

@param string|array $sanitizer Sanitizer method to apply to items in the array or omit/null for none,
  or in 3.0.165+ optionally substitute the $options argument here instead (default=null).

@param array $options Optional modifications to default behavior:
	- `maxItems` (int): Maximum items allowed in each array (default=0, which means no limit)
 - `maxDepth` (int): Max nested array depth (default=0, which means no nesting allowed) Since 3.0.160
 - `trim` (bool): Trim whitespace from front/back of each string item in array? (default=true) Since 3.0.190
	- `sanitizer` (string): Optionally specify sanitizer for array values as option rather than argument (default='') Since 3.0.165
	- `keySanitizer` (string): Optionally sanitize associative array keys with this method (default='') Since 3.0.167
	- The following options are only used if the provided $value is a string:
 - `csv` (bool): Allow conversion of delimited string to array? (default=true) Since 3.0.165
	- `delimiter` (string): Single delimiter to use to identify CSV strings. Overrides the 'delimiters' option when specified (default=null)
	- `delimiters` (array): Delimiters to identify CSV strings. First found delimiter will be used, default=array("|", ",")
	- `enclosure` (string): Enclosure to use for CSV strings (default=double quote, i.e. `"`)
	- `escape` (string): Escape to use for CSV strings (default=backslash, i.e. "\\")

@return array

@throws WireException if an unknown $sanitizer method is given

## arrayVal()

Simply sanitize value to array with no conversions

This is the same as the `array()` sanitizer except that it does not attempt to convert
delimited/csv strings to arrays. Meaning, a delimited string would simply become an array
with the first item being that delimited string.


@param mixed $value

@param array $options
	- `maxItems` (int): Maximum items allowed in each array (default=0, which means no limit)
 - `maxDepth` (int): Max nested array depth (default=0, which means no nesting allowed)
	- `sanitizer` (string): Optionally specify sanitizer method name to apply to items (default='')
	- `keySanitizer` (string): Optionally sanitize associative array keys with this method (default='') Since 3.0.167

@return array

@throws WireException

@since 3.0.165

## intArray()

Sanitize array or CSV string to array of unsigned integers (or signed integers if specified $min is less than 0)

If string specified, string delimiter may be comma (","), or pipe ("|"), or you may override with the 'delimiter' option.


@param array|string|mixed $value Accepts an array or CSV string. If given something else, it becomes first value in array.

@param array|bool $options Optional options (see `Sanitizer::array()` and `Sanitizer::int()` methods for options), plus these two:
	- `min` (int): Minimum allowed value (default=0)
	- `max` (int): Maximum allowed value (default=PHP_INT_MAX)
 - `strict` (bool): Remove rather than convert any values that are not all digits or fall outside min/max range? (default=false) Since 3.0.157+
	- `maxItems` (int): Maximum items allowed in each array (default=0, which means no limit)
 - `maxDepth` (int): Max nested array depth (default=0, which means no nesting allowed) Since 3.0.160
 - You may specify boolean true for $options argument to use just the `strict` option. (3.0.157+)
	- The following options are only used if the provided $value is a string:
 - `csv` (bool): Allow conversion of delimited string to array? (default=true) Since 3.0.165
	- `delimiter` (string): Single delimiter to use to identify CSV strings. Overrides the 'delimiters' option when specified (default=null)
	- `delimiters` (array): Delimiters to identify CSV strings. First found delimiter will be used, default=array("|", ",")
	- `enclosure` (string): Enclosure to use for CSV strings (default=double quote, i.e. `"`)

@return array Array of integers

## intArrayVal()

Sanitize array to be all unsigned integers with no conversions

This is the same as the `intArray()` method except for the following:

 - The `csv` delimited string conversion option is disabled by default.
 - The `strict` option default is true, meaning non-integer numbers or those outside allowed range
   are removed rather than converted.


@param array|string|mixed $value Accepts an array or CSV string. If given something else, it becomes first value in array.

@param array|bool $options Options to modify behavior or specify bool for `strict` option:
	- `min` (int): Minimum allowed value (default=0)
	- `max` (int): Maximum allowed value (default=PHP_INT_MAX)
	- `maxItems` (int): Maximum items allowed in each array (default=0, which means no limit)
 - `maxDepth` (int): Max nested array depth (default=0, which means no nesting allowed) Since 3.0.160
 - `strict` (bool): Remove rather than convert any values that are not all digits or fall outside min/max range? (default=true)
    Note that this default for the strict option is different from the one on the intArray() method.

@return array Array of integers

@since 3.0.165

## minArray()

Minimize an array to remove empty values


@param array $data Array to reduce

@param bool|array $allowEmpty Should empty values be allowed in the encoded data? Specify any of the following:
 - `false` (bool): to exclude all empty values (this is the default if not specified).
 - `true` (bool): to allow all empty values to be retained (thus no point in calling this function).
 - Specify array of keys (from data) that should be retained if you want some retained and not others.
 - Specify array of literal empty value types to retain, i.e. [ 0, '0', array(), false, null ]
 - Specify the digit `0` to retain values that are 0, but not other types of empty values.

@param bool $convert Perform type conversions where appropriate? i.e. convert digit-only string to integer (default=false).

@return array

## flatArray()

Given a potentially multi-dimensional array, return a flat 1-dimensional array


@param array $value

@param array $options
 - `preserveKeys` (bool): Preserve associative array keys where possible? (default=false)
 - `maxDepth` (int): Max depth of nested arrays to flatten into value, after which they are discarded (default=0).
    The default value of 0 removes any nested arrays, so specify 1 or higher to include them.

@return array

@since 3.0.160

## wordsArray()

Return array of all words in given value (excluding punctuation and other non-word characters)


@param string|array $value String containing words

@param array $options
 - `keepNumbers` (bool): Keep number-only words in return value? (default=true)
 - `keepNumberFormat` (bool): Keep minus/comma/period in numbers rather than splitting into words? Also requires keepNumbers==true. (default=false)
 - `keepUnderscore` (bool): Keep underscores as part of words? (default=false)
 - `keepHyphen` (bool): Keep hyphenated words? (default=false)
 - `keepApostrophe` (bool): Keep apostrophe as part of words? (default=true) 3.0.168+
 - `keepChars` (array): Specify any of these to also keep as part of words ['.', ',', ';', '/', '*', ':', '+', '<', '>', '_', '-' ] (default=[])
 - `minWordLength` (int): Minimum word length (default=1)
 - `maxWordLength` (int): Maximum word length (default=80)
 - `maxWords` (int): Maximum number of words allowed (default=0, no limit)
 - `stripTags` (bool): Strip markup tags so they don’t contribute to returned word list? (default=true)
 - `truncate` (bool): Truncate rather than remove words that exceed maxWordLength? (default=false) 3.0.250+

@return array

@since 3.0.160

## wordsArrayNumberReplacements()

Identify decimals, minus signs and commas in numbers, replace them, and return the replacements array

@param string $value

@param string $prefix

@return array

## option()

Return $value if it exists in $allowedValues, or null if it doesn't


@param string|int $value

@param array $allowedValues Whitelist of option values that are allowed

@return string|int|null

## options()

Return given values that that also exist in $allowedValues whitelist


@param array $values

@param array $allowedValues Whitelist of option values that are allowed

@return array

## bool()

*************************************************************************************************************************
OTHER SANITIZERS

## bool()

Convert the given value to a boolean

This differs from regular boolean type conversion in the following ways:

- This method will recognize things like the strings "false" or "0" representing a boolean false.
- If given an object, it will convert the object to a string before determining what boolean value it should represent.
- If given an array, it returns false if the array contains zero items.


@param $value

@return bool

## bit()

Sanitize to a bit, returning only integer 0 or 1

This works the same as the bool sanitizer except that it returns 0 or 1 rather than false or true.


@param string|int|array $value

@return int

@see Sanitizer::bool()

@since 3.0.125

## checkbox()

Sanitize checkbox value


@param int|bool|string|mixed|null $value Value to check

@param int|bool|string|mixed|null $yes Value to return if checked (default=true)

@param int|bool|string|mixed|null $no Value to return if not checked (default=false)

@return int|bool|string|mixed|null Return value, based on $checked or $unchecked argument

@since 3.0.128

@see Sanitizer::bool(), Sanitizer::bit()

## maxLength()

Limit length of given value to that specified

- For strings, this limits the length to that many characters.
- For arrays, the maxLength is assumed to be the max allowed array items.
- For integers maxLength is assumed to be the max allowed digits.
- For floats, maxLength is assumed to be max allowed digits (including decimal point).
- Returns the same type it is given: string, array, int or float


@param string|int|array|float $value

@param int $maxLength Maximum length (default=128)

@param null|int $maxBytes Maximum allowed bytes (used for string types only)

@return array|float|int|string

@since 3.0.125

@see Sanitizer::minLength()

## minLength()

Validate or sanitize a string to have a minimum length

If string meets minimum length it is returned as-is.

Note that the default behavior of this function is to validate rather than sanitize the value.
Meaning, it will return blank if the string does not meet the minimum length. Specify the `$padChar`
argument to change that behavior.

If string does not meet minimum length, blank will be returned, unless a `$padChar` is defined in which
case the string will be padded with as many copies of that $padChar are necessary to meet the minimum
length. By default it padds to the right, but you can specify `true` for the `$padLeft` argument to
make it pad to the left instead.

~~~~~~
$value = $sanitizer->minLength('foo'); // returns "foo"
$value = $sanitizer->minLength('foo', 3); // returns "foo"
$value = $sanitizer->minLength('foo', 5); // returns blank string
$value = $sanitizer->minLength('foo', 5, 'o'); // returns "foooo"
$value = $sanitizer->minLength('foo', 5, 'o', true); // returns "oofoo"
~~~~~~


@param string $value Value to enforcer a minimum length for

@param int $minLength Minimum allowed length

@param string $padChar Pad string with this character if it does not meet minimum length (default='')

@param bool $padLeft Pad to left rather than right? (default=false)

@return string

@see Sanitizer::maxLength()

## maxBytes()

Limit bytes used by given string to max specified

- This function will not break multibyte characters so long as PHP has mb_string.
- This function works only with strings and if given a non-string it will be converted to one.


@param string $value

@param int $maxBytes

@return string

@since 3.0.125

## ___testAll()

Run value through all sanitizers, return array indexed by sanitizer name and resulting value

Used for debugging and testing purposes.


@param mixed $value

@return array

## getAll()

Get all sanitizer method names and optionally types they return


@param bool $getReturnTypes Get array where method names are keys and values are return types?

@return array

@since 3.0.165

## getTextTools()

Get instance of WireTextTools


@return WireTextTools

@since 3.0.101

## getNumberTools()

Get instance of WireNumberTools


@return WireNumberTools

@since 3.0.214

## validateFile()

*******************************************************************************************************************
FILE VALIDATORS

## validateFile()

Validate and sanitize a file using FileValidator modules

This is intended for validating file data, not file names. Depending on the FileValidator
modules that are used, they may sanitize the file in order ot make it valid.

IMPORTANT: This method returns NULL if it can’t find a validator for the file. This does
not mean the file is invalid, just that it didn't have the tools to validate it. If the
getArray option is specified then it would return a blank array rather than null.

**getArray option** (3.0.167+):
When specifying true for the `getArray` option this method will return an associative array
of validation results indexed by module name. The values for each module name will be either
true (file validates as-is), 1 (file valid after it was sanitized), or false (file not valid
and cannot be sanitized). A blank array is returned if no modules could perform the validation.

**dryrun option** (3.0.167+):
When specifying true for the `dryrun` option please note that no validation is performed and
instead the method returns true or false as to whether or not the file can be validated. It
only looks at the file extension, so the file need not exist. Meaning it’s also okay to specify
filename like “test.jpg” without path, when using this option. If using the dryrun option with
the `getArray` option then it will return an array of module names that would perform the
validation for the given file type (or blank array if none).


@param string $filename Full path and filename to validate

@param array $options When available, provide array with any one or all of the following:
 - `page` (Page): Page object associated with $filename. (default=null)
 - `field` (Field): Field object associated with $filename. (default=null)
 - `pagefile` (Pagefile): Pagefile object associated with $filename. (default=null)
 - `getArray` (bool): Return array of results rather than a boolean? (default=false) Added 3.0.167
 - `dryrun` (bool|int): Specify true to only return if the file can be validated with this method,
    without actually performing any validation. (default=false). Added 3.0.167

@return bool|array|null Returns one of the following, depending on use of dryrun and getArray options:
 - Boolean true if valid, false if not.
 - NULL if no validator available for given file type or file does not exist.
 - If dryrun option is used, returns boolean (or array of strings if getArray option is true).
 - If getArray option is used, returns associative array of results or blank array if no validators.

## __toString()

*******************************************************************************************************************
CLASS HELPERS

## sanitize()

Call a sanitizer method indirectly where method name can contain combined/combo methods

This method is primarily here to support predefined sanitizers in strings, like those that might
be specified in settings for a module or field. For regular use, you probably want to call the
sanitizer methods directly rather than through this method.

~~~~~
// sanitize with text then entities sanitizers
$value = $sanitizer->sanitize($value, 'text,entities');

// numbers appended to text sanitizers imply max length
$value = $sanitizer->sanitize($value, 'text128,entities');
~~~~~


@param mixed $value

@param string $method Method name "method", or combined method name(s) "method1,method2,method3"

@return string|int|array|float|null

@since 3.0.125

## validate()

Validate that value remains unchanged by given sanitizer method, or return null if not

If change is just a type conversion change or surrounding whitespace (that gets trimmed)
then this is still considered valid.

Returns NULL or given $fallback value if value does not validate. Note that if results like
0, false or blank string are considered valid values, then this method can return them. So for
cases like that you should compare the return value with NULL (or whatever your $fallback is).

things like 0 or false (if that is a valid value) compare the return value with null before
assuming a value is not valid.


~~~~~
$sanitizer->validate('abc', 'alpha'); // valid: returns 'abc'
$sanitizer->validate('abc123', 'alpha'); invalid: returns null
~~~~~

@param string|int|array|float $value Value to validate

@param string $method Saniatizer method name or CSV names combo

@param null|mixed mixed $fallback Optionally return this fallback value (rather than null) if value does not validate

@return null|mixed Returns sanitized value if it validates or null (or given fallback) if value does not validate

@since 3.0.125

## valid()

Is given value valid? (i.e. unchanged by given sanitizer method)

~~~~~~
if($sanitizer->valid('abc123', 'alphanumeric')) {
 // value is valid
}
~~~~~~


@param string|int|array|float $value Value to check if valid

@param string $method Method name or CSV method names

@param bool $strict When true, sanitized value must be identical in type to the one given

@return bool

@since 3.0.125
