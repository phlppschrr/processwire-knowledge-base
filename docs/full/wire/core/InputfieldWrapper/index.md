# InputfieldWrapper

Source: `wire/core/InputfieldWrapper.php`

Inherits: `Inputfield`
Implements: `Countable`, `IteratorAggregate`


Groups:
Group: [manipulation](group-manipulation.md)
Group: [output](group-output.md)
Group: [properties](group-properties.md)

ProcessWire InputfieldWrapper


About InputfieldWrapper
=======================
A type of Inputfield that is designed specifically to wrap other Inputfields.
The most common example of an InputfieldWrapper is a <form>.

A type of Inputfield that contains other Inputfield objects as children. Commonly a form or a fieldset.

InputfieldWrapper is not designed to render an Inputfield specifically, but you can set a value attribute
containing content that will be rendered before the wrapper.

Methods:
- [`__construct()`](method-__construct.md)
- [`wired()`](method-wired.md)
- [`get(string $key): Inputfield|mixed`](method-get.md)
- [`__get(string $key): mixed|null`](method-__get.md)
- [`add(Inputfield|array|string $item): Inputfield|InputfieldWrapper|$this`](method-add.md)
- [`new(string $typeName, string|array $name = '', string|array $label = '', array|string $settings = array()): Inputfield|InputfieldSelect|InputfieldWrapper`](method-___new.md) (hookable)
- [`import(InputfieldWrapper|array|InputfieldsArray $items): $this`](method-import.md)
- [`prepend(Inputfield $item): $this`](method-prepend.md)
- [`append(Inputfield $item): $this`](method-append.md)
- [`insert(Inputfield|array|string $item, Inputfield|string $existingItem, bool $before = false): $this`](method-insert.md)
- [`insertBefore(Inputfield|array|string $item, Inputfield|string $existingItem): $this`](method-insertbefore.md)
- [`insertAfter(Inputfield|array|string $item, Inputfield|string $existingItem): $this`](method-insertafter.md)
- [`remove(Inputfield|string $key): $this`](method-remove.md)
- [`removeByName(string $name): Inputfield|null`](method-removebyname.md)
- [`preRenderChildren()`](method-prerenderchildren.md)
- [`classParents(Inputfield|string $inputfield): array`](method-classparents.md)
- [`render(): string`](method-___render.md) (hookable)
- [`setAttributeInMarkup(string $name, string $value, string $markup, bool $removeEmpty = false): string`](method-setattributeinmarkup.md)
- [`removeAttributeFromMarkup(string $name, string $markup): string`](method-removeattributefrommarkup.md)
- [`renderHeaderActions(Inputfield $inputfield, array $actions): string`](method-renderheaderactions.md)
- [`renderValue(): string`](method-___rendervalue.md) (hookable)
- [`renderInputfield(Inputfield $inputfield, bool $renderValueMode = false): string`](method-___renderinputfield.md) (hookable)
- [`renderInputfieldAjaxPlaceholder(Inputfield $inputfield, bool $renderValueMode): string`](method-renderinputfieldajaxplaceholder.md)
- [`processInput(WireInputData $input): $this`](method-___processinput.md) (hookable)
- [`isEmpty(): bool`](method-isempty.md)
- [`getErrors(bool $clear = false): array`](method-geterrors.md)
- [`getErrorInputfields(): array|Inputfield[]`](method-geterrorinputfields.md)
- [`children(string $selector = ''): InputfieldsArray`](method-children.md)
- [`child(string|int $name = '', bool $recursive = true): Inputfield|null`](method-child.md)
- [`find(string $selector): InputfieldsArray`](method-find.md)
- [`getChildByName(string $name): Inputfield|InputfieldWrapper|null`](method-getchildbyname.md)
- [`getByName(string $name): Inputfield|InputfieldWrapper|null`](method-getbyname.md)
- [`getByAttr(string $attrName, string $attrValue): Inputfield|InputfieldWrapper|null`](method-getbyattr.md)
- [`getByField(Field|string|int $field): Inputfield|InputfieldWrapper|null`](method-getbyfield.md)
- [`getByProperty(string $property, mixed $value, bool $getAll = false): Inputfield|InputfieldWrapper|null|array`](method-getbyproperty.md)
- [`getValueByName(string $name): array|float|int|object|Wire|WireArray|WireData|string|null`](method-getvaluebyname.md)
- [`getIterator(): InputfieldsArray`](method-getiterator.md)
- [`count(): int`](method-count.md)
- [`getAll(array $options = array()): InputfieldsArray`](method-getall.md)
- [`getConfigInputfields(): InputfieldWrapper`](method-___getconfiginputfields.md) (hookable)
- [`importArray(array $a, ?InputfieldWrapper $inputfields = null): $this`](method-importarray.md)
- [`populateValues(WireData|Wire|ConfigurableModule|array $data): array`](method-populatevalues.md)
