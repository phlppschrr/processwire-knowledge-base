# How to structure your template files

Source: https://processwire.com/docs/tutorials/how-to-structure-your-template-files/

## Summary

How to use some of the more common strategies used by developers in structuring template files. Includes pros and cons as well as extensive examples.

## Key Points

- How to use some of the more common strategies used by developers in structuring template files. Includes pros and cons as well as extensive examples.
- When ProcessWire loads a template file, it hands it a copy of the current $page, along with all of the other ProcessWire API variables. Beyond that, it is just a regular PHP file. What happens within that file is entirely to the developer.
- ProcessWire knows nothing about the type of output you intend to produce with that template file. In fact, you can produce any kind of output with your template file, which is one of the reasons why ProcessWire is so flexible. But with flexibility comes some ambiguity, especially for developers new to ProcessWire. Such developers may be asking themselves "what exactly should I put in this template file?" or "what are the best practices?".

## Sections


### Remember to enable debug mode

Regardless of what template file strategy you use, you will almost always want debug mode ON when you are working with template files. This ensures that you see error messages and notices as they occur. On a production site you would of course want error messages suppressed so that they do not interfere with the user–or worse–reveal sensitive details that might affect security. But when developing a site and making edits to template files, you most certainly want to see error messages and notices, otherwise it would be very difficult to make progress! Edit your /site/config.php file, locate the line referring to $config->debug and change it from false to true.


## Direct Output

The first strategy is the easiest to understand (though also likely the least flexible). But even if you don't intend to use this strategy, read on, as it does help to establish the context that template files operate in. When a template file is used as direct output, the only difference between a template file and an HTML file is that you can use some PHP in there when you want to. Here is an example of a template file using direct output:


## Direct Output with Includes

When we want to utilize the convenience of direct output, but don't want to repeat the same markup in every template file, we move the code that we want to re-use into separate files. That way we can have multiple template files that pull in the same bits of code without us having to repeat ourselves. The benefit is that if we need to change something, we only need to change it in one place rather than in all of our template files.


### Direct output with automatic inclusions

It's not actually necessary to manually include("./head.inc") and include("./foot.inc") in each of your template files. You can make this happen automatically by editing your /site/config.php file and populating these two lines like so:


### Disadvantages of direct output

Where direct output starts to fall apart is when you want to affect the output in multiple regions on a page. In our examples above, our template files only control the output for what comes between head.inc and foot.inc. While we could accommodate more regions with additional includes, it starts to get a little cumbersome. What if any of our template files could populate any region in our markup without us having to know exactly where it will go ahead of time? That leads into our next strategy…


## Delayed Output


### Also known as the main.inc strategy

This strategy focuses on generating the output for all the various regions of our final document ahead of time, and temporarily storing them in placeholders (called variables). Rather than including a head.inc and foot.inc file, we instead just include a main.inc file at the end. That main.inc file knows where to output all the placeholders.


### What does this strategy look like?

When using delayed output with variables, your template files focus on populating variables rather than outputting them. This leads to template files that are quite a bit simpler, and occasionally even blank! Here's an example of what our template file might look like:
