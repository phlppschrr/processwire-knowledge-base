# $wireTextTools->truncate($str, $maxLength, $options = array()): string

Source: `wire/core/WireTextTools.php`

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

## Example

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

## Usage

~~~~~
// basic usage
$string = $wireTextTools->truncate($str, $maxLength);

// usage with all arguments
$string = $wireTextTools->truncate($str, $maxLength, $options = array());
~~~~~

## Arguments

- `$str` `string` String to truncate
- `$maxLength` `int|array` Maximum length of returned string, or specify $options array here.
- `$options` (optional) `array|string` Options array, or specify `type` option (string). - `type` (string): Preferred truncation type of word, punctuation, sentence, or block. (default='word') This is a “preferred type”, not an absolute one, because it will adjust to match what it can within your maxLength. - `maxLength` (int): Max characters for truncation, used only if $options array substituted for $maxLength argument. - `maximize` (bool): Include as much as possible within specified type and max-length? (default=true) If you specify false for the maximize option, it will truncate to first word, puncutation, sentence or block. - `visible` (bool): When true, invisible text (markup, entities, etc.) does not count towards string length. (default=false) - `trim` (string): Characters to trim from returned string. (default=',;/ ') - `noTrim` (string): Never trim these from end of returned string. (default=')]>}”»') - `more` (string): Append this to truncated strings that do not end with sentence punctuation. (default='…') - `keepTags` (array): HTML tags that should be kept in returned string. (default=[]) - `keepFormatTags` (bool): Keep HTML text-formatting tags? Simpler alternative to keepTags option. (default=false) - `collapseLinesWith` (string): String to collapse lines with where the first is not punctuated. (default=' … ') - `convertEntities` (bool): Convert HTML entities to non-entity characters? (default=false) - `noEndSentence` (string): Strings that sentence may not end with, space-separated values (default='Mr. Mrs. …')

## Return value

- `string`
