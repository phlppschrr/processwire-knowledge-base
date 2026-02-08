# ProcessWire PHP Coding Style Guide v1.0

Source: https://processwire.com/docs/more/coding-style-guide/

## Summary

This PHP style guide represents the coding style preferred for the ProcessWire core.

## Key Points

- Make string constants translatable for multi-language support.*

## Sections


## ProcessWire PHP Coding Style Guide v1.0

This PHP style guide represents the coding style preferred for the ProcessWire core.

It is also recommended (though certainly not required) for 3rd party modules and other code using the ProcessWire API, unless an existing coding standard is already in place or preferred. Use of this coding standard is however requested for code submissions (pull requests) to the ProcessWire core.

The ProcessWire coding style guide is based on [PSR-1](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-1-basic-coding-standard.md) and [PSR-2](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-2-coding-style-guide.md) (with many sections copied directly from them), but with several important differences and additions. Read more in our [Introduction to the ProcessWire Coding Style Guide](https://processwire.com/blog/posts/processwire-2.7.1-dev-coding-style-guide/#style-guide-intro).


### Table of Contents

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).


## 1. Overview


### 1.1. Summary

**An asterisk is appended to lines that vary significantly from the PSR style guides.*

- Make string constants translatable for multi-language support.*


### 1.2. Example

This example encompasses some of the rules below as a quick overview:

```php
<?php

/**
 * Class Sample
 *
 * Description of what the class does.
 *
 * @method int hookableMethod($a, $b)
 *
 */
class Sample extends WireData implements Module {

    /**
     * Description of sampleConstant
     *
     */
    const sampleConstant = 1;

    /**
     * Description of sampleProperty
     *
     * @var bool
     *
     */
    protected $sampleProperty = true;

    /**
     * Description of sampleFunction
     *
     * @param int $a Description of a
     * @param int|null $b Description of b
     *
     */
    public function sampleFunction($a, $b = null) {
        if($a === $b) {
            bar();
        } else if($a > $b) {
            $foo->bar($arg1);
        } else {
            BazClass::bar($arg2, $arg3);
        }
    }

    /**
     * Description of hookableMethod
     *
     * @param int $a Description of a
     * @param int $b Description of b
     * @return string Description of return value
     *
     */
    public function ___hookableMethod($a, $b) {
        $result = $a + $b;
        return sprintf($this->_('The result is %s'), $result);
    }
}
```


## 2. General


### 2.1. Files


### 2.2. Lines

- There SHOULD NOT be more than one statement per line.


### 2.3. Indentation, Tabs, Spaces

*For conversion purposes: when spaces are present instead of tabs, each group of 4-consecutive spaces at the beginning of a line will be assumed to be a tab, for spaces-to-tabs conversion.*


### 2.4. Keywords and True/False/Null


## 3. Namespaces


### 3.1. Using Namespaces

When namespaces are used (like with ProcessWire 3.x), the following are RECOMMENDED:

- When present, `use` declarations go after the namespace declaration, with one `use` keyword per declaration, and a blank line after the block of `use` declarations.

For example:

```php
<?php namespace SampleNamespace;

use FooClass;
use BarClass as Bar;
use OtherVendor\OtherPackage\BazClass;

// ... additional PHP code ...
```


## 4. Classes, Properties, and Methods


### 4.1. Class and Interface Declarations

```
/**
 * Class SampleClass
 *
 * Description of SampleClass
 *
 */
 class SampleClass {
   // ...
 }
```


### 4.2. Constants

```
class Foo {

    /**
     * Current version number
     *
     */
    const version = '1.0';

    /**
     * Default approval date
     *
     */
    const dateApproved = '2012-06-01';
}
```


### 4.3. Extends and Implements

The `extends` and `implements` keywords MUST be declared on the same line as the class name.

```
class ClassName extends ParentClass implements SomeInterface {
    // constants, properties, methods
}
```

Lists of `implements` MAY be split across multiple lines, where each subsequent line is indented once. When doing so, the first item in the list MUST be on the next line, and there MUST be only one interface per line.

```
class ClassName extends ParentClass implements
    InterfaceA,
    InterfaceB,
    InterfaceC {
```


### 4.4. Properties

