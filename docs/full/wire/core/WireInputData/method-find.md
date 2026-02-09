# $wireInputData->find($pattern, array $options = array()): array

Source: `wire/core/WireInputData.php`

Find all input vars that match given pattern in name (or optionally value)

$values = [

## Example

~~~~~
// find all input vars having name beginning with "title_" (i.e. title_en, title_de, title_es)
$values = $input->post->find('title_*');

// find all input vars having name with "title" anywhere in it (i.e. title, subtitle, titles, title_de)
$values = $input->post->find('*title*');

// find all input vars having value with the term "wire" anywhere, regardless of case
$values = $input->post->find('/wire/i', [ 'type' => 'value' ]);

// example of result from above find operation:

```php

```
  'title' => 'ProcessWire CMS',
  'subtitle' => 'Have plenty of caffeine to make sure you are wired',
  'sidebar' => 'Learn how to rewire a flux capacitor...',
  'summary' => 'All about the $wire API variable',
];
~~~~~

## Usage

~~~~~
// basic usage
$array = $wireInputData->find($pattern);

// usage with all arguments
$array = $wireInputData->find($pattern, array $options = array());
~~~~~

## Arguments

- `$pattern` `string` Wildcard string or PCRE regular expression
- `$options` (optional) `array` - `type` (string): Specify "value" to match input value (rather input name), OR prefix pattern with "value=". - `limit` (int): Maximum number of items to return (default=0, no limit) - `sanitizer` (string): Name of sanitizer to run values through (default='', none) - `arrays` (bool): Also find on input varibles that are arrays? (default=false)

## Return value

- `array` Returns associative array of values `[ name => value ]` if found, or empty array if none found.

## Since

3.0.163
