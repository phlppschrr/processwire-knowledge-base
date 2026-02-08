# $wireTextTools->findReplaceEscapeChars(&$str, array $escapeChars, array $options = array()): array

Source: `wire/core/WireTextTools.php`

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

## Arguments

- string &$str String to find escape chars in, it will be modified directly (passed by reference)
- array $escapeChars Array of chars you want to escape i.e. [ '*', '[', ']', '(', ')', '`', '_', '\\', '"' ]
- array $options Options to modify behavior: - `escapePrefix` (string): Character used to escape another character (default is backslash). - `restoreEscape` (bool): Should returned array also include the escape prefix, so escapes are restored? (default=false) - `gluePrefix` (string): Prefix for placeholders we substitute for escaped characters (default='{ESC') - `glueSuffix` (string): Suffix for placeholders we substitute for escaped characters (default='}') - `unescapeUnknown` (bool): If we come across escaped char not in your $escapeChars list, unescape it? (default=false) - `removeUnknown` (bool): If we come across escaped char not in your $escapeChars list, remove the escape and char? (default=false)

## Return value

array Returns assoc array where keys are placeholders substituted in $str and values are escaped characters.

## Meta

- @since 3.0.162
