# FileCompilerModule

Source: `wire/core/FileCompilerModule.php`

ProcessWire File Compiler base module

Provides the base class for FileCompiler modules

FileCompiler modules must use the name format: FileCompiler[Name].module
For example, FileCompilerTags.module

ProcessWire 3.x, Copyright 2016 by Ryan Cramer
https://processwire.com

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

## other

@property int $runOrder Order that the module executes in relative to other FileCompiler modules.

## init()

Optional method to initialize the module.

This is called after ProcessWire's API is fully ready for use and hooks

## compile()

The compile method processes the contents of a file

1. If you want to compile the entire contents of the file, override this method and don't parent::compile().
2. If you only want to compile non-PHP sections of the file, implement the compileMarkup() method instead.

@param string $data

@return string|array

## compileMarkup()

Compile a section of markup

@param string $data

@return string

## ___install()

Perform any installation procedures specific to this module, if needed.

## ___uninstall()

Perform any uninstall procedures specific to this module, if needed.

## getSourceFile()

Get the source file (full path and filename) that this module is acting upon

@return string

## getModuleConfigInputfields()

Configure the FileCompiler module

@param InputfieldWrapper $inputfields
