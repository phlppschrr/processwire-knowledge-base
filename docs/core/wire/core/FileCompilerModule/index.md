# FileCompilerModule

Source: `wire/core/FileCompilerModule.php`

Inherits: `WireData`
Implements: `Module`, `ConfigurableModule`


Groups:
Group: [other](group-other.md)

ProcessWire File Compiler base module

Provides the base class for FileCompiler modules

FileCompiler modules must use the name format: FileCompiler[Name].module
For example, FileCompilerTags.module


This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Methods:
- [`init()`](method-init.md)
- [`compile(string $data): string|array`](method-compile.md)
- [`compileMarkup(string $data): string`](method-compilemarkup.md)
- [`install()`](method-___install.md) (hookable)
- [`uninstall()`](method-___uninstall.md) (hookable)
- [`getSourceFile(): string`](method-getsourcefile.md)
- [`getModuleConfigInputfields(InputfieldWrapper $inputfields)`](method-getmoduleconfiginputfields.md)
