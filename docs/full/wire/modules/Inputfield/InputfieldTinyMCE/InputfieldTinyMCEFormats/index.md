# InputfieldTinyMCEFormats

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCEFormats.php`

Inherits: `InputfieldTinyMCEClass`

InputfieldTinyMCEFormats

Helper for managing TinyMCE style_formats and related settings

Methods:
- [`getBlockFormats(): string`](method-getblockformats.md) Get block_formats
- [`getStyleFormats(array $defaults): array|mixed`](method-getstyleformats.md) Get style_formats
- [`mergeStyleFormats(array $styleFormats, array $addFormats): array`](method-mergestyleformats.md) Merge the given style formats
- [`applyStyleFormatsCSS(string $css, array &$settings, array $defaults)`](method-applystyleformatscss.md) Add CSS that converts to style_formats and content_style
- [`applyRemoveStyleFormats(array $styleFormats): array`](method-applyremovestyleformats.md) Remove style formats that have a 'remove=true' property
- [`getInvalidStyles(string|array $value, array|string $defaultValue, bool $merge = false): array|string`](method-getinvalidstyles.md) Get TinyMCE "invalid_styles" setting and prepare as array value
- [`invalidStylesStrToArray(string $value, array $a = array()): array`](method-invalidstylesstrtoarray.md) Convert invalid_styles string to array
- [`invalidStylesArrayToStr(array $a): string`](method-invalidstylesarraytostr.md) Convert invalid_styles array to string
