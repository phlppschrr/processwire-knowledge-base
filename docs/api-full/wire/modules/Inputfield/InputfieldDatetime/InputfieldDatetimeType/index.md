# InputfieldDatetimeType

Source: `wire/modules/Inputfield/InputfieldDatetime/InputfieldDatetimeType.php`

Inherits: `WireData`

## Summary

Common methods:
- [`getTypeName()`](method-gettypename.md)
- [`getTypeLabel()`](method-gettypelabel.md)
- [`getAttribute()`](method-getattribute.md)
- [`setAttribute()`](method-setattribute.md)
- [`getSetting()`](method-getsetting.md)

## Methods
- [`__construct(InputfieldDatetime $inputfield)`](method-__construct.md) Construct
- [`getTypeName(): string`](method-gettypename.md) Get name for this type
- [`getTypeLabel(): string`](method-gettypelabel.md) Get type label
- [`getAttribute(string $key): string|null`](method-getattribute.md) Get attribute
- [`setAttribute(string $key, string $value): self`](method-setattribute.md) Get attribute
- [`getSetting(string $key): mixed`](method-getsetting.md) Get setting
- [`get(string $key): mixed|null`](method-get.md) Get setting or attribute or API var
- [`getDefaultSettings(): array`](method-getdefaultsettings.md) Get array of default settings
- [`renderValue(): string`](method-rendervalue.md)
- [`sanitizeValue(string|int $value): int|string`](method-sanitizevalue.md) Sanitize value to unix timestamp integer or blank string (to represent no value)
- [`renderReady()`](method-renderready.md) Render ready
- [`render(): string`](method-render.md)
- [`processInput(WireInputData $input): int|string|bool`](method-processinput.md) Process input
- [`getConfigInputfields(InputfieldWrapper $inputfields)`](method-getconfiginputfields.md)
