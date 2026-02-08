# Languages

Source: `wire/modules/LanguageSupport/Languages.php`

ProcessWire Languages (plural) Class

API variable $languages enables access to all Language pages and various helper methods.
The $languages API variable is most commonly used for iteration of all installed languages.
~~~~~
foreach($languages as $language) {
  echo "<li>$language->title ($language->name) ";
  if($language->id == $user->language->id) {
    echo "current"; // the user's current language
  }
  echo "</li>";
}
~~~~~


ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [translator()](method-translator.md)
Method: [findOther()](method-findother.md)
Method: [findNonDefault()](method-findnondefault.md)
Method: [getDefault()](method-getdefault.md)
Method: [setDefault()](method-setdefault.md)
Method: [unsetDefault()](method-unsetdefault.md)
Method: [setLanguage()](method-setlanguage.md)
Method: [getLanguage()](method-getlanguage.md)
Method: [unsetLanguage()](method-unsetlanguage.md)
Method: [setLocale()](method-setlocale.md)
Method: [getLocale()](method-getlocale.md)
Method: [deleted()](method-___deleted.md) (hookable)
Method: [added()](method-___added.md) (hookable)
Method: [updated()](method-___updated.md) (hookable)
Method: [pageNames()](method-pagenames.md)
Method: [hasPageNames()](method-haspagenames.md)
Method: [editable()](method-editable.md)
Method: [importTranslationsFile()](method-importtranslationsfile.md)
