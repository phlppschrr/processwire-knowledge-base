# InputfieldPageListSelectCommon

Source: `wire/modules/Inputfield/InputfieldPageListSelect/InputfieldPageListSelectCommon.php`

## Summary

Common methods for InputfieldPageListSelect and InputfieldPageListSelectMultiple

Common methods:
- [`pageListReady()`](method-pagelistready.md)
- [`renderMarkupValue()`](method-rendermarkupvalue.md)
- [`getPageLabel()`](method-getpagelabel.md)
- [`renderParentError()`](method-renderparenterror.md)

@since 3.0.231

## Methods
- [`pageListReady(string $name, string $labelFieldName)`](method-pagelistready.md) Render ready
- [`renderMarkupValue(int|int[] $value): string`](method-rendermarkupvalue.md) Render markup value for PageListSelect/PageListSelectMultiple
- [`getPageLabel(Page $page): string`](method-getpagelabel.md) Get label to represent given `$page`
- [`renderParentError(): string`](method-renderparenterror.md) Render an error message that a parent ID is missing in field settings
