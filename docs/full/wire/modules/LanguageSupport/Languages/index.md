# Languages

Source: `wire/modules/LanguageSupport/Languages.php`

Inherits: `PagesType`


Groups:
Group: [other](group-other.md)

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

Methods:
- [`__construct(ProcessWire $wire, array $templates = array(), array $parents = array())`](method-__construct.md)
- [`translator(Language $language): LanguageTranslator`](method-translator.md)
- [`findOther(string|Language $selector = '', Language|null $excludeLanguage = null): PageArray`](method-findother.md)
- [`findNonDefault(string $selector = ''): PageArray`](method-findnondefault.md)
- [`getDefault(): Language`](method-getdefault.md)
- [`setDefault(?Language $language = null): void`](method-setdefault.md)
- [`unsetDefault(): void`](method-unsetdefault.md)
- [`setLanguage(int|string|Language $language): bool`](method-setlanguage.md)
- [`getLanguage(string|int $name = ''): Language|null`](method-getlanguage.md)
- [`unsetLanguage(): bool`](method-unsetlanguage.md)
- [`setLocale(int|string|array|null|Language $category = LC_ALL, int|string|array|null|Language $locale = null): string|bool`](method-setlocale.md)
- [`getLocale(int|Language|string|null $category = LC_ALL, Language|string|int|null $language = null): string|bool`](method-getlocale.md)
- [`deleted(Page $language)`](method-___deleted.md) (hookable)
- [`added(Page $language)`](method-___added.md) (hookable)
- [`updated(Page $language, string $what)`](method-___updated.md) (hookable)
- [`pageNames(): LanguageSupportPageNames|false`](method-pagenames.md)
- [`hasPageNames(): bool`](method-haspagenames.md)
- [`editable(Language|int|string $language): bool`](method-editable.md)
- [`importTranslationsFile(Language|string $language, string $file, bool $quiet = false): bool|int`](method-importtranslationsfile.md)
