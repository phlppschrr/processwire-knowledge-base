# Languages

Source: `wire/modules/LanguageSupport/Languages.php`

Inherits: `PagesType`

## Summary

ProcessWire Languages (plural) Class

Common methods:
- [`translator()`](method-translator.md)
- [`getPageClass()`](method-getpageclass.md)
- [`getLoadOptions()`](method-getloadoptions.md)
- [`getJoinFieldNames()`](method-getjoinfieldnames.md)
- [`getAll()`](method-getall.md)

Groups:
Group: [other](group-other.md)

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

## Methods
- [`__construct(ProcessWire $wire, array $templates = array(), array $parents = array())`](method-__construct.md) Construct
- [`translator(Language $language): LanguageTranslator`](method-translator.md) Return the LanguageTranslator instance for the given language
- [`findOther(string|Language $selector = '', Language|null $excludeLanguage = null): PageArray`](method-findother.md) Find and return all languages except current user language
- [`findNonDefault(string $selector = ''): PageArray`](method-findnondefault.md) Find and return all languages except default language
- [`getDefault(): Language`](method-getdefault.md) Get the default language
- [`setDefault(?Language $language = null): void`](method-setdefault.md) Set current user to have default language temporarily
- [`unsetDefault(): void`](method-unsetdefault.md) Restores whatever previous language a user had prior to a setDefault() call
- [`setLanguage(int|string|Language $language): bool`](method-setlanguage.md) Set the current user language for the current request
- [`getLanguage(string|int $name = ''): Language|null`](method-getlanguage.md) Get the current language or optionally a specific named language
- [`unsetLanguage(): bool`](method-unsetlanguage.md) Undo a previous setLanguage() call, restoring the previous user language
- [`setLocale(int|string|array|null|Language $category = LC_ALL, int|string|array|null|Language $locale = null): string|bool`](method-setlocale.md) Set the current locale
- [`getLocale(int|Language|string|null $category = LC_ALL, Language|string|int|null $language = null): string|bool`](method-getlocale.md) Return the current locale setting
- [`deleted(Page $language)`](method-___deleted.md) (hookable) Hook called when a language is deleted
- [`added(Page $language)`](method-___added.md) (hookable) Hook called when a language is added
- [`updated(Page $language, string $what)`](method-___updated.md) (hookable) Hook called when a language is added or deleted
- [`pageNames(): LanguageSupportPageNames|false`](method-pagenames.md) Get LanguageSupportPageNames module if installed, false if not
- [`hasPageNames(): bool`](method-haspagenames.md) Is LanguageSupportPageNames installed?
- [`editable(Language|int|string $language): bool`](method-editable.md) Does current user have edit access for page fields in given language?
- [`importTranslationsFile(Language|string $language, string $file, bool $quiet = false): bool|int`](method-importtranslationsfile.md) Import a language translations file
