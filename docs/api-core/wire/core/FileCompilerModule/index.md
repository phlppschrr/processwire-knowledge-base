# FileCompilerModule

Source: `wire/core/FileCompilerModule.php`

Inherits: `WireData`
Implements: `Module`, `ConfigurableModule`

## Summary

ProcessWire File Compiler base module

Common methods:
- [`init()`](method-init.md)
- [`compile()`](method-compile.md)
- [`compileMarkup()`](method-compilemarkup.md)
- [`install()`](method-___install.md)
- [`uninstall()`](method-___uninstall.md)

Groups:
Group: [other](group-other.md)

Provides the base class for FileCompiler modules

FileCompiler modules must use the name format: FileCompiler[Name].module
For example, FileCompilerTags.module


This file is licensed under the MIT license
https://processwire.com/about/license/mit/

## Methods
- [`init()`](method-init.md) Optional method to initialize the module.
- [`compile(string $data): string|array`](method-compile.md) The compile method processes the contents of a file
- [`compileMarkup(string $data): string`](method-compilemarkup.md) Compile a section of markup
- [`install()`](method-___install.md) (hookable) Perform any installation procedures specific to this module, if needed.
- [`uninstall()`](method-___uninstall.md) (hookable) Perform any uninstall procedures specific to this module, if needed.
- [`getSourceFile(): string`](method-getsourcefile.md) Get the source file (full path and filename) that this module is acting upon
- [`getModuleConfigInputfields(InputfieldWrapper $inputfields)`](method-getmoduleconfiginputfields.md) Configure the FileCompiler module
