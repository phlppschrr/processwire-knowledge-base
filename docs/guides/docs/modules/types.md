# ProcessWire module types

Source: https://processwire.com/docs/modules/types/

## Summary

This page looks at the different predefined types of modules in ProcessWire and what they do. It also provides the recommended naming prefixes for modules so that ProcessWire can recognize your module type without actually loading it.

## Key Points

- [Fieldtype](/api/ref/fieldtype/) for defining field types.
- [Inputfield](/api/ref/inputfield/) for defining types of form input fields.
- [Process](/api/ref/process/) for creating admin processes/applications.
- [Textformatter](/api/ref/textformatter/) for formatting text.
- [AdminTheme](/api/ref/admin-theme-framework/) for creating themes in the admin.

## Sections


## Predefined module types in ProcessWire

This page looks at the different predefined types of modules in ProcessWire and what they do. It also provides the recommended naming prefixes for modules so that ProcessWire can recognize your module type without actually loading it.

ProcessWire comes with a base [Module interface](/api/ref/module/) for implementing any kind of plugin, as well as a few abstract and base objects for predefined module types that can be extended to create a module of that type. Common examples of predefined module types in ProcessWire include:

- [Fieldtype](/api/ref/fieldtype/) for defining field types.
- [Inputfield](/api/ref/inputfield/) for defining types of form input fields.
- [Process](/api/ref/process/) for creating admin processes/applications.
- [Textformatter](/api/ref/textformatter/) for formatting text.
- [AdminTheme](/api/ref/admin-theme-framework/) for creating themes in the admin.
- [WireMail](/api/ref/wire-mail/) for modules that send email and extend the *WireMail* class.
- [Tfa](/api/ref/tfa/) for implementing a specific kind of two-factor authentication.
- [ImageSizerEngine](/api/ref/image-sizer-engine/) for modules that extend *ImageSizerEngine* for resizing images.
- [FileCompiler](/api/ref/file-compiler-module/) for modules that extend *FileCompilerModule* for compilation of files.
- [FileValidator](/api/ref/file-validator-module/) for modules that extend *FileValidatorModule* for validation of files.


### Naming conventions

When creating new modules that fall in this category of predefined types, the module type must be used as a prefix in the class name, as a means of identification. For instance, if you create a new Textformatter module called "Something" you should name it "TextformatterSomething". Likewise, a new Inputfield module called "SuperCheckbox" should be named "InputfieldSuperCheckbox". For the module types mentioned above, ProcessWire will not recognize them as a module of that type unless they contain the correct prefix. For modules that aren't based on these existing types, you don't need to consider naming conventions. However, we recommend the following:

- Use the prefix **Markup** for modules that are used primarily for markup generation.
- Use the prefix **Session** for modules that focus primarily on sessions.
- Use the prefix **Jquery** (case intended) for modules that represent a jQuery plugin.
- Use the prefix **LanguageSupport** for modules that provide multi-language features and don't match an existing predefined type.

Outside of these module types and naming conventions, you are welcome to use whatever name you'd like when developing a module.
