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
- [`__construct()`](method-__construct.md) Construct
- [`getSelectorInfo(Field $field): array`](method-getselectorinfo.md) Return array with information about what properties and operators can be used with this field
- [`getSelectorInfoTemplate(): array`](method-getselectorinfotemplate.md) Return the default selector info template array
- [`getOperators(string $inputType = ''): array`](method-getoperators.md) Get array of operators
- [`getOperatorLabels(): array`](method-getoperatorlabels.md) Get array of operators mapped to text labels