```
class ClassName {

    /**
     * Description of foo
     *
     * @var int|null
     *
     */
    protected $foo = null;
}
```


### 4.5. Properties and magic methods

This refers to class properties that are pulled from the `__get($key)` magic method, or set by the `__set($key, $value)` magic method. For example, properties in a `WireData` class in ProcessWire.

When possible, these properties SHOULD be documented with PHPDoc in the class declaration. Use `@property` for read/write properties, `@property-read` for read-only properties, and `@property-write` for write-only properties.

```
/**
 * Class SampleClass
 *
 * Description of SampleClass
 *
 * @property int $propertyA Description of read/write propertyA
 * @property-read bool $propertyB Description of read-only propertyB
 * @property-write string $propertyC Description of write-only propertyC
 *
 */
class SampleClass {
  // ...
}
```


### 4.6. Methods

```
/**
 * Description of fooBarBaz
 *
 * @param int $arg1 Description of arg1
 * @param int $arg2 Description of arg2
 *
 */
public function fooBarBaz($arg1, $arg2) {
    // method body
}
```


### 4.7. Method Arguments

```
public function foo($arg1, &$arg2, $arg3 = true) {
    // method body
}
```

Argument lists MAY be split across multiple lines, where each subsequent line is indented once. When doing so, the first item in the list MUST be on the next line, and there MUST be only one argument per line.

When the argument list is split across multiple lines, the closing parenthesis and opening brace SHOULD be placed together on the last argument line, and the method body SHOULD begin with a blank line.

```
public function aVeryLongMethodName(
    ClassTypeHint $arg1,
    &$arg2,
    array $arg3 = array()) {

    // method body
}
```


### 4.8. Hookable Methods and Arguments (ProcessWire only)

```
/**
 * Class SampleClass
 *
 * Description of SampleClass
 *
 * @method int fooBarBaz(int $arg1, int $arg2) Add two integers
 *
 */
class SampleClass extends Wire {

    /**
     * Description of fooBarBaz
     *
     * @param int $arg1 Description of arg1
     * @param int $arg2 Description of arg2
     * @return int
     *
     */
    public function ___fooBarBaz($arg1, $arg2) {
        return $arg1 + $arg2;
    }
}
```


### 4.9. abstract, final, and static

```
abstract class ClassName {

    protected static $foo = null;

    abstract protected function zim();

    final public static function bar() {
        // method body
    }
}
```


### 4.10. Method and Function Calls

When making a method or function call, there MUST NOT be a space between the method or function name and the opening parenthesis, there MUST NOT be a space after the opening parenthesis, and there MUST NOT be a space before the closing parenthesis. In the argument list, there MUST NOT be a space before each comma, and there MUST be one space after each comma.

```
bar();
$foo->bar($arg1);
Foo::bar($arg2, $arg3);
```

Argument lists MAY be split across multiple lines, where each subsequent line is indented once. When doing so, the first item in the list MUST be on the next line, and there MUST be only one argument per line.

```
$foo->bar(
    $longArgument,
    $longerArgument,
    $muchLongerArgument
);
```


## 5. Control Structures

The general style rules for control structures are as follows:

- There MUST NOT be whitespace after the control structure keyword
- There MUST NOT be a space after the opening parenthesis
- There MUST NOT be a space before the closing parenthesis
- There MUST be one space between the closing parenthesis and the opening brace
- The structure body MUST be indented once
- The closing brace MUST be on the next line after the body

The body of each structure SHOULD be enclosed by braces. The braces MAY be omitted if the structure exists on a single line of 80 characters or less.


### 5.1. if, elseif, else

An `if` structure looks like the following. Note the placement of parentheses, spaces, and braces.

```
if($expr1) { 
    // if body
} else if($expr2) {
    // else if body
} else {
    // else body
}
```

The keywords `else if` SHOULD be used instead of `elseif` so that all control keywords are as readable as possible and remain in consistent English.


### 5.2. switch, case

A `switch` structure looks like the following. Note the placement of parentheses, spaces, and braces. The case statement MUST be indented once from switch, and the break keyword (or other terminating keyword) MUST be indented at the same level as the case body. There SHOULD be a comment such as `// no break intentional` when fall-through is intentional in a non-empty case body.

