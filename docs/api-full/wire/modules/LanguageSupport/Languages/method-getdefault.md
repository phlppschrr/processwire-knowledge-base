# $languages->getDefault(): Language

Source: `wire/modules/LanguageSupport/Languages.php`

Get the default language

The default language can also be accessed from property `$languages->default`.

## Example

~~~~~
if($user->language->id == $languages->getDefault()->id) {
  // user has the default language
}
~~~~~

## Usage

~~~~~
// basic usage
$language = $languages->getDefault();
~~~~~

## Return value

- `Language`

## Exceptions

- `WireException` when default language hasn't yet been set
