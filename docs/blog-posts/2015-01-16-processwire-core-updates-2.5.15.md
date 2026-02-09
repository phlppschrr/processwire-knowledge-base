# ProcessWire core updates (2.5.15)

Source: https://processwire.com/blog/posts/processwire-core-updates-2.5.15/

## Sections


## ProcessWire core updates (2.5.15)

16 January 2015 by Ryan Cramer [ 1 Comment](/blog/posts/processwire-core-updates-2.5.15/#comments)


## Blogging about Logging (and more)


### New log viewer module (ProcessLogger)

One weakness in ProcessWire has always been its logging system. While it has included all the tools to create and append to log files for quite awhile, it has never included any core tool to view them in the admin.

Of course the log files aren't web accessible (for security) so the only way to view them is by grabbing them directly from the server (FTP or SSH, etc.). As a result, I'd gather many ProcessWire users don't even know that logs exist in ProcessWire. And that's been okay, because log files really haven't been utilized all that much. However, we introduced the [$log](/api/variables/log/) API variable in ProcessWire 2.5, which makes logs much easier to write, and makes them accessible not just to core and modules, but to template files in individual websites and applications.

As of ProcessWire 2.5, it's super easy to record anything that you want to ProcessWire logs (form submissions, site searches, etc.). In my case, I also use logs a lot for debugging ajax requests or other difficult to debug operations. The time had come where we needed to finish the job and make logs accessible not just for writing, but for reading too.

This week the dev branch introduces the ProcessLogger module, which enables you to read and manipulate log files from the admin. When you grab the latest PW dev branch, you'll see a new "Logs" menu item under your "Setup" menu. Click to that and you'll get a list of log files. Click on any log file, and it'll show the entries to you. But it can do a lot more than that. Notable features include:

- Real-time updates: when viewing a log, new log entries appear automatically as they occur (ajax).
- Ajax-driven pagination and filtering.
- Results displayed newest-to-oldest (reverse of what they are in actual log files).
- Perform live text searches on logs.
- Filter log entries by date ranges.
- Download log files.
- Chop (prune) log files to contain only entries for the last [n] days.
- Delete log files.
- Add entries to log files (useful for testing out the real-time updates feature without having to write any code).

Please let us know how the ProcessLogger module works for you. One thing you may notice is that our existing core log files (messages and errors) tend to be a little boring and repetitive in terms of their content. Now that the log files are more acccessible (as a result of this module) we'll be putting more emphasis on making the log files more useful and relevant.


### New $log and $this->log('text') API functions

This week several updates were made to ProcessWire's $log API variable. Previously it could be used to save log entries. Now it can also be used to retrieve logs, find and filter them, and more. See the [$log API variable page](/api/variables/log/) for details. Most of these were added in support of the new ProcessLogger module, but I thought they might be genuinely useful in other contexts too.

In addition to the $log API variable updates, we've added a log('text') method to the base Wire class. This enables any ProcessWire module, class, or Wire-derived class to call a `$this->log('text');` method and have "text" automatically recorded to a log file with the same name as the module/class.* The new method is actually defined as `___log()` in the class definition, which has the effect of making it hookable, while also preventing it from causing errors with existing modules/classes that may have already implemented their own log() method… it's a common method name after all.

We've setup most of the core API variables to record to their own log files, but only if requested to. A new `$config->logs` array has been added which can contain any of the following to enable log files for the associated API variables:

```
$config->logs = array('pages', 'templates', 'fields', 'modules');
```

When any of those are enabled, all save/add/delete/clone, etc. activities are logged. In our default configuration (/wire/config.php), we've enabled this only for 'modules', but you can choose to enable it for the others if you'd like in your /site/config.php. Note that this logs $config option applies only to core logs, and only because we didn't want to make the assumption that you wanted all of this activity logged (the 'pages' log could grow especially large if you are doing lots of imports and such). In other modules or classes the `$this->log('text')` or `$this->log->save('name', 'text')` will always create/append log files, without needing mention in the `$config->logs`.

*Same name, but converted to hyphenated lowercase behind-the-scenes, i.e. the HelloWorld module's log file would be called hello-world.txt.


### Create new fields from your template edit screen

This week we have a new contribution from Adrian (who you may know from the forums or [his many great modules](http://modules.processwire.com/authors/adrian/)). It's a small thing that you may not even notice at first, but it's super useful when you are building out a new site. Grab the latest dev branch of ProcessWire and take a look in Setup > Templates > some-template > Basics [tab].

Note the linked text in the screenshot below "Create a new field." Click that and it'll pop open a modal window, enabling you to create a new field while editing your template. Once saved, the modal will close and automatically be added to your template.

This is really very handy. Of course, use some care here, as you usually want to create fields outside the context of a specific template, when possible. This provides for greater reusability potential. Meaning, consider how a field might possibly be used in the big picture of your site rather than just one specific page type [template]. But so long as you keep that in the back of your mind, this new feature is a nice time saver. I personally have been benefitting from this all week. Thanks Adrian!


### New icon selection module in the core

Another small but useful detail added to the core this week is the InputfieldIcon module. As you may know, you can enter an icon to associate with any field or template in ProcessWire. But it's not been particularly easy to do, as you have to manually go to the Font Awesome site, determine which icon you want to use, and then copy/paste the name into the relevant input in the Field or Template editor (advanced tab).

I honestly got sick of keeping a window open to the Font Awesome website anytime I'm working with fields or templates, so I put together a simple module to improve this part of the UI in PW's admin. Now when you go to set an icon for a Field or Template, you can pick from a list of icon names, or from a list of the icons themselves:

I wouldn't usually add a module to the core unless it had more reusability potential, and this one does. This new Inputfield can be used by any module (core or 3rd party) that needs to provide an icon input/selection capability. For example, the core AdminThemeReno and SystemNotifications modules ask you to specify icons as part of their configuration screens–I will be updating these to use InputfieldIcon. I imagine we'll see 3rd party modules begin to use this in the coming months as well. But in the end, it was the core that really needed something better with regards to icon selection, and now we've got it.
