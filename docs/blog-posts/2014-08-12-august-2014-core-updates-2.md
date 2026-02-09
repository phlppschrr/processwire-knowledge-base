# August 2014 Core Updates #2

Source: https://processwire.com/blog/posts/august-2014-core-updates-2/

## Sections


## August 2014 Core Updates #2

12 August 2014 by Ryan Cramer [ 0 Comments](/blog/posts/august-2014-core-updates-2/#comments)


### Upgrades to CKEditor

We've made several upgrades to our CKEditor Inputfield in order to make it easier to customize, configure and add plugins. As you may know from a past edition of the Weekly, CKEditor is now a core module in ProcessWire.

We've made several additions this week to make it more customization and plugin friendly by adding support for a customizations directory [/site/modules/InputfieldCKEditor/](https://github.com/ryancramerdesign/ProcessWire/tree/dev/site-default/modules/InputfieldCKEditor) – have a look at that link for the defaults, now included in the default site profile.

Here's what's in there by default:

- [plugins/](https://github.com/ryancramerdesign/ProcessWire/tree/dev/site-default/modules/InputfieldCKEditor/plugins) Directory to place additional CKEditor plugins in. You can then activate them from your CKEditor field settings (see the short tutorial below).
- [contents.css](https://github.com/ryancramerdesign/ProcessWire/blob/dev/site-default/modules/InputfieldCKEditor/contents.css) Example CSS file for the admin editor. To make CKEditor use this file, go to your CKEditor field settings and specify /site/modules/InputfieldCKEditor/contents.css as the regular mode Contents CSS file.
- [contents-inline.css](https://github.com/ryancramerdesign/ProcessWire/blob/dev/site-default/modules/InputfieldCKEditor/contents-inline.css) Same as contents.css but for the inline mode editor.
- [mystyles.js ](https://github.com/ryancramerdesign/ProcessWire/blob/dev/site-default/modules/InputfieldCKEditor/mystyles.js) Optional configuration for the CKEditor Styles option. This enables you to set what appears in your "Styles" dropdown menu. To use this file, go to your CKEditor field settings and set the Custom Styles Set to be this label and file: Then enter "Styles" somewhere in your toolbar definition. Now you have selectable custom styles in your editor.

While we were putting in these updates, we also updated the CKEditor version to the latest. Of the items above, the most exciting is likely the plugins directory. That's because previously you couldn't install custom plugins without putting them right in CKEditor's core plugins directory.

Read on to see how to use it…


### Mini-tutorial: how to properly install a plugin for CKEditor bundled with ProcessWire

This is how installing plugins for CKEditor works with the latest core additions in dev branch. Because the plugins are now installed under your /site/ directory, they persist through core upgrades, which is exactly what you want – read on to learn how to handle things properly! Please note that this tutorial applies only to the latest [dev branch](https://github.com/ryancramerdesign/ProcessWire/tree/dev).

- **Download a [plugin](http://ckeditor.com/addons/plugins/all) from the CKEditor site** We'll use the Wordcount plugin as an example: [http://ckeditor.com/addon/wordcount](http://ckeditor.com/addon/wordcount). Click the "Download" button to download the ZIP file. Extract or upload the contents of the ZIP file to:
- **Edit field settings** We'll assume that you want to add this plugin to a CKEditor field called "body". In that case, in the ProcessWire admin, go to Setup > Fields > body > Input. Scroll down to the "Plugins" section and check the box for the "wordcount" plugin. Save. *While in your field settings, double check that your Editor Mode setting is Regular Editor and not Inline Editor, as the Wordcount plugin doesn't support Inline Editor mode.*
- **Edit a page that uses this field** You should see a running word count in the lower right hand-corner. Cool – you're almost done! But lets say that you wanted to see a running character count too…
- **Return to field settings** (Setup > Fields > body > Input). Scroll down to the "Plugins" section and open the "Wordcount settings" box. The website you downloaded the Wordcount plugin from outlined some optional settings that we'll use now. Paste following into the settings to make the plugin show both a word countand a character count:
- **See the results** After saving the field, go back to edit a page using this field. Now you should see both a word and character count. That's it. Congratulations, you've just installed CKEditor plugin in a way that makes it both functional and safe from upcoming core upgrades!


### A fix for “This request appears to have been forged”

Chances are you've seen that message at some point or another. Our CSRF protection has been a bit aggressive in the past; if you edited one page, and opened another page editor before saving the first, you'd encounter this error message when you tried to save the first.

We've put in an update this week that makes that behaviour less annoying. Now you can edit multiple pages without having to worry about what order they are saved in.


### New module installation options

Since ProcessWire 2.4, you've had the ability to install modules in your admin simply by pasting in the class name for the module you want to install from the [Modules Directory](http://modules.processwire.com/).

As of this week (on the dev branch) ProcessWire now gives you two more new module installation options:

- Upload a module ZIP file
- Specify a URL to a module ZIP file

These options should be particularly handy with modules that aren't already in the modules directory, and for your own custom modules. As they've not yet had a lot of testing, please let us know if you run into any issues with these new upload options.


### Change to how you add pages

Usually when you add a new page in ProcessWire, it is initially in an unpublished state. There is an exception: when you add a new page that has no fields (other than a "title" field) it publishes immediately.

This is the way it's always been. The thinking behind it was that there's really no need for an intermediate unpublished state on such pages, since there's not really any content to consider.

However, some people found this confusing. As a result, we now have separate "Save" and "Publish" buttons when adding a new page – though you will only see the "Publish" button in cases where there aren't any fields to consider other than Title.
