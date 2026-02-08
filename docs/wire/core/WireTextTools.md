# WireTextTools

Source: `wire/core/WireTextTools.php`

ProcessWire Text Tools

Specific text and markup tools for ProcessWire $sanitizer and elsewhere.

ProcessWire 3.x, Copyright 2020 by Ryan Cramer
https://processwire.com

@since 3.0.101

## __construct()

Construct

## markupToText()

Convert HTML markup to readable text

Like PHP’s strip_tags but with some small improvements in HTML-to-text conversion that
improves the readability of the text.

In 3.0.197+ inner content of script, style and object tags is now removed, rather than just the tags.
To revert this behavior or to remove content of additional tags, see the `clearTags` option.

Note that this method differs from the `Sanitizer::markupToText()` method in that this method is newer,
more powerful and has more options. But the two methods differ in how they perform markup-to-text
conversion so you may want to review and try both to determine which one better suits your needs.

@param string $str String to convert to text

@param array $options
 - `keepTags` (array): Tag names to keep in returned value, i.e. [ "em", "strong" ]. (default=none)
 - `clearTags` (array): Tags that should also have their content cleared. (default=[ "script", "style", "object" ]) Since 3.0.197
 - `splitBlocks` (string): String to split paragraph and header elements. (default="\n\n")
 - `convertEntities` (bool): Convert HTML entities to plain text equivalents? (default=true)
 - `listItemPrefix` (string): Prefix for converted list item `<li>` elements. (default='• ')
 - `linksToUrls` (bool): Convert links to `(url)` rather than removing? (default=true) Since 3.0.132
 - `linksToMarkdown` (bool): Convert links to `[text](url)` rather than removing? (default=false) Since 3.0.197
 - `uppercaseHeadlines` (bool): Convert headline tags to uppercase? (default=false) Since 3.0.132
 - `underlineHeadlines` (bool): Underline headlines with "=" or "-"? (default=true) Since 3.0.132
 - `collapseSpaces` (bool): Collapse extra/redundant extra spaces to single space? (default=true) Since 3.0.132
 - `replacements` (array): Associative array of strings to manually replace. (default=['&nbsp;' => ' '])

@return string

@see Sanitizer::markupToText()

## fixUnclosedTags()

Remove (or close) unclosed HTML tags from given string

Remove unclosed tags:
---------------------
At present, if it finds an unclosed tag, it removes all tags of the same kind.
This is in order to keep the function fast, by delegating what it can to strip_tags().
This is sufficient for our internal use here, but may not be ideal for all situations.

Fix/close unclosed tags:
------------------------
When the remove option is false, it will attempt to close unclosed tags rather than
remove them. It doesn't know exactly where they should be closed, so it appends the
close tags to the end of the string.

@param string $str

@param bool $remove Remove unclosed tags? If false, it will attempt to close them instead. (default=true)

@param array $options
 - `ignoreTags` (array): Tags that can be ignored because they close themselves. (default=per HTML spec)

@return string

## collapse()

Collapse string to plain text that all exists on a single long line without destroying words/punctuation.

@param string $str String to collapse

@param array $options
 - `stripTags` (bool): Strip markup tags? (default=true)
 - `keepTags` (array): Array of tag names to keep, if stripTags==true. (default=[])
 - `collapseLinesWith` (string): String to collapse newlines with. (default=' ')
 - `linksToUrls` (bool): Convert links to "(url)" rather than removing entirely? (default=false) Since 3.0.132
 - `endBlocksWith` (string): Character or string to insert to identify paragraph/header separation (default='')
 - `convertEntities` (bool): Convert entity-encoded characters to text? (default=true)

@return string

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

## truncateSentenceTests()

Helper to truncate() method, generate tests/positions for where sentences end

@param string $str

@param array $tests Tests to append found positions to

@param array $endSentenceChars

@param array $options Options provided to truncate method

## getVisibleLength()

Return visible length of string, which is length not counting markup or entities

@param string $str

@return int

## getPunctuationChars()

Get array of punctuation characters

@param bool $sentence Get only sentence-ending punctuation

@return array

## getWordAlternates()

Get alternate words for given word

This method does not do anything unless an implementation is provided by a module (or something else)
hooking the protected `WireTextTools::wordAlternates($word, $options)` method. Implementation should
populate $event->return with any or all of the following (as available):

- Word plural(s)
- Word singular(s)
- Word Lemmas
- Word Synonyms
- Anything else applicable to current $user->language

See the protected WireTextTools::wordAlternates() method for hook instructions and an example.

@param string $word

@param array $options
 - `operator` (string): Operator being used, if applicable (default='')
 - `minLength` (int): Minimum word length to return in alternates (default=2)
 - `lowercase` (bool): Convert words to lowercase, if not already (default=false)

@return array

@since 3.0.162

@see WireTextTools::getWordStem()

## ___wordAlternates()

Hookable method to return alternate words for given word

