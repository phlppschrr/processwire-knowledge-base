# New ajax-driven inputs, conditional hooks, template family settings and more

Source: https://processwire.com/blog/posts/new-ajax-driven-inputs-conditional-hooks-template-family-settings-and-more/

## Sections


## New ajax-driven inputs, conditional hooks, template family settings and more

31 July 2015 by Ryan Cramer [ 3 Comments](/blog/posts/new-ajax-driven-inputs-conditional-hooks-template-family-settings-and-more/#comments)


## ProcessWire 2.6.11

Major updates to the core dev branch this week, including system-wide support for AJAX-driven Inputfields, support for conditional hooks, some very useful updates to the Template editor, improvements to our autocomplete field, a new version of CKEditor, upgrades to AdminThemeReno and more!


### New AJAX-driven Inputfields, system-wide

A few weeks back, we introduced the new ListerPro inline column editing features to you. At the time we mentioned that the core additions to support it would be put to more good use very soon. And that's exactly what we did this week. You now have two new visibility settings available for any input fields in your page editor, or with forms that you might define on your own using the Inputfields interface. Note the two new AJAX options in the screenshot below (taken from the Field editor Input tab):

When you choose one of the two AJAX options available the field won't be rendered or processed with the page you are editing, unless you first click on it to open it.

**Here's the best part though: **you can use this option with Fieldsets and Tabs too, delegating entire groups of fields or tabs of fields to only load when they are needed for edits. The benefits are rather major here, in that you maintain a whole lot of fields in your page editor, without the lag and front-end overhead sometimes associated with large forms.

This is not unlike the modal tab option we introduced to you several months back, in that it does something similar. However, we think you may like this new option even better because it doesn't make use of modals, and it can be applied to any field (or group of fields), rather than just tabs.

The AJAX-driven features should now work with all core input fields (yes, even including files/images, repeaters (!), PageTable, asmSelect, and so on). However, a lot of new code went into this over the last week, and you may very well find some scenarios where it doesn't work. If so, please let me know. There are also some scenarios where you'll want to avoid AJAX-driven inputs, such as field dependencies where one of the dependent fields is loaded from AJAX. For now, if you want to use AJAX-driven inputs, make sure you test thoroughly when using the new modes before assuming all is well. Note that most of the ProFields do not yet support these modes, but I'll be working on that next week. When it comes to 3rd party Inputfields that have Javascript dependencies, it's probably best to assume they won't work yet, unless you test and find out otherwise.

We've already started to use these new modules in the core. The new "Usage" tab in the template editor uses them, as do the "Parent" and "Who can access this page?" fields from the "Settings" tab of any page editor. This means that fewer resources are needed to build the page editor, which makes everything load more quickly.

If you want to use these AJAX modes in your own Inputfield forms (from the API side), see the new collapsedYesAjax and collapsedBlankAjax constants at the top of /wire/core/Inputfield.php.


### New conditional hooks

Conditional hooks imply the ability to specify conditions along with the hook definition. This is best explained by example. Lets say we've got the following hook function in our /site/ready.php file. The Page::changed hook has been with PW since the beginning, and it is called every time a value is modified on a page. It receives 3 arguments: the name of field that changed, the old value, and the new value. Here's what a function that hooks to Page::changed looks like, *without* use of conditional hooks:

```
$wire->addHookAfter('Page::changed', function(HookEvent $event) {
  $page = $event->object;
  $change = $event->arguments(0);
  if($page->template == 'order' && $change == 'order_status') {
    // execute some code when "order_status" changes on "order" pages.
  }
});
```

The conditional format lets you accomplish the same thing as the above, like this:

```
$wire->addHookAfter('Page(template=order)::changed(order_status)', 
  function($event) {
    // execute some code when "order_status" changes on "order" pages.
  });
```

The expressions in parenthesis that you see in the conditional format `(template=order)` and `(order_status)` are where conditions are specified. This can be any selector string *or* the value you want to match. In our example above, the first argument to `Page::changed()` is a string (specifically, the name of the field that changed) so we just specify the value we require to be present in order to execute our hook function. Were the argument an object, then we'd specify a selector string to match some property in it.

Here's the same example, but taken a little further on the implementation side:

```
$wire->addHookAfter("Page(template=order)::changed(order_status)", 
  function(HookEvent $event) {
    $page = $event->object;
    $old = $event->arguments(1); // old value
    $new = $event->arguments(2); // new value
    $event->addHookAfter("Pages::saved($page)",
      function($event) use($page, $old, $new) {
        $event->message("Status change: $old->title to $new->title");
        $event->removeHook(null);
      });
  });
```

In the above example, you can see that we are attaching yet another conditional hook `Pages::saved($page)` within the hook, and that hook executes when the `$page` that had the `order_status` change is saved. When that page is saved, we report a message, and then remove the hook (since we only want it to run once).

Stepping back for a minute, lets take a closer look at the `::changed(order_status)` part. In most cases, when using conditional hooks you are likely to want to match something from the first argument to the hook method. However, if you want to match a value from something other than the first argument to the hooked method (or maybe multiple arguments at once), you can still do so. Just specify the zero-based index of the argument in this format "0:conditions".

For example, lets say that we wanted our hook to execute when the order_status changes from "pending" to "delivered". Since the `Page::changed()` method has 3 arguments (property, old value, new value) we can access those as arguments 0, 1, 2. Our hook definition can access them like this below. Note that order_status is a Page field in our case, so will compare against its "name" property.

```
$wire->addHookAfter("Page(template=order)::changed(0:order_status, 1:name=pending, 2:name=delivered)", 
  function(HookEvent $event) {
    // ...
  });
```

With the above, our hook function will only be called when a page using template "order" has an order_status field that changes from "pending" to "delivered". Now that may be getting a little much, and you certainly don't have to place all your conditions in your hook definition of you don't want to. The example is just there to show you that you can, if you want to. You could just as easily do this, using a conditional hook, but checking the order_status values within your hook function instead:

```
$wire->addHookAfter("Page(template=order)::changed(order_status)", 
  function(HookEvent $event) {
    $old = $event->arguments(1);
    $new = $event->arguments(2);
    if($old->name == 'pending' && $new->name == 'delivered') {
      // ...
    }
  });
```


### New conveniences in template family settings

When you get the latest version of ProcessWire, head on over to edit a template in Setup > Templates, and click the Family tab. If you are editing a template that doesn't yet have any pages created with it, or only has *one* page created with it, you'll have a new option for the "Can this template be used for new pages" setting. Note the "One" option in the screenshot below:

Note: the screenshot above says "(no more allowed)" next to the One option because I already had a page using this template, so it was just indicating that it's not allowing any more pages to be created with that template.

This "One" option is particularly handy for situations where you are creating parent/child template relationships, and you only want one of the parent template pages to exist in the system. This lets you configure the template for that scenario before you even create the page. Once the page is created, it won't let you create any more using that template. No longer do you have to add a template, configure it, create the page, and then go back and configure the family settings to prevent more pages of that type from being created.

Next take a look at the "Allowed template(s) for children" and "Allowed template(s) for parents". The templates here now indicate whether they are ready, or need additional configuration, to meet the intended parent/child relationship. Should they need additional configuration, you can now simply click on the template name, and it'll pop open a modal window, directly to that template's Family tab. Thanks LostKobrakai for suggesting this useful shortcut.

Now click over to the "Basics" (main) tab. Note the last field: Usage. Click that, and it opens a new Lister showing you all pages using that template. (This new Usage field is using an AJAX-loaded Inputfield, as introduced earlier in this post). Since it is a Page Lister, it'll work regardless of how many pages you might have using that template, since it is paginated. You can also click to edit and view pages right from there, but if you want to get into more specific page manipulations, you'll probably want to go to the PageList or the main Page Lister, outside of the template editor. However, we thought it would be handy for you to have the ability to see at a glance all the pages using that template while you are editing it.


### Improvements to the Page Autocomplete Input

When using a Page Autocomplete input in the ProcessWire admin for single page selection (vs. multi-page selection) it now uses a more condensed format that's easier to use and takes up less space. Previously it used the same format for both single and multi-page selections. Now you've got something much simpler for when you only need a single-selection autocomplete:


### Other updates

**We upgraded our CKEditor version from 4.4.6 to 4.5.1.** Usually we can just put in a new version of CKEditor and everything works, but that was not the case this time. We had to go back in and make several tweaks in the system to get it working properly, but that's now done. Please let us know if you come across anything that's not working with it.

**There were also some updates to the Reno admin theme this week.** Thanks to Tom Reno for his great work with PW's best looking admin theme.

Today's version of ProcessWire is 2.6.11, but I'm not bumping up the version number today because the scope of changes is rather major, and I'd rather give it the weekend before the ProcessWireUpgrade module starts notifying people of the new version. So if you'd like to upgrade to the the version of the dev branch discussed here, please grab it from GitHub and then do a Modules > Refresh in your admin. Please test thoroughly before using in production and let us know if you run into any hiccups.

Next week we'll be putting out new versions of most of the ProFields. And right now we're testing the ProFields Table field with new Page Autocomplete support. Hope that everyone has a great weekend and week ahead and don't forget to check out the [ProcessWire weekly](http://www.flamingruby.com) on Saturday morning!
