# $wireTextTools->collapse($str, array $options = array()): string

Source: `wire/core/WireTextTools.php`

Collapse string to plain text that all exists on a single long line without destroying words/punctuation.

## Arguments

- string $str String to collapse
- array $options - `stripTags` (bool): Strip markup tags? (default=true) - `keepTags` (array): Array of tag names to keep, if stripTags==true. (default=[]) - `collapseLinesWith` (string): String to collapse newlines with. (default=' ') - `linksToUrls` (bool): Convert links to "(url)" rather than removing entirely? (default=false) Since 3.0.132 - `endBlocksWith` (string): Character or string to insert to identify paragraph/header separation (default='') - `convertEntities` (bool): Convert entity-encoded characters to text? (default=true)

## Return value

string