This hookable method is separate from the public getWordAlternates() method so that
we can provide predictable and already-populated $options to whatever is hooking this, as
as provide some additional QA with the return value from modules/hooks.

It is fine if the return value contains duplicates, the original word, or too-short words,
as the calling getWordAlternates() takes care of those before returning words to user.
Basically, hooks can ignore the `$options` argument, unless they need to know the `operator`,
which may or may not be provided by the caller.

In hook implementation, avoid deleting what’s already present in $event->return just in
case multiple hooks are adding words.

~~~~~
// Contrived example of how to implement
$wire->addHookAfter('WireTextTools::wordAlternates', function(HookEvent $event) {
  $word = $event->arguments(0); // string: word requested alternates for
  $words = $event->return; // array: existing return value

  $cats = [ 'cat', 'cats', 'kitty', 'feline', 'felines' ];
  $dogs = [ 'dog', 'dogs', 'doggy', 'canine', 'canines' ];

  if(in_array($word, $cats)) {
    $words = array_merge($words, $cats);
  } else if(in_array($word, $dogs)) {
    $words = array_merge($words, $dogs);
  }

  $event->return = $words;
});

// Test it out
$words = $sanitizer->getTextTools()->getWordAlternates('cat');
echo implode(', ', $words); // outputs: cats, kitty, kitten, feline, felines
~~~~~


@param string $word

@param array $options
 - `operator` (string): Operator being used, if applicable (default='')

@return array

@since 3.0.162

## findPlaceholders()

Find and return all {placeholder} tags found in given string

@param string $str String that might contain field {tags}

@param array $options
 - `has` (bool): Specify true to only return true or false if it has tags (default=false).
	- `tagOpen` (string): The required opening tag character(s), default is '{'
	- `tagClose` (string): The required closing tag character(s), default is '}'

@return array|bool Always returns array unless you specify the `has` option as true.

@since 3.0.126

## hasPlaceholders()

Does the string have any {placeholder} tags in it?

@param string $str

@param array $options
	- `tagOpen` (string): The required opening tag character(s), default is '{'
	- `tagClose` (string): The required closing tag character(s), default is '}'

@return bool

@since 3.0.126

## populatePlaceholders()

Given a string ($str) and values ($vars), populate placeholder “{tags}” in the string with the values

- The `$vars` should be an associative array of `[ 'tag' => 'value' ]`.
- The `$vars` may also be an object, in which case values will be pulled as properties of the object.

By default, tags are specified in the format: {first_name} where first_name is the name of the
variable to pull from $vars, `{` is the opening tag character, and `}` is the closing tag char.

The tag parser can also handle subfields and OR tags, if `$vars` is an object that supports that.
For instance `{products.title}` is a subfield, and `{first_name|title|name}` is an OR tag.

~~~~~
$vars = [ 'foo' => 'FOO!', 'bar' => 'BAR!' ];
$str = 'This is a test: {foo}, and this is another test: {bar}';
echo $sanitizer->getTextTools()->populatePlaceholders($str, $vars);
// outputs: This is a test: FOO!, and this is another test: BAR!
~~~~~

@param string $str The string to operate on (where the {tags} might be found)

@param WireData|object|array $vars Object or associative array to pull replacement values from.

@param array $options Array of optional changes to default behavior, including:
	- `tagOpen` (string): The required opening tag character(s), default is '{'
 - `tagClose` (string): The optional closing tag character(s), default is '}'
 - `recursive` (bool): If replacement value contains tags, populate those too? (default=false)
 - `removeNullTags` (bool): If a tag resolves to a NULL (i.e. field not present), remove it? (default=true)
 - `removeEmptyTags` (bool): If a tag value resolves to blank string, false or NULL, remove it? (default=true) 3.0.237+
 - `entityEncode` (bool): Entity encode the values pulled from $vars? (default=false)
 - `entityDecode` (bool): Entity decode the values pulled from $vars? (default=false)
 - `allowMarkup` (bool): Allow markup to appear in populated variables? (default=true)

@return string String with tags populated.

@since 3.0.126 Use wirePopulateStringTags() function for older versions

## diffArray()

Given two arrays, return array of the changes with 'ins' and 'del' keys

Based upon Paul Butler’s Simple Diff Algorithm v0.1 © 2007 (zlib/libpng) https://paulbutler.org

@param array $oldArray

@param array $newArray

@return array

@since 3.0.144

## diffMarkup()

Given two strings ($old and $new) return a diff string in HTML markup

@param string $old Old string value

@param string $new New string value

@param array $options Options to modify behavior:
 - `ins` (string) Markup to use for diff insertions (default: `<ins>{out}</ins>`)
 - `del` (string) Markup to use for diff deletions (default: `<del>{out}</del>`)
 - `entityEncode` (bool): Entity encode values, other than added ins/del tags? (default=true)
 - `split` (string): Regex used to split strings for parts to diff (default=`\s+`)

