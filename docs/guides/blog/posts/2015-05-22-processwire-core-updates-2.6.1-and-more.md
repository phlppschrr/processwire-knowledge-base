# ProcessWire core updates (2.6.1) and more

Source: https://processwire.com/blog/posts/processwire-core-updates-2.6.1-and-more/

## Sections


## ProcessWire core updates (2.6.1) and more

22 May 2015 by Ryan Cramer [ 5 Comments](/blog/posts/processwire-core-updates-2.6.1-and-more/#comments)

**ProcessWire 2.6.1 is now on the dev branch! **This post discusses some of the new features that have been added. These will likely be merged to the master branch after a week or two of testing. 2.6.1 also includes a couple minor fixes and adjustments, though none that are particularly significant or likely to affect most. But if any of the new features mentioned here sound appealing, we think you will enjoy the latest core dev branch. As always, please let us know how it works for you.


### Page editor now reminds you to save

This week we added a feature to the core that helps prevent lost work when you navigate away from a page you are editing (whether intentionally or unintentionally). Now when you are making edits to a page, if you've happened to change any fields, it'll pop up a confirmation dialog to make sure that's what you really wanted to do. The dialog box also tells you what fields you changed, to help you in your important decision.

This feature has actually been available already for quite a long time by way of Soma's [Form Save Reminder](http://modules.processwire.com/modules/form-save-reminder/) module. I've heard several times that people thought this should be a core feature. But I didn't want to add such a feature to the core until we had a means of avoiding the inevitable false positives.

The false positive issue doesn't actually have anything to do with the Form Save Reminder module (which does a great job) but rather with the fact that PW can support any possible kind of input, given that inputs are in fact modules themselves (Inputfield modules). Not all inputs trigger the necessary javascript "change" events in order to be trackable. For instance, many (or most) javascript-based fields don't trigger change events (CKEditor and TinyMCE for example). By necessity, any form/save/reminder type function must involve custom code specific to those situations. In fact, Form Save Reminder does exactly that (and quite well) by using CKEditor and TinyMCE-specific API code to identify when a change has occurred.

Since the Inputfield modules are an unknown, and could be anything, it's simply not possible for the core to get into the APIs of every possible input type to identify changes. The Form Save Reminder module attempts to do that with CKEditor and TinyMCE, but those are just two (albeit common) inputs of any number of current and future possibilities. And that's why there's not been such a function in the core. What we needed was some sort of alternative method whereby the Inputfield could notify the core of the change, rather than the other way around. Anything else isn't sustainable. So that's what we added this week.


### How it works

For inputs that already trigger change events (as occurs with native HTML inputs) the Inputfield module doesn't need to do anything. But for inputs that don't (like rich text editors and the like), they just need to add a `InputfieldStateChanged` class to their parent `<div class='Inputfield'>` container when it's known that they have changed. That's all there is to it. So in addition to adding this feature, we also updated all the core Inputfields that didn't trigger change events to adopt this behavior.

If you've already got Soma's Form Save Reminder module installed, then the new core feature will let Soma's module have control. That way you don't get two confirmation dialogs. There are also some differences in how the core handles it versus Form Save Reminder (they don't share the same code). Soma's module is more production ready since it's already been out for quite some time. But for those not using Form Save Reminder, we could use your help testing the new core feature on the dev branch. Specifically, we'd like to know if you come across any false positives, and if so, with what type of inputs. What's a false positive? That's when it fails to notify you when it should, or when it notifies you about a change you are certain isn't applicable.

The core feature is enabled by default in the page editor. All you have to do is install core 2.6.1 and it'll be enabled. But it's not enabled for any other forms outside the page editor just yet. The feature is capable of supporting any form in ProcessWire. Specifically, any InputfieldForm that has the class `InputfieldFormConfirm` will automatically have the change tracking function enabled. We'll likely enable it in most other core forms very soon, but wanted to start with just the page editor since that's where we've done all our testing thus far. But given that it will work on any InputfieldForm, it's something you can use with your own forms, and very soon, with FormBuilder too.

If for some reason you want to disable the feature, you can do so by setting `$config->pageEdit['confirm'] = false;`, but after using it for several days here, I think you'll find it a welcome and worthwhile new feature.


### Process modules now support external view files

ProcessWire lets you do things the way you want and doesn't impose strict rules on how you should do things. But sometimes people like to have a more structured methodology for certain tasks. A best practice is to separate output markup from logic, and we often like to do that functionally by having separate `render()` methods in our Process modules. But outside of the ProcessWire world, it's more common to separate markup generation into separate view files, and likewise some people prefer this strategy, especially when the front-end and back-end are being developed by different people.

This week we added the ability for Process modules to support this more MVC-like strategy for people that prefer it, or situations where it might be beneficial. Here's how it works:

Process modules all have an `execute()` method, and optionally one or more `execute[Something]` methods, where "Something" represents a URL segment. Previously these methods were required to return the output directly, which was typically generated markup. The original intention was that you could make use of ProcessWire's *TemplateFile* class if you wanted to delegate the markup to a separate view file. But in practice, we've not seen anyone do that, and it's perhaps just too much of a pain...

In recognition of that, the execute methods now support a built-in view system. Rather than your execute() methods returning generated markup, they can now optionally return an array of variables to send to a view file.

The view file follows the same naming convention as the execute() method that it represents, and the view files should be placed in a ./views/ directory within your module directory. Here are examples of method names to view file names:

- execute() => views/execute.php
- executeSomething() => views/execute-something.php
- executeSomethingElse() => views/execute-something-else.php

The "execute-" part of the filenames is actually optional, so you could also do this:

- executeSomething() => views/something.php
- executeSomethingElse() => views/something-else.php

We have updated the [ProcessHello module (dev branch)](https://github.com/ryancramerdesign/ProcessHello/tree/dev) to demonstrate use of the new view system. It's really simple to use, but if there's any question take a look at that module for a working example. More on these updates below…


### Updated "Hello World" modules for PW 2.6

For a long time we've been maintaining fully functional "Hello World" modules to demonstrate the latest supported features with PW's Module interface. The modules also serve as excellent starting points for your own modules. These modules include:

This week both of these modules were updated for new features in ProcessWire 2.6. Here are a few of the new things that these modules now demonstrate:

Note that we also have the [FieldtypeEvents](https://github.com/ryancramerdesign/FieldtypeEvents) module, which is our "hello world" module for Fieldtype and Inputfield modules. This has not had any changes made to it specific to PW 2.6, as I didn't think any changes were helpful there. But I wanted to mention this module since it is part of the Hello World family of modules and the one you should look at if looking to create a Fieldtype and/or Inputfield module.


### Mini tutorial: really simple short links

*The following tutorial is not specific to ProcessWire 2.6 and should work in most versions of ProcessWire. *

Some of the URLs for these blog posts get pretty long, and there are times when I want to publish a link to one of these posts without the super-long URL. For instance, if I'm on the phone with somebody and want to tell them to look at something in a post, I pretty much have to tell them to go to processwire.com and click around to find it, because the direct URL is just too long to communicate verbally…

Now we could use a URL shortener service, which makes them shorter, but not really much easier to communicate. I'd like to tell somebody, "hey just go to processwire.com/123 to read the article." And actually, it's really easy–here's how:

```php
$s = $input->urlSegmentStr; 
if(strlen($s)) {
  if(ctype_digit($s)) {
    $p = $pages->get((int) $s);
    if($p->id && $p->viewable()) $session->redirect($p->url);
  }
  throw new Wire404Exception();
}
```

Note: the above assumes you aren't already using URL segments on your homepage for some other purposes. If you are, then you may want to remove the "throw" statement at the bottom and double check that what we're doing here is compatible with what you are already doing.

Now you can access your-domain.com/123 where "123" is the ID of the page you want to go to. If you aren't sure what the ID is, just edit the page and you'll see it in your address bar. Whenever you access one of these short URLs, it will perform a 301 redirect to the full URL of the page.


### Taking it further

The above was exactly what I needed, but lets say that you wanted to have more control over the URL segment and use things like "hello-world" or "rotfl", rather than just using the page ID? No problem. We'll just need to create a field to store our named short links. Follow these instructions:

```php
$s = $input->urlSegmentStr; 
if(strlen($s)) {
  $s = $sanitizer->pageName($s);
  if($s) {
    $p = $pages->get("short_link=$s");
    if($p->id && $p->viewable()) $session->redirect($p->url);
  }
  throw new Wire404Exception();
}
```

Now test things out. Open your browser to your-domain.com/abc or whatever you specified for your test short_link. It should now redirect to your intended page. Access an undefined short_link and you should get a 404.
