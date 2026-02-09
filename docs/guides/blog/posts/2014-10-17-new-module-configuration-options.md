# ProcessWire 2.5.5 – New module configuration

Source: https://processwire.com/blog/posts/new-module-configuration-options/

## Sections


## ProcessWire 2.5.5 – New module configuration

17 October 2014 by Ryan Cramer [ 7 Comments](/blog/posts/new-module-configuration-options/#comments)


### Module configuration got a lot nicer this week

ProcessWire 2.5.5 (dev) adds new module configuration options that will save module developers time. Of course, the old methods will continue to work, but we think there are some things you'll like better about the new methods. To get started, lets consider this simple test module that displays a message on every page load in the admin:

/site/modules/Test/Test.module

```
class Test extends WireData implements Module {
  public static function getModuleInfo() {
    return array(
     'title' => 'Module Test',
     'version' => 1,
     'summary' => 'Module for testing/demo purposes.',
     'autoload' => 'template=admin',
    );
  }
  public function ready() {
    if($this->fullname && !count($this->input->post)) {
      $msg = "Hi $this->fullname! ";
      $msg .= "Your age: $this->age. ";
      $msg .= "Favorite color: $this->color.";
      $this->message($msg);
    }
  }
}
```

That module has 3 configuration settings: fullname, age and color.


### The way we used to do it

In the past, we would have implemented the module configuration like this below, as part of the Test.module file. It's a bit long, so just skip to the end of this next code sample if you want.

/site/modules/Test/Test.module

```
class Test extends WireData implements Module, ConfigurableModule {
  public static function getModuleInfo() {
    return array(
     'title' => 'Module Test',
     'version' => 1,
     'summary' => 'Module for testing/demo purposes.',
     'autoload' => 'template=admin',
    );
  }
  static protected $defaults = array(
    'fullname' => '',
    'color' => 'blue',
    'age' => 40
  );
  public function __construct() {
    // populate defaults, which will get replaced with actual
    // configured values before the init/ready methods are called
    $this->setArray(self::$defaults);
  }
  public function ready() {
    if($this->fullname && !count($this->input->post)) {
      $msg = "Hi $this->fullname! ";
      $msg .= "Your age: $this->age. ";
      $msg .= "Favorite color: $this->color.";
      $this->message($msg);
    }
  }
  public static function getModuleConfigInputfields(array $data) {
    $inputfields = new InputfieldWrapper();
    $data = array_merge(self::$defaults, $data);

    $f = wire('modules')->get('InputfieldText');
    $f->attr('name', 'fullname');
    $f->label = 'Full Name';
    $f->required = true;
    $f->attr('value', $data['fullname']);
    $inputfields->add($f);

    $f = wire('modules')->get('InputfieldSelect');
    $f->attr('name', 'color');
    $f->label = 'Favorite Color';
    $f->options = array(
      'red' => 'Red',
      'green' => 'Green',
      'blue' => 'Blue'
    );
    $f->attr('value', $data['color']);
    $inputfields->add($f);

    $f = wire('modules')->get('InputfieldInteger');
    $f->attr('name', 'age');
    $f->label = 'Your Age';
    $f->attr('value', $data['age']);
    $inputfields->add($f);

    return $inputfields;
}
```

That really adds a lot of verbosity to our simple module, doesn't it? Some things to note above:

- We had to add a `ConfigurableModule` interface to our class definition.
- We had to define a static `getModuleConfigInputfields()` method for configuration (an inconvenience).
- We had to manually define and manage our default values in the static `self::$defaults` variable (a pain).
- We have to manually populate values to our configuration fields (also a pain).

In the end, this method is reliable and works just fine… but is just not as nice as it could be. With ProcessWire growing, we need something nicer…


### Enter the new ModuleConfig class

Now we have new options to define module configuration. We use a separate configuration file and class which is named the same as the module but with "Config" appended to the end of it. This new class simply extends the new *ModuleConfig* class included with the core. This *ModuleConfig* class can save us a lot of work!

Go back and look at the first code sample on this page, which shows the nice and clean "Test" module, before it got bogged down with all the configuration code. That clean and simple version is exactly what the module would look like when we use a ModuleConfig file. It needs no configuration-specific code, nor does it need to implement *ConfigurableModule*. It can simply just refer to it's configuration values with `$this->fieldName` without any preparation. Here's what the the *ModuleConfig* file looks like:

/site/modules/Test/TestConfig.php

```
class TestConfig extends ModuleConfig {
  public function getDefaults() {
    return array(
      'fullname' => '',
      'color' => 'blue',
      'age' => 40,
    );
  }
  public function getInputfields() {
    $inputfields = parent::getInputfields();

    $f = $this->modules->get('InputfieldText');
    $f->attr('name', 'fullname');
    $f->label = 'Full Name';
    $f->required = true;
    $inputfields->add($f);

    $f = $this->modules->get('InputfieldSelect');
    $f->attr('name', 'color');
    $f->label = 'Favorite Color';
    $f->options = array(
      'red' => 'Red',
      'green' => 'Green',
      'blue' => 'Blue'
    );
    $inputfields->add($f);

    $f = $this->modules->get('InputfieldInteger');
    $f->attr('name', 'age');
    $f->label = 'Your Age';
    $inputfields->add($f);

    return $inputfields;
  }
}
```

Note that we are implementing two methods here: `getDefaults()` and `getInputfields()`. The `getDefaults()` method just returns an associative array of field name and default value. The `getInputfields()` method returns a group of Inputfields. There are some benefits here versus the previous static method:

- Default values get automatically populated to our module (we don't need to do that manually in a `__construct()` method).
- We don't have to set the value attribute of any Inputfields… *ModuleConfig* takes care of that for us automatically.
- No more static methods or variables interfering with the way we usually access the API in modules.
- We don't have to do anything to tell ProcessWire that the module is configurable other than adding a file in the same directory named ModuleNameConfig.php, where you replace ModuleName with the actual module name. Note however that you will need to click the Modules > Refresh button in the admin in order for ProcessWire to notice it the first time.


### Using an array to define module configuration

Another nice thing about the new ModuleConfig class is that it gives you another option for defining your module configuration. You can define it entirely as an array. Admittedly, I prefer to define things programatically, but some have asked for this array option in the past. So here it is. And I have to admit, now that I see it in action it's growing on me–I like how little code it takes to define module configuration:

/site/modules/Test/TestConfig.php

```
class TestConfig extends ModuleConfig {
  public function __construct() {
    $this->add(array(
      array(
        'name' => 'fullname',
        'label' => 'Full Name',
        'type' => 'text',
        'required' => true,
        'value' => '',
      ),
      array(
        'name' => 'color',
        'type' => 'select',
        'label' => 'Favorite Color',
        'options' => array(
          'red' => 'Red',
          'green' => 'Green',
          'blue' => 'Blue'
        ),
        'value' => 'blue',
      ),
      array(
        'name' => 'age',
        'type' => 'integer',
        'label' => 'Your Age',
        'value' => 40
      )
    ));
  }
}
```

That's all there is to it! Some things to mention about the above:

- The entire configuration is defined in an array sent to the `$this->add()` method (a method of *ModuleConfig*). Each field has it's own array defining properties of the field. The properties are exactly the same properties you populate when doing it programatically (as in the previous example).
- The "type" property is the only exception, as you don't see that when defining it programatically. This is where you tell it what type of field it can be. The value can be any Inputfield module name, or you can omit the "Inputfield" part at the beginning, and just specify the remainder, i.e. "text" rather than "InputfieldText".
- Our default values are defined in this array as well. See the "value" property. This is a nice benefit, keeping everything together.
- Not shown, but if you wanted to define a fieldset, then you would make the type "fieldset" and give it a "children" property which is itself an array like the above. You can nest as far as you'd like.

Alright… you guys that wanted arrays for defining Inputfields–I have to admit this is most definitely a good thing. So as a bonus (stepping outside module configuration for a moment), you can now use these arrays anywhere that you use Inputfields. Simply pass an array like the above to any *InputfieldWrapper*, *InputfieldForm*, or *InputfieldFieldset* via the add() method, and it will set it all up for you, i.e `$form->add(array( ... ));`

Here's the module configuration screen that all of the above examples produced:
