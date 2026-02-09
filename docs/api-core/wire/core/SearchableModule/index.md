# SearchableModule

Source: `wire/core/Module.php`

Interface SearchableModule

Interface for modules that implement a method and expected array return value
for completing basic text searches (primarily for admin search engine).

It is optional to add this interface to "implements" section of the module class definition.
However, you must specify a "searchable: name" property in your getModuleInfo() method in
order for ProcessWire to recognize the module is searchable. See below for more info:

~~~~~~
public static function getModuleInfo() {
  return array(
    'searchable' => 'name',

    // You'll need the above 'searchable' property returned by your getModuleInfo().
    // The value of 'name' should be the name by which search results should be referred to
    // if the user wants to limit the search to this module. For instance, if your module
    // was called “ProcessWidgets”, you’d probably choose the name “widgets” for this.
    // If the module represents an API variable, the name should be the same as the API variable.
    // ...
  );
}
~~~~~

Methods:
- [`search(string $text, array $options = array()): array`](method-search.md) Search for items containing $text and return an array representation of them
