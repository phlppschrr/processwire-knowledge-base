# InputfieldTinyMCEConfigs

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCEConfigs.php`

Inherits: `InputfieldTinyMCEClass`

InputfieldTinyMCEConfigHelper

Helper for managing configuration settings in TinyMCE

Methods:
- [`label(string $name): string`](method-label.md) Get shared text label
- [`getMceToolbars(bool $splitToArray = true): array|string[]`](method-getmcetoolbars.md) Get TinyMCE toolbar names and details
- [`getSkinOptions(): string[]`](method-getskinoptions.md) Get skin options (array of name => label)
- [`getContentCssOptions(): string[]`](method-getcontentcssoptions.md) Get content_css options (array of name=label)
- [`getFeaturesOptions(): array[]`](method-getfeaturesoptions.md) Get features options
- [`getConfigInputfields(InputfieldWrapper $inputfields): InputfieldFieldset`](method-getconfiginputfields.md) Get field configuration
- [`getModuleConfigInputfields(InputfieldWrapper $inputfields)`](method-getmoduleconfiginputfields.md) Module configuration
- [`getOtherTinyMCEFields(): array`](method-getothertinymcefields.md) Get other textarea fields that are using TinyMCE
- [`configStyleFormatsCSS(): InputfieldTextarea`](method-configstyleformatscss.md)
- [`addPlugin(string $file)`](method-addplugin.md) Add an external plugin .js file
- [`removePlugin(string $file): bool`](method-removeplugin.md) Remove an external plugin .js file
- [`ckeToMceToolbar(string $value): string`](method-cketomcetoolbar.md) Convert CKE toolbar to MCE (future use)
