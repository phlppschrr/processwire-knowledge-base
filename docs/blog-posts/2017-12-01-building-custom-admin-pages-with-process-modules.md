# Building custom admin pages with Process modules

Source: https://processwire.com/blog/posts/building-custom-admin-pages-with-process-modules/

## Sections


## Building custom admin pages with Process modules

1 December 2017 by Ryan Cramer [ 8 Comments](/blog/posts/building-custom-admin-pages-with-process-modules/#comments)

This week we have a guest post from Bernhard Baumrock that is a nice introduction to creating Process modules in ProcessWire. Bernhard covers a lot of useful material here and we hope you enjoy it. Big thanks to him for his contribution this week. While there's a lot here, there's actually a few more things to cover too (like use of separate view files) so we may cover those in a Part 2 at some point in the near future as well. For more about Bernhard, check out his website at [baumrock.com](https://www.baumrock.com/). I've been traveling (Ryan) but arrived back in town last night, so next week we'll be back to our regular PW core updates and schedule.


## Yes, it’s that simple! ;)


### A tutorial on building custom admin pages in ProcessWire by creating Process modules

*By Bernhard Baumrock*

If the title of this blog post sounds familiar you've probably read my [tutorial in the forum a few weeks ago](/talk/topic/17709-how-to-create-custom-admin-pages-aka-processmodules-yes-its-that-simple/). Since there was a lot of positive feedback to that tutorial and requests to explain everything more in detail, I asked Ryan if he was interested in me writing a guest post while he is traveling. He was and so I started writing…

The intention of this article is the same as the one from my forum tutorial: I want to show how easy it is to create your own pages in the PW admin, how you can use PW's components and include external scripts. And finally, I want to show that you don't have to be afraid of looking into the code of the core to look for documentation that is not listed in the PW docs.

For this tutorial I'm using a clean PW 3.0.84 installation with the default profile. If you want to follow the examples I recommend you try it with the same setup so that you can use my code without any modifications. The code of all examples is available in [this gitlab repository](https://gitlab.com/baumrock/ProcessSimple/).


## Building a basic custom admin page


### Hello World

I'm sure everybody is eager to write their first custom backend page, so we will start with the most basic module possible and explain what's happening later on. This step might be easier than you have ever thought — it's just a matter of placing one file (with very little code) in the right place and giving it the correct name.

Please create the file ProcessSimple.module, place it in your /site/modules/ folder and copy this code into it:

```php
<?php namespace ProcessWire;

class ProcessSimple extends Process {

  public static function getModuleinfo() {
    return [
      'title' => 'Custom Admin Page Example',
      'summary' => 'No need to be afraid of building custom admin pages.',
      'author' => 'Bernhard Baumrock, baumrock.com',
      'version' => 1,

      // page that you want created to execute this module
      'page' => [
        // your page will be online at /processwire/yourname/
        'name' => 'yourname',
        // page title for this admin-page
        'title' => 'Hello',
      ],
    ];
  }

  public function ___execute() {
    return 'Hello World :)';
  }
}
```

Side note: the 3 underscores "___" preceding the method name "execute" are optional. Whenever a method in ProcessWire is preceded with 3 underscores, it becomes hookable. Should you call the method from your own code, you would call it without the underscores and ProcessWire takes care of the rest. In the case of the example above, if the method was named execute() rather than ___execute(), it would still work the same in our examples here, but just would not be hookable by other modules.

Congratulations! You have now built your first very own Process module, meaning you have created your first custom admin page (and application). You can now install your module via the PW backend and the module will show up in your modules list:


### Explanations

What happened behind the scenes is that ProcessWire created a page for us under the parent /processwire/ (or whatever the admin page is named) using the template admin. Every page having the admin template executes a specified Process module. And that's what we did: We created a Process module that returns "Hello World :)", and we assigned that Process to our newly created page in the admin.

This is the page editor, editing the newly created page in the admin:


### The manual way

If you don't believe me (or you want to get a better understanding of what is going on) you can try to create the same Process module manually. If not you can skip this example. ;)

We'll call that module ProcessSimpleManual.module and paste this code into the file:

```php
<?php namespace ProcessWire;
class ProcessSimpleManual extends Process {
  public function ___execute() {
    return 'Hello World :)';
  }
}
```

Notice that we also changed the name of the class to "ProcessSimpleManual" instead of "ProcessSimple". The name of the file and the name of the class always have to correspond!

Go to the Modules screen, click *refresh* and you will see the new Module:

We can even install this module!

So you may ask what is the difference relative to the first version (that had more code)? If you look at the screenshot above you may notice that some information is missing, like the summary of the module. And if you look at the menu you'll see that there is no page for that module. That's intended for this example because we want to take the steps manually. But in real life development of course it would be better to take the first route.

Back to work… Go to the page tree and create a new admin page under "Setup":

Save, and on the next screen, you can then choose the Process that the page should use—choose "ProcessSimpleManual". After choosing the right Process and publishing the page you'll see your page in the menu. In this case we placed our page under the parent "Setup". I just wanted to show you that you can place your page wherever you want:

Well done—you now know how to create basic admin pages and maybe you are impressed how simple it is. Our next step will show how to build a Module with multiple pages and how to add some common elements like Data Tables.


## Building a module with multiple pages and buttons


### Hello Page2!

For more complex modules it might be necessary to split the content into several pages. So we'll continue expanding our ProcessSimple.module with a second page. All you need to do is add a second method to your module and give that method a proper name:

```
public function ___executeMysecondpage() {
  return 'Hello Page2 :)';
}

```

Here we called the method `___executeMysecondpage()` so the page will be accessible via /processwire/yourname/mysecondpage where "processwire" is the name of your admin, "yourname" is the name of the admin page created for your module, and "mysecondpage" is the name of your method (following the "___execute" or "execute" part). The content of the page will again be what your method returns:


### Add some HTML (i.e. buttons)

For now we have just returned simple strings in our Process module, but of course most of the time want to return some HTML. In this example we'll place a button on each of our two pages that makes it possible to navigate from one page to the other. We will modify both methods a little bit. You can also find all the code also on [gitlab](https://gitlab.com/baumrock/ProcessSimple/):

```
public function ___execute() {
  return '
    <p>
      Hello World :)
    </p>
    <p>
      <a href="./mysecondpage" class="ui-button ui-state-default">
        Go to Page2
      </a>
    </p>
  ';
}

public function ___executeMysecondpage() {
  return '
    <p>
      Hello Page2 :)
    </p>
    <p>
      <a href="./" class="ui-button ui-state-default">
        Go to Page1
      </a>
    </p>
  ';
}
```

Screenshot of the code above, formatted a bit differently, but equivalent:

We get a nice button and can navigate between the pages:

There is also a second way of adding buttons that we will cover next, after this method naming tip below.


### Method naming tip

If you want to use hyhens in your URL segments, simply use camel case for your method name. Any uppercase characters (after the first) translate to hyphens in the URL. The following examples help to clarify:

- `executeMySecondPage` translates to `my-second-page` in the URL
- `executeMysecondpage` translates to `mysecondpage` in the URL


### Using internal components (modules)

The example above was a very basic HTML tag but there is A LOT more to discover in the PW core. I'll show you two of my most favourite components that I use in my modules:


### PW-Panels

Let's start with a very easy one: The PW-Panel. [They were introduced in PW 3.0.15](/blog/posts/pw-3.0.15/) and I prefer them a lot over modals. They are great for opening previews of PDFs, opening edit-screens of pages and much more. And the best part is that it is as simple as adding a "pw-panel" class to your link. Modify the "Go to Page2" link from the example above and add the class "pw-panel" and you'll see the link will open in a nice panel like this:

You might wonder where I have all this knowledge from? Open up your IDE and search your files for "panel":

This lists all files that contain "panel" in the filename. Most of the time you'll want to take a look at the .module and the .js/.css files. And most of the time you'll find some VERY valuable information inside those files. It's something like hidden docs that might save you from asking one or another question in the forum. ;) The panel file is a very good example for this statement: [panel.js on Github](https://github.com/processwire/processwire/blob/master/wire/modules/Jquery/JqueryUI/panel.js)


### Data tables

Tables are still one of the most important tools for a content management system. And everybody knows that it is not that simple to output a table with HTML that is nicely designed and has some additional features like column sorting. There are a lot of tables in the PW backend and of course there is a Module that helps you creating them. Though it is a little more complicated than the examples we have had so far. But don't be afraid—whenever you see something in the backend that you want to use, you can open your browser dev-tools and inspect that element (sorry for my German screenshot). Here we take the table of the modules screen:

You see that the table is called "AdminDataTable" and we also see that we are using the UIkit admin theme because the table has some UIkit classes (uk-table, etc.). Again we can open up our IDE and inspect the core files for information about the AdminDataTable class. The file MarkupAdminDataTable.module currently has little documentation about how to use it, so you can try to find information on a different place… I'm sure you know the Setup > Templates page in the admin. If you look at the edit-screen of that page, you see that it renders the Process module named "ProcessTemplate". We search the file for "AdminDataTable" and see how it has to be used:

Let's add another page to our Process module that renders a simple table:

```
public function ___executeTable() {
  $table = $this->modules->get('MarkupAdminDataTable');
  $table->headerRow(['A', 'B', 'C']);
  $table->row([1, 2, 3]);
  $table->row([4, 5, 6]);
  return $table->render();
}
```


### Buttons (Option 2)

In a previous example we added a button via an anchor tag, but as we know now how to use PW's internal components we can add buttons in a different way. That can be necessary in several situations—for example you could add a button that triggers some AJAX actions where you don't want to leave the current page. We can add a button that should open the page itself in a panel. When the page is rendered in the panel (which also means we have a GET variable called "modal" set to "panel"; in case of a normal modal it would just be "1") we hide the button to avoid an endless panel-in-panel-loop using a simple if-statement:

```
public function ___executeTable() {
  $out = '';

  $table = $this->modules->get('MarkupAdminDataTable');
  $table->headerRow(['A', 'B', 'C']);
  $table->row([1, 2, 3]);
  $table->row([4, 5, 6]);
  $out .= $table->render();

  if(!$this->input->get('modal')) {
    $button = $this->modules->get('InputfieldButton');
    $button->value = 'Open Page in Panel';
    $button->attr('data-href', './table');
    $button->addClass('pw-panel');
    $out .= $button->render();
  }

  return $out;
}
```


### Add external styles and scripts (i.e. charts)

You can do a lot with PW's internal tools but sometimes you'll want to include external software to extend PW's functionality even further. Charts are a great example, so we'll add another page to our Module that shows a simple chart rendered by the [chartjs library](http://www.chartjs.org/). As we are going to add a javascript file in this step, we will move the ProcessSimple.module file inside of its own folder. We name the folder ProcessSimple, move the .module file there and refresh the modules cache by hitting the Refresh button in the PW backend (Modules > Refresh).

Now we can take [this Line Chart](http://www.chartjs.org/samples/latest/charts/line/basic.html) and add it to our page:

```
public function ___executeChart() {
  $this->config->scripts->add(
    'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.bundle.min.js'
  );
  $this->config->scripts->add(
    'http://www.chartjs.org/samples/latest/utils.js'
  );
  $this->config->scripts->add(
    $this->config->urls->ProcessSimple . 'chart.js'
  );

  $out = '';

  $buttons = [
    'randomizeData' => 'Randomize Data',
    'addDataset' => 'Add Dataset',
    'addData' => 'Add Data',
    'removeDataset' => 'Remove Dataset',
    'removeData' => 'Remove Data',
  ];

  $button = $this->modules->get('InputfieldButton');
  $button->setSmall(true);

  foreach($buttons as $id => $label) {
    $button->id = $id;
    $button->value = $label;
    $out .= $button->render();
  }

  return $out;
}
```

First we add the chart.js library to the scripts array. Then we add some utility functions from chartjs, and finally we add our local file. The code from our file chart.js is taken from their samples, unmodified and only wrapped in a `$(document).ready()` jQuery function. [See our chart.js file](https://gitlab.com/baumrock/ProcessSimple/blob/master/chart.js).

I hope you get an idea of what powerful tools you are holding in your hands now. ;)


## Handling user-input: Using Forms & Inputfields

Inspired from [Abdus Dashboard-Tutorial in the forum](/talk/topic/16185-how-to-build-a-simple-dashboard-with-ajax-functionality-using-a-process-module/) we'll use our new knowledge and create a little Dashboard of the well known Skyscrapers profile. As this profile is quite outdated (but still a great resource) I updated ProcessWire to the latest Version. By the way: It was nothing more to do than changing the old "body" field from TinyMCE to CKEditor and adding "namespace ProcessWire;" to the config.php file - and the profile is from 01/2013! Anybody still afraid of using ProcessWire for long term Projects? ;)

Note: if interested in the Skyscrapers profile, you can find the [newer version here](https://github.com/ryancramerdesign/skyscrapers2), but it is just the template files rather than the complete profile.


### Organizing your code and your files

Before we start, we will organize our module a little differently from our other examples. This one is going to be a little more complex so we split everything into seperate files to keep a good overview. [See the ProcessHello module for files and instructions](https://github.com/ryancramerdesign/ProcessHello/tree/dev).


### Module Info + Views

The first thing we do is to separate the Module Info into a separate file. We'll call our new module "ProcessSkyDashboard", so we create the following:

- a folder /site/modules/ProcessSkyDashboard
- a file /site/modules/ProcessSkyDashboard/ProcessSkyDashboard.module.php
- a file /site/modules/ProcessSkyDashboard/ProcessSkyDashboard.info.php

See [this blog post](/blog/posts/processwire-core-updates-2.6.1-and-more/#updated-hello-world-modules-for-pw-2.6) for details.

ProcessSkydashboard.info.php

```php
<?php namespace ProcessWire;
$info = [
  'title' => 'Skyscraper Dashboard',
  'summary' => 'Demo Dashboard for my guest blogpost',
  'author' => 'Bernhard Baumrock, baumrock.com',
  'version' => 1,
  'page' => [
    'name' => 'dashboard',
    'title' => 'Dashboard',
  ],
];
```

ProcessSkydashboard.module.php

```php
<?php namespace ProcessWire;
class ProcessSkyDashboard extends Process {
  public function ___execute() {
    echo __FILE__;
  }
}
```

One thing that was new to me that Ryan mentioned is the use of views. It's also shown in the ProcessHello module but I will not take this approach here and explain why later on. After installation we see the output of our Module:

Some advertisement in this screenshot for Adrian's awesome [TracyDebugger](/blog/posts/introducing-tracy-debugger/) that is a must-have for every development work done in ProcessWire. :) Lets start with our dashboard now…


### Adding your first field: InputfieldMarkup

Whenever we are talking about user input we need a form with some Inputfields [Inputfield modules]. Forms and Inputfields are not only great to handle user input but also to structure your output, as well as separate your code and functionality into several reusable pieces. I'll show you some examples at the end of this section. In our dashboard example we also need both structure and user input. We create a very basic form using the most minimalistic Inputfield modules we have: InputfieldForm and InputfieldMarkup.

```
public function ___execute() {
  $form = $this->modules->get('InputfieldForm');

  $field = $this->modules->get('InputfieldMarkup');
  $field->label = 'Table';
  $field->value = '--table--';
  $form->add($field);

  return $form->render();
}
```

Easy, isn't it? We add the other fields to get a skeleton of our dashboard…

```
public function ___execute() {
  $form = $this->modules->get('InputfieldForm');

  $field = $this->modules->get('InputfieldMarkup');
  $field->label = 'Table';
  $field->value = '--table--';
  $field->columnWidth = 50;
  $form->add($field);

  $field = $this->modules->get('InputfieldMarkup');
  $field->label = 'Chart';
  $field->value = '--chart--';
  $field->columnWidth = 50;
  $form->add($field);

  $fieldset = $this->modules->get('InputfieldFieldset');
  $fieldset->label = 'Create New';
  $form->add($fieldset);

  $field = $this->modules->get('InputfieldMarkup');
  $field->value = '--field1--';
  $field->columnWidth = 33;
  $fieldset->add($field);

  $field = $this->modules->get('InputfieldMarkup');
  $field->value = '--field2--';
  $field->columnWidth = 33;
  $fieldset->add($field);

  $field = $this->modules->get('InputfieldMarkup');
  $field->value = '--field3--';
  $field->columnWidth = 34;
  $fieldset->add($field);

  return $form->render();
}
```


### Creating separate methods for the output

To keep our code clean and readable we will create separate methods for each field's value:

```
// we change this
$field->value = '--table--';

// to this
$field->value = $this->renderTable();
```

When done, we get a dashboard like this:

See the code for this example here: [ProcessSkyDashboard.module.php.v1](https://gitlab.com/baumrock/ProcessSkyDashboard/blob/master/ProcessSkyDashboard.module.php.v1)


### Create our first “real” Inputfields

**Please take care whenever you are dealing with user input! You need to sanitize and validate all inputs carefully. The examples are just a quick showcase and not 100% foolproof or secure.**

I'm saying "real" here because technically speaking all of the fields in the admin are INPUTfields whereas some of them are used only for OUTPUTting data (like *InputfieldMarkup* or Kongondos great [InputfieldRuntimeMarkup](https://github.com/kongondo/FieldtypeRuntimeMarkup) that some of you might know). We added three Inputfields of type *InputfieldMarkup* at the bottom of our dashboard that we want to convert now to text Inputfields (InputfieldText). All we need to do is change the class name from *InputfieldMarkup* to *InputfieldText*, and then add name attributes to be able to retrieve those values later in our script. For the third field we use an *InputfieldPage* to show another option. Finally we add a button that submits this form. In the screenshot below, we added a TracyDegugger `bd()` call to dump our data and see what's happening:

See the code of this step here: [ProcessSkyDashboard.module.php.v2](https://gitlab.com/baumrock/ProcessSkyDashboard/blob/master/ProcessSkyDashboard.module.php.v2)

Next we need to add the logic of the form submit. We submit the form to a separate endpoint and we know already how to do that:

- Add a new method `___executeAddnewskyscraper()` to our module
- Set the form's action to submit to this page
- Redirect back to the dashboard after creating the page.

I just added this to the `___execute()` method:

```
$form->action = './addskyscraper';
```

Note: setting the action attribute (like above) is only necessary if you are NOT using trailing slashes in the URLs. If you *are* using trailing slashes for your Process module's URLs, then it's not necessary to set the form action attribute because the default setting is the current directory path.

And this new Method to save the page and redirect:

```
public function ___executeAddskyscraper() {
  if(!$this->input->post('submit')) throw new Wire404Exception();

  // determine city
  $city = $this->pages->get($this->input->post->int('City'));
  if($city->template != 'city') throw new WireException('Unknown city');
  if(!$city->viewable()) throw new WireException('City not available');

  // determine skyscraper name/title
  $title = $this->input->post->text('Name');
  if(empty($title)) throw new WireException('Skyscraper name required');

  // add page
  $p = new Page();
  $p->template = 'skyscraper';
  $p->parent = $city;
  $p->title = $title;
  $p->height = $this->input->post->float('Height');
  $p->save();

  // show message
  $this->message('Added a new skyscraper to the database');

  // redirect to our dashboard
  $this->session->redirect('./');
}
```

Note: The example above pulls values directly from the $input API variable. However, it is often preferable to use the source *InputfieldForm* to process input and pull the resulting values directly from the Inputfields. That way the validation is already taken care of. For example:

```
public function ___executeAddSkyscraper() {
  // build the add-skyscraper form
  $form = $this->buildAddSkyscraper();

  // if form not submitted, display it instead
  if(!$this->input->post('submit')) return $form->render();

  // process the InputfieldForm
  $form->processInput($this->input->post);

  if(count($form->getErrors())) {
    // form had errors, ask them to fix
    $this->error('Please fix the errors');
    return $form->render();
  }

  // add skyscraper from submitted form
  $p = new Page();
  $p->template = 'skyscraper';
  $p->parent = $form->get('City')->value->first();
  $p->title = $form->get('Name')->value;
  $p->height = $form->get('Height')->value;
  $p->save();

  // show message
  $this->message('Added a new skyscraper to the database');

  // redirect to our dashboard
  $this->session->redirect('./');
}
```

Please note: the above example is not shown in the example files. If you wanted to use this strategy, you'd want to move your InputfieldForm generation code to a separate method (i.e. buildAddSkyscraper) so that it can be called by both ___execute() and ___executeAddskyscraper(). This is the strategy used by most of the core Process modules.

Another approach could be to customize the add new page screen via a hook as recently [discussed in the forum](/talk/topic/17866-customize-add-new-page-screen/).


### Ajax reload fields

Besides the benefit of a better optical appearance, you get some features that are built into PW's Inputfield modules by default. You can group them into fieldsets, create responsive grids by setting the `columnWidth` property, and you can reload fields by triggering the "reload" event. I'll show you how in this section.

First we need to update our chart that is by now just a placeholder with hardcoded values:

```
$counts = [];
$counts[] = $this->pages->count('template=skyscraper,height<=50');
$counts[] = $this->pages->count('template=skyscraper,height>50,height<=150');
$counts[] = $this->pages->count('template=skyscraper,height>150');
$out = implode(',', $counts);
```

And the javascript (below is abbreviated, [see the full example](https://gitlab.com/baumrock/ProcessSkyDashboard/blob/master/ProcessSkyDashboard/skyscraperchart.js)):

```
var counts = $('#chart').data('counts').split(',');
// and replace the hardcoded array data: [12, 19, 3], with this variable
data: counts,
```

And finally the reload of the table: We will create a javascript that polls the server every 5 seconds. We place the file ProcessSkyDashboard.js into our module's folder—that will load the javascript automatically (same as for css files). Because we want to replace only the table we set an `id` attribute on that table in the `renderTable()` method of our module: `$table->id = 'skyscrapertable';`

Then the poll is quite simple:

```
$(document).ready(function() {
  function poll() {
    $( "#skyscrapertable" ).load( "./ #skyscrapertable" );
    setTimeout(poll, 5000);
  }
  poll();
});
```

I also added a simple add-new button to show you how you can easily use PW's built in tools instead of creating custom forms:

```
$button = $this->modules->get('InputfieldButton');
$button->value = 'Add new Skyscraper';
$button->icon = 'plus';
$button->setSmall()->setSecondary()->addClass('pw-panel');
$button->attr('data-href',
  $this->config->urls->admin . 'page/add/?template_id=' .
  $this->templates->get('skyscraper')->id
);
$out .= $button->render();
```

Of course this is just a quick example and it does not update the chart. It's just an [idea that was requested in the forum](/talk/topic/17709-how-to-create-custom-admin-pages-aka-processmodules-yes-its-that-simple/?do=findComment&comment=156698) and I wanted to show a basic principle how this can be done.


## How to install this Site-Profile

All files from this tutorial are [hosted here](https://gitlab.com/baumrock/ProcessSkyDashboard). To install the finished version follow these steps:

- Download the latest [PW dev version](https://github.com/processwire/processwire/archive/dev.zip).
- Download [the site profile](https://gitlab.com/baumrock/ProcessSkyDashboard/raw/master/site-SkyscraperDashboard.zip) and place it in your root folder (or subdirectory if preferred).
- Run the installer

There are some errors regarding the old google maps module that I did not fix because it would have taken me too long. I'm sorry for those errors though. If anybody wants to fix it I'm happy to accept pull-requests :)

I hope you enjoyed reading this and lost any fear about creating your first Process module. When I started diving into this topic around two years ago I quickly got some really cool results. You can see my [custom CRM/Controlling-Office-Management-Tool](https://www.baumrock.com/portfolio/individuelles-crm-und-controlling-tool/) that I built for a Vienna based company on my (PW powered and ProCache’d) [website (in german)](https://www.baumrock.com/portfolio/individuelles-crm-und-controlling-tool/) or on the [processwire forums (in english)](/talk/topic/17207-custom-office-management-crmcontrolling-software/).

See you soon in the forum! Bernhard
