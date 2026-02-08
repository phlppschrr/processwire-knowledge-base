# Predefined module types in ProcessWire

Source: https://processwire.com/docs/modules/types/

## Summary

This page looks at the different predefined types of modules in ProcessWire and what they do. It also provides the recommended naming prefixes for modules so that ProcessWire can recognize your module type without actually loading it.

## Key Points

- This page looks at the different predefined types of modules in ProcessWire and what they do. It also provides the recommended naming prefixes for modules so that ProcessWire can recognize your module type without actually loading it.
- ProcessWire comes with a base Module interface for implementing any kind of plugin, as well as a few abstract and base objects for predefined module types that can be extended to create a module of that type. Common examples of predefined module types in ProcessWire include:
- When creating new modules that fall in this category of predefined types, the module type must be used as a prefix in the class name, as a means of identification. For instance, if you create a new Textformatter module called "Something" you should name it "TextformatterSomething". Likewise, a new Inputfield module called "SuperCheckbox" should be named "InputfieldSuperCheckbox". For the module types mentioned above, ProcessWire will not recognize them as a module of that type unless they contain the correct prefix. For modules that aren't based on these existing types, you don't need to consider naming conventions. However, we recommend the following:

## Sections


### Naming conventions

When creating new modules that fall in this category of predefined types, the module type must be used as a prefix in the class name, as a means of identification. For instance, if you create a new Textformatter module called "Something" you should name it "TextformatterSomething". Likewise, a new Inputfield module called "SuperCheckbox" should be named "InputfieldSuperCheckbox". For the module types mentioned above, ProcessWire will not recognize them as a module of that type unless they contain the correct prefix. For modules that aren't based on these existing types, you don't need to consider naming conventions. However, we recommend the following:
