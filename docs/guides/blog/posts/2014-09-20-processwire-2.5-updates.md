# ProcessWire 2.5.1 updates

Source: https://processwire.com/blog/posts/processwire-2.5-updates/

## Sections


## ProcessWire 2.5.1 updates

20 September 2014 by Ryan Cramer [ 1 Comment](/blog/posts/processwire-2.5-updates/#comments)

With 2.5 released last week, we focused this week on tweaking some details with admin navigation. We got a lot done this week, but still want to refine yet a few more details before we send out official 2.5 press releases. The good news is that there are no major bug reports to-date, so 2.5.0 is looking very solid in its first week. Official announcements (and official release version 2.5.2) will likely go out next week. Here's what's new this week on the dev branch (currently 2.5.1).


### Updates to Reno admin theme

One thing that we wanted for our official 2.5 release was for the Reno admin theme to have the same ajax-driven navigation that's present in the Default admin theme. This has been updated so that now the Reno admin theme has full AJAX support for its navigation items.

In version 2.5.0 the Reno admin theme did not have full multi-language support. It was close, but there were still a few translatable phrases to get in place and adjustments to make in the language editor. Now that is complete, so the Reno admin should now be fully multi-language compatible.


### Process modules can now feed navigation to the admin theme

Since we were already working on admin theme navigation and AJAX, it also seemed like a good opportunity to take it further. Now any Process module can serve AJAX-driven navigation to the admin theme. Previously it was only supported for Fields and Templates. If you grab the dev core this week, you'll see you now have AJAX driven navigation for Modules, Users, Roles, Permissions and Languages. That's just the beginning–we'll explain how to support this in your own Process modules a little further down in this post.


### New overwrite mode for file and image fields

A new "overwrite" mode has been added to file and image fields. In your field settings, you'll see a checkbox for Overwrite Mode. If you check that box and upload a file that has the same filename as one that's already in the field, it will overwrite the existing file rather then making a copy of it (and thus renaming it). One example of where this is especially useful is in uploading a new version of a language pack. Previously you had to delete the files in the language pack before you could upload the new version. Now you can just drag in the new language pack and it'll replace all the files automatically. Naturally, we have now made this the default setting when uploading language packs.


### New tutorial for Default Site Profile

The new Default Site Profile now comes with a comprehensive README file that walks you through exactly how everything works. It's actually a lot more than just a README, and more accurately a full tutorial for the Default Site Profile. Though we think beginners will find this a handy tutorial regardless of whether using the Default Site Profile or not. [Read it here](/docs/tutorials/default-site-profile/). While you are there, check out the other [tutorials](/docs/tutorials/), including Joss's new [gallery tutorial](/docs/tutorials/galleries-short-and-long/).


## Process Module Navigation


### How to expose navigation from your Process module

Admin theme navigation support enables your Process modules to expose their navigation options to the admin theme. This in turn enables the admin theme to make your Process module's navigation part of the overall admin navigation.

Lets use Form Builder as an example: previously you would go to Setup > Forms to get to Form Builder. Now you can hover Setup > Forms and then it will reveal a list of forms available. From there you can choose a form to edit or click the button to add a new form. This all happens right in the navigation regardless of what page you are on in the admin.

Our official release of ProcessWire 2.5 will likely be version 2.5.2 which includes this navigation support for Process modules. You can also find this now on the dev branch. For developers creating Process modules, here's how to implement.

You have two choices when it comes to supporting navigation: AJAX or static navigation. *Please note that to see the results of either method below, you'll need to reset your modules cache by going to Modules > Check for new modules. This forces ProcessWire to reload your getModuleInfo() data. *


### Static navigation

If you want to just support a few predefined navigation options, go for the static method. Specify a **nav** array in your `getModuleInfo()` method (or ModuleName.info.json or ModuleName.info.php). Here's an example from the new *ProcessDatabaseBackups* module.

```
public static function getModuleInfo() {
  return array(
    'title' => 'DB Backups',
     // …other module info left out for brevity
    'nav' => array(
      array(
        // URL for action, relative to module's root URL
        'url' => 'backup/',
        // navigation text
        'label' => 'New Backup',
        // navigation icon (optional)
        'icon' => 'plus-circle',
      ),
      array(
        'url' => 'upload/',
        'label' => 'Upload',
        'icon' => 'upload'
      )
    )
  );
}
```

Here's the result:

Those are the basics of it. Other properties you can specify with each navigation option are:

- **permission:** The name of the permission a user must have in order to see this navigation option.
- **navJSON:** If nav option reveals additional options, specify the URL (relative to module root) where a JSON list of that navigation can be retrieved.

That last option "navJSON" is an interesting one in that it lets you combine both static and AJAX/JSON navigation. If you have an interest in using this property, please see the getModuleInfo() from [ProcessModule](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/modules/Process/ProcessModule/ProcessModule.module#L24) for a good example.


### AJAX/JSON navigation

Use the AJAX JSON navigation method when your Process module contains an unknown quantity of dynamic items. Most Process modules are managing some sort of group of items, so we expect that this option may be used more commonly than the static navigation option. To enable it, your getModuleInfo() only needs to specify the boolean value true for a `useNavJSON` property, i.e.

```
public static function getModuleInfo() {
  // …other module info left out for brevity
  'useNavJSON' => true
);
```

Following that your Process module should specify an `___executeNavJSON()` method, like this:

```
public function ___executeNavJSON(array $options = array()) {
  $options = array(
    // WireArray or regular array of your module's nav items
   'items' => $this->myItems,
    // Name of property to get nav label from each item
   'itemLabel' => 'name',
    // URL each item should link to. Specify {id} or {name} in it.
   'edit' =>'edit/?id={id}',
    // Optional URL for adding new items (if applicable)
   'add' => 'add/',
    // Optional property with name of icon for each item (if applicable)
   'iconKey' => 'icon',
    // Optional default icon for each item (when none available)
   'icon' => 'file-o',
  );
  return parent::___executeNavJSON($options);
}
```

Here's an actual example from the soon-to-be-released next version of Form Builder:

```
public function ___executeNavJSON(array $options = array()) {
  $options['items'] = array();
  foreach($this->forms as $id => $name) {
    $form = wire('forms')->load($name);
    if(!$form || !$form->hasPermission('form-list')) continue;
    $options['items'][] = $form;
  }
  $options['itemLabel'] = 'name';
  $options['edit'] = 'editForm/?id={id}';
  $options['add'] = 'addForm/';
  return parent::___executeNavJSON($options);
}
```

If you need to go beyond what is provided above, you can also choose to implement your own `___executeNavJSON()` method. See the [/wire/core/Process.php](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/core/Process.php#L243) file for full implementation.
