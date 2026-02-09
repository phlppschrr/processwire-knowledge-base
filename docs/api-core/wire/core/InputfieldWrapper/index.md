# InputfieldWrapper

Source: `wire/core/InputfieldWrapper.php`

Inherits: `Inputfield`
Implements: `Countable`, `IteratorAggregate`

## Summary

ProcessWire InputfieldWrapper

Common methods:
- [`wired()`](method-wired.md)
- [`get()`](method-get.md)
- [`add()`](method-add.md)
- [`new()`](method-___new.md)
- [`import()`](method-import.md)

Groups:
Group: [manipulation](group-manipulation.md)
Group: [output](group-output.md)
Group: [properties](group-properties.md)

## About Inputfieldwrapper
A type of Inputfield that is designed specifically to wrap other Inputfields.
The most common example of an InputfieldWrapper is a <form>.

A type of Inputfield that contains other Inputfield objects as children. Commonly a form or a fieldset.

InputfieldWrapper is not designed to render an Inputfield specifically, but you can set a value attribute
containing content that will be rendered before the wrapper.

## Methods
- [`__construct()`](method-__construct.md) Construct the Inputfield, setting defaults for all properties
- [`wired()`](method-wired.md) Wired to API
- [`get(string $key): Inputfield|mixed`](method-get.md) Get a child Inputfield having a name attribute matching the given `$key`.
- [`__get(string $key): mixed|null`](method-__get.md) Provides direct reference to attributes and settings, and falls back to Inputfield children
- [`add(Inputfield|array|string $item): Inputfield|InputfieldWrapper|$this`](method-add.md) Add an Inputfield item as a child (also accepts array definition)
- [`new(string $typeName, string|array $name = '', string|array $label = '', array|string $settings = array()): Inputfield|InputfieldSelect|InputfieldWrapper`](method-___new.md) (hookable) Create a new Inputfield, add it to this InputfieldWrapper, and return the new Inputfield
- [`import(InputfieldWrapper|array|InputfieldsArray $items): $this`](method-import.md) Import the given Inputfield items as children
- [`prepend(Inputfield $item): $this`](method-prepend.md) Prepend an Inputfield to this instance’s children.
- [`append(Inputfield $item): $this`](method-append.md) Append an Inputfield to this instance’s children.
- [`insert(Inputfield|array|string $item, Inputfield|string $existingItem, bool $before = false): $this`](method-insert.md) Insert new or existing Inputfield before or after another
- [`insertBefore(Inputfield|array|string $item, Inputfield|string $existingItem): $this`](method-insertbefore.md) Insert one Inputfield before one that’s already there.
- [`insertAfter(Inputfield|array|string $item, Inputfield|string $existingItem): $this`](method-insertafter.md) Insert one Inputfield after one that’s already there.
- [`remove(Inputfield|string $key): $this`](method-remove.md) Remove an Inputfield from this instance’s children.
- [`removeByName(string $name): Inputfield|null`](method-removebyname.md) Remove an Inputfield from the form by name
- [`preRenderChildren()`](method-prerenderchildren.md) Prepare children for rendering by creating any fieldset groups
- [`classParents(Inputfield|string $inputfield): array`](method-classparents.md) Get array of parent Inputfield classes for given Inputfield (excluding the base Inputfield class)
- [`render(): string`](method-___render.md) (hookable) Render this Inputfield and the output of its children.
- [`setAttributeInMarkup(string $name, string $value, string $markup, bool $removeEmpty = false): string`](method-setattributeinmarkup.md) Set attribute value in markup, optionally replacing a {placeholder} tag
- [`removeAttributeFromMarkup(string $name, string $markup): string`](method-removeattributefrommarkup.md) Remove named attribute from given markup
- [`renderHeaderActions(Inputfield $inputfield, array $actions): string`](method-renderheaderactions.md) Render Inputfield header actions
- [`renderValue(): string`](method-___rendervalue.md) (hookable) Render the output of this Inputfield and its children, showing values only (no inputs)
- [`renderInputfield(Inputfield $inputfield, bool $renderValueMode = false): string`](method-___renderinputfield.md) (hookable) Render output for an individual Inputfield
- [`renderInputfieldAjaxPlaceholder(Inputfield $inputfield, bool $renderValueMode): string`](method-renderinputfieldajaxplaceholder.md) Render a placeholder for an ajax-loaded Inputfield
- [`processInput(WireInputData $input): $this`](method-___processinput.md) (hookable) Process input for all children
- [`isEmpty(): bool`](method-isempty.md) Returns true if all children are empty, or false if one or more is populated
- [`getErrors(bool $clear = false): array`](method-geterrors.md) Return an array of errors that occurred on any of the children during input processing.
- [`getErrorInputfields(): array|Inputfield[]`](method-geterrorinputfields.md) Get Inputfield objects that have errors
- [`children(string $selector = ''): InputfieldsArray`](method-children.md) Return all children Inputfield objects
- [`child(string|int $name = '', bool $recursive = true): Inputfield|null`](method-child.md) Find an Inputfield below this one that has the given name
- [`find(string $selector): InputfieldsArray`](method-find.md) Find all children Inputfields matching a selector string
- [`getChildByName(string $name): Inputfield|InputfieldWrapper|null`](method-getchildbyname.md) Given an Inputfield name, return the child Inputfield or NULL if not found.
- [`getByName(string $name): Inputfield|InputfieldWrapper|null`](method-getbyname.md) Shorter alias of getChildByName()
- [`getByAttr(string $attrName, string $attrValue): Inputfield|InputfieldWrapper|null`](method-getbyattr.md) Given an attribute name and value, return the first matching Inputfield or null if not found
- [`getByField(Field|string|int $field): Inputfield|InputfieldWrapper|null`](method-getbyfield.md) Get Inputfield by Field (hasField)
- [`getByProperty(string $property, mixed $value, bool $getAll = false): Inputfield|InputfieldWrapper|null|array`](method-getbyproperty.md) Get Inputfield by some other non-attribute property or setting
- [`getValueByName(string $name): array|float|int|object|Wire|WireArray|WireData|string|null`](method-getvaluebyname.md) Get value of Inputfield by name
- [`getIterator(): InputfieldsArray`](method-getiterator.md) Enables foreach() of the children of this class
- [`count(): int`](method-count.md) Return the quantity of children present
- [`getAll(array $options = array()): InputfieldsArray`](method-getall.md) Get all Inputfields below this recursively in a flat InputfieldWrapper (children, and their children, etc.)
- [`getConfigInputfields(): InputfieldWrapper`](method-___getconfiginputfields.md) (hookable) Get configuration Inputfields for this InputfieldWrapper
- [`importArray(array $a, ?InputfieldWrapper $inputfields = null): $this`](method-importarray.md) Import an array of Inputfield definitions to to this InputfieldWrapper instance
- [`populateValues(WireData|Wire|ConfigurableModule|array $data): array`](method-populatevalues.md) Populate values for all Inputfields in this wrapper from the given `$data` object or array.
