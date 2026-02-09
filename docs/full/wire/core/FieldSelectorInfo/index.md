# FieldSelectorInfo

Source: `wire/core/FieldSelectorInfo.php`

Inherits: `Wire`

Class that provides information about selectors for Fieldtypes

This is primarily a helper for the base Fieldtype class getSelectorInfo method

This originated with the InputfieldSelector module and the need for Fieldtypes to
provide information about what properties can be selected, what operators, are used,
and so on. In the future this class will likely come in handy in providing selector
validation and improved help and error messaging when building/testing selectors.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Methods:
- [`__construct()`](method-__construct.md)
- [`getSelectorInfo(Field $field): array`](method-getselectorinfo.md)
- [`getSelectorInfoTemplate(): array`](method-getselectorinfotemplate.md)
- [`getOperators(string $inputType = ''): array`](method-getoperators.md)
- [`getOperatorLabels(): array`](method-getoperatorlabels.md)