```
switch($expr) {
    case 0:
        echo 'First case, with a break';
        break;
    case 1:
        echo 'Second case, which falls through';
        // no break intentional
    case 2:
    case 3:
    case 4:
        echo 'Third case, return instead of break';
        return;
    default:
        echo 'Default case';
        break;
}
```


### 5.3. while, do while

A `while` statement looks like the following. Note the placement of parentheses, spaces, and braces.

```
while($expr) {
    // structure body
}
```

Similarly, a `do while` statement looks like the following. Note the placement of parentheses, spaces, and braces.

```
do {
    // structure body
} while($expr);
```


### 5.4. for

A `for` statement looks like the following. Note the placement of parentheses, spaces, and braces.

```
for($i = 0; $i < 10; $i++) {
    // for body
}
```


### 4.5. foreach

A `foreach` statement looks like the following. Note the placement of parentheses, spaces, and braces.

```
foreach($iterable as $key => $value) {
    // foreach body
}
```


### 4.6. try, catch

A `try catch` block looks like the following. Note the placement of parentheses, spaces, and braces.

```
try {
    // try body
} catch(FirstExceptionType $e) {
    // catch body
} catch(OtherExceptionType $e) {
    // catch body
}
```


## 6. Closures


### 6.1. Using Closures

Closures MUST follow the same rules as defined above for method and function declarations. When `use` is present, it MUST be preceded by a single space and SHOULD NOT have whitespace after it.

```
// closure with arguments
$foo = function($arg1, $arg2) {
    // body
};

// closure with arguments and use vars
$bar = function($arg1, $arg2) use($var1, $var2) {
    // body
};

// closure in argument list
$foo->bar($arg1, function($arg2) use($var1) {
    // body
});

// closure in multi-line argument list
$foo->bar(
    $arg1,
    function($arg2) use($var1) {
        // body
    },
    $arg3
);
```


## 7. Operators


### 7.1. Operators and spacing

PHP comparison, arithmetic, string concatenation and ternary operators SHOULD have a single space before and after them:

```
$a == $b; // do this
$a==$b; // not this

$a + $b; // do this
$a+b; // not this

$a += $b; // do this
$a+=$b; // not this

$a . $b; // do this
$a.$b; // not this

$a ? $a : $b; // do this
$a?$a:$b; // not this
```

PHP logical operators MAY have a single space before them but MUST NOT have a space after them:

```
$a && !$b; // do this
$a && ! $b; // not this
```

Increment and decrement operators MUST NOT have space between them and the value that they affect:

```
$a++; // do this
$a ++; // not this
```


### 7.2. Operators in ProcessWire Selector Strings

Operators in ProcessWire selector strings MUST NOT have whitespace before or after them. This is not just a matter of style, but a requirement of statements in selector strings. We mention it here to call attention to the difference between operators usage in selector strings and operators in PHP code.

- Do this: `name=some_page, qty>10`
- Not this: `name = some_page, qty > 10`


## 8. Strings and Quotes


### 8.1. Single vs. Double Quotes

For strings, it is RECOMMENDED that you use double "quotes" if the string value may have (or may ever have) a PHP variable inserted into it. PHP variables are resolved in double quoted strings, but not in single quoted strings.

Otherwise it is RECOMMENDED that you use whatever quote style reduces or prevents the need to escape characters within the string. For example, use double "quotes" if your string contains an apostrophe like `"it's"`, or use single 'quotes' if your string contains embedded double quotes like `'click "submit" to continue'`.

When outputting strings with HTML markup, it is RECOMMENDED that you use double quotes for the string, and single quotes for HTML attribute values within the string. For example:

```
$q = htmlentities($searchValue, ENT_QUOTES, 'UTF-8');
echo "<input type='search' name='q' placeholder='Search' value='$q'>";
```


### 8.2. Variables in strings

It is RECOMMENDED that you use variables embedded in strings, when possible, rather than concatenating multiple strings. Double quotes must be used to embed variables in strings.

```
echo "Welcome $firstName $lastName!"; // do this
echo "Welcome " . $firstName . " " . $lastName . "!"; // not this
```

