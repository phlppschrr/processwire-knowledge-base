# $languages->getDefault(): Language

Source: `wire/modules/LanguageSupport/Languages.php`

Get the default language

The default language can also be accessed from property `$languages->default`.

~~~~~
if($user->language->id == $languages->getDefault()->id) {
  // user has the default language
}
~~~~~

## Return value

Language

## Throws

- WireException when default language hasn't yet been set