@return string

@since 3.0.144

## findReplaceEscapeChars()

Find escaped characters in $str, replace them with a placeholder, and return the placeholders

Usage
~~~~~
// 1. Escape certain chars in a string that you want to survive some processing:
$str = 'Hello \*world\* foo \"bar\" baz';

// 2. Use this method to find escape chars and replace them temporarily:
$a = $sanitizer->getTextTools()->findReplaceEscapeChars($str, [ '*', '"' ]);

// 3. Process string with anything that you want NOT to see chars that were escaped:
$str = some_function_that_processes_the_string($str);

// 4. Do this to restore the escaped chars (restored without backslashes by default):
$str = str_replace(array_keys($a), array_values($a), $str);
~~~~~

@param string &$str String to find escape chars in, it will be modified directly (passed by reference)

@param array $escapeChars Array of chars you want to escape i.e. [ '*', '[', ']', '(', ')', '`', '_', '\\', '"' ]

@param array $options Options to modify behavior:
 - `escapePrefix` (string): Character used to escape another character (default is backslash).
 - `restoreEscape` (bool): Should returned array also include the escape prefix, so escapes are restored? (default=false)
 - `gluePrefix` (string): Prefix for placeholders we substitute for escaped characters (default='{ESC')
 - `glueSuffix` (string): Suffix for placeholders we substitute for escaped characters (default='}')
 - `unescapeUnknown` (bool): If we come across escaped char not in your $escapeChars list, unescape it? (default=false)
 - `removeUnknown` (bool): If we come across escaped char not in your $escapeChars list, remove the escape and char? (default=false)

@return array Returns assoc array where keys are placeholders substituted in $str and values are escaped characters.

@since 3.0.162

## substr()

********************************************************************************************************
MULTIBYTE PHP STRING FUNCTIONS THAT FALLBACK WHEN MBSTRING NOT AVAILABLE

These duplicate the equivalent PHP string methods and use exactly the same arguments
and exhibit exactly the same behavior. The only difference is that these methods using
the multibyte string versions when they are available, and fallback to the regular PHP
string methods when not. Use these functions only when that behavior is okay.

## substr()

Get part of a string


@param string $str

@param int $start

@param int|null $length Max chars to use from str. If omitted or NULL, extract all characters to the end of the string.

@return string

@see https://www.php.net/manual/en/function.substr.php

## strpos()

Find position of first occurrence of string in a string


@param string $haystack

@param string $needle

@param int $offset

@return bool|false|int

@see https://www.php.net/manual/en/function.strpos.php

## stripos()

Find the position of the first occurrence of a case-insensitive substring in a string


@param string $haystack

@param string $needle

@param int $offset

@return bool|false|int

@see https://www.php.net/manual/en/function.stripos.php

## strrpos()

Find the position of the last occurrence of a substring in a string


@param string $haystack

@param string $needle

@param int $offset

@return bool|false|int

@see https://www.php.net/manual/en/function.strrpos.php

## strripos()

Find the position of the last occurrence of a case-insensitive substring in a string


@param string $haystack

@param string $needle

@param int $offset

@return bool|false|int

@see https://www.php.net/manual/en/function.strripos.php

## strlen()

Get string length


@param string $str

@return int

@see https://www.php.net/manual/en/function.strlen.php

## strtolower()

Make a string lowercase


@param string $str

@return string

@see https://www.php.net/manual/en/function.strtolower.php

## strtoupper()

Make a string uppercase


@param string $str

@return string

@see https://www.php.net/manual/en/function.strtoupper.php

## substrCount()

Count the number of substring occurrences


@param string $haystack

@param string $needle

@return int

@see https://www.php.net/manual/en/function.substr-count.php

## strstr()

Find the first occurrence of a string


@param string $haystack

@param string $needle

@param bool $beforeNeedle Return part of haystack before first occurrence of the needle? (default=false)

@return false|string

@see https://www.php.net/manual/en/function.strstr.php

## stristr()

Find the first occurrence of a string (case insensitive)


@param string $haystack

@param string $needle

@param bool $beforeNeedle Return part of haystack before first occurrence of the needle? (default=false)

@return false|string

@see https://www.php.net/manual/en/function.stristr.php

## strrchr()

Find the last occurrence of a character in a string


@param string $haystack

@param string $needle Only first given character used

@return false|string

@see https://www.php.net/manual/en/function.strrchr.php

## trim()

Strip whitespace (or other characters) from the beginning and end of a string


@param string $str

@param string $chars Omit for default

@return string

## ltrim()

Strip whitespace (or other characters) from the beginning of string only (aka left trim)


@param string $str

@param string $chars Omit for default

@return string

@since 3.0.168

## rtrim()

Strip whitespace (or other characters) from the end of string only (aka right trim)


@param string $str

@param string $chars Omit for default

@return string

@since 3.0.168
