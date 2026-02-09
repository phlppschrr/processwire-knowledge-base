# ModuleConfig

Source: `wire/core/ModuleConfig.php`

Inherits: `WireData`

ModuleConfig class

Serves as the base for classes dedicated to configuring modules.

Descending class name should follow the format: [ModuleName]Config and file [ModuleName]Config.php
located in the same directory as the module it is configuring.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Methods:
- [`__construct()`](method-__construct.md)
- [`getDefaults(): array`](method-getdefaults.md)
- [`getInputfields(): InputfieldWrapper`](method-getinputfields.md)
- [`add(array $a): self`](method-add.md)
- [`identifyDefaults(array $a): array`](method-identifydefaults.md)