If the embedded variable is an object property, of an object property, then you MUST surround the variable access in {brackets}. Likewise, if the variable is adjacent to text in the string that might be confused with the variable name, it must also be surrounded in {brackets}. These are PHP requirements, not stylistic.

```
// brackets required
echo "Welcome {$user->info->fullName}!";

// brackets NOT required
echo "You have logged in $user->logins times.";

// brackets required
echo "<input name='{$id}_sort'>";
```

For the cases where it's not required to use {brackets} it is RECOMMENDED that you don't use them, unless they aid readability in a specific case.


### 8.4. Multi-language Translatable Strings

```
echo sprintf(__('Thank you for visiting %s'), $user->fullname); // do this
echo __("Thank you for visiting $user->fullname"); // not this!
```

Considering the above, it is RECOMMENDED that you use single 'quotes' when possible for translation strings, as it serves as a good reminder that variables may not be inserted in translation strings. However, you MAY use either quote style, so long as you remember variables should not be inserted in double quoted translatable strings.

Additional comments to the person performing translation of phrases MAY be provided by appending a PHP `// comment` to the end of the line that the phrase exists on. For example:

```
echo __('Thank you for visiting'); // Thank you message shown at logout
```


## 9. Using ProcessWire API Variables


### 9.1. Accessing API Variables

You SHOULD access ProcessWire API variables via `$this->wire('var')` within `Wire` derived classes. You MAY also use `$this->var` when supported by the class. When in doubt, use `$this->wire('var')`.

You SHOULD access ProcessWire API variables via `wire('var')` outside of Wire derived classes. You MAY also use `$var` when API variables are locally scoped (as in template files, outside of function or class declarations).

Within hook functions that are procedural functions or closures, you SHOULD access API variables from the given `HookEvent` argument. For example:

```
$wire->addHookAfter('Pages::saved', function(HookEvent $event) {
    $user = $event->user; // access current user API variable (or any other)
    // ...
});
```


### 9.2. Creating API Variables

Within a Wire-derived class, you MUST create a new ProcessWire API variable by calling:

```
$this->wire('varName', $varValue);
```

Outside of a Wire-derived class, you MUST create a new ProcessWire API variable by calling:

```
$wire->wire('varName', $varValue); // if $wire is in scope
wire()-wire('varName', $varValue); // if $wire is not in scope
```

You MUST NOT overwrite existing API variables (many will throw exceptions if you attempt to).


## 10. ProcessWire 3.x


### 10.1. Dependency Injection

All newly-created objects that are derived from `Wire` SHOULD have their dependencies injected. In order to do this, pass the new object through the `wire()` method.

```
$item = $this->wire(new SampleClass()); // do this
$item = new SampleClass(); // not this
```

Within template files (outside of Wire-derived class scope) you may use the `$wire` API variable to perform the same thing:

```
$item = $wire->wire(new SampleClass());
```

Any objects returned from ProcessWire API functions/methods will already have their dependencies injected. You only need to inject dependencies to objects that you are creating yourself with `new ClassName()`.


### 10.2. ProcessWire 3.x Namespace

For new projects in ProcessWire 3.x, it is RECOMMENDED that you use the ProcessWire namespace, or declare your own. To use the ProcessWire namespace, the following MUST be placed at the top of your PHP file:

```php
<?php namespace ProcessWire;
```

To declare your own namespace, replace `ProcessWire` above with the path/name of your namespace. However, unless you have a reason to use a separate namespace it is RECOMMENDED that you use the ProcessWire namespace for simplicity.

Please note that if you do not declare a namespace in your PHP file (reverting to the root namespace), ProcessWire may maintain a separate compiled copy of the file in order to ensure compatibility with 3.x.


## 11. Other


### 11.1. Procedural functions

Procedural functions SHOULD follow the same syntax and documentation rules as class methods.


### 11.2. define()

PHP `define()` statements SHOULD use `UPPERCASE` rather than `camelCase`. Words should be split by underscores. For example:

```
define("SAMPLE_DEFINE", "This is a sample define");
```


### 11.3. PHPDoc Style Recommendations

```
/**
 * Description of method
 *
 * @param int $arg1
 * @param int $arg2
 *
 */
public function someMethod($arg1, $arg2) {
  // method body
}
```
