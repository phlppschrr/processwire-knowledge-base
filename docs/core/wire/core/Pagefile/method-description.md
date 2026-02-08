# $pagefile->description($language = null, $value = null): string|array

Source: `wire/core/Pagefile.php`

Get or set the file’s description (with multi-language support).

When not in a multi-language environment, you can still use this method but we recommend using the simpler method of just
getting/seting the `Pagefile::$description` property directly instead.

## Example

~~~~~
// Get a Pagefile to work with
$pagefile = $page->files->first();

// Setting description
$pagefile->description('en', 'Setting English description');
$pagefile->description('de', 'Setting German description');

// Getting description for current language (whatever it happens to be)
echo $pagefile->description();

// Getting description for language "de"
echo $pagefile->description('de');
~~~~~

## Usage

~~~~~
// basic usage
$string = $pagefile->description();

// usage with all arguments
$string = $pagefile->description($language = null, $value = null);
~~~~~

## Arguments

- null|bool|Language|array - To GET in current user language: Omit arguments or specify null. - To GET in another language: Specify a Language name, id or object. - To GET in all languages as a JSON string: Specify boolean true (if LanguageSupport not installed, regular string returned). - To GET in all languages as an array indexed by language name: Specify boolean true for both arguments. - To SET for a language: Specify a language name, id or object, plus the $value as the 2nd argument. - To SET in all languages as a JSON string: Specify boolean true, plus the JSON string $value as the 2nd argument (internal use only). - To SET in all languages as an array: Specify the array here, indexed by language ID or name, and omit 2nd argument.
- `$value` (optional) `null|string` Specify only when you are setting (single language) rather than getting a value.

## Return value

- `string|array`
