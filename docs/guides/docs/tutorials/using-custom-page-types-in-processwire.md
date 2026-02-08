# Using custom page types in ProcessWire

Source: https://processwire.com/docs/tutorials/using-custom-page-types-in-processwire/

## Summary

A look at some lesser known advanced techniques that enable you to introduce new conveniences by creating custom page types.

## Key Points

- A look at some lesser known advanced techniques that enable you to introduce new conveniences by creating custom page types.
- An advanced tutorial by Benjamin Milde
- As ProcessWire users you're probably aware of the fact that core objects like users, roles or languages are just pages. But that fact can actually be missed out quite easily as ProcessWire's api does offer lot's of conveniencies, which are specific to those objects.

## Sections


### When to use this approach

Before we start I want to mention, that this approach is not really beneficial if you just want to add a single method here and there. Also it's not recommended to create a new repository classes for any small group of 3-5 pages. These classes, that we'll be creating here, are most useful if you know you'll be working with the type of data extensively throughout your site. Otherwise it may not be worth the effort.


### Custom repository API variable

Now let's get onto the topic. When looking into the source files of those existing api variables there's one important similarity. They do all extend the same class, which is PagesType. This class is a baseline implementation of what we're trying to create – just flexible enough, so it just needs some setup to be ready to use.


### Custom methods for events

In this second part of the tutorial we'll add custom methods to the event instances we'll be getting from our new $events api variable. For our example we'll be implementing a check if an event does start at the current day, which might be something often required throughout the site.


### Hooking

We're using a conditional hook here. This means ProcessWire will make it look like the method does not exist on a page, which isn't an event, and return a result just in the case it is one. This is the way I'd recommend for one-of additions.


### Inheritance

The second option we have is extending the Page class like we did it above with the PagesType class. For that we'll create another file site/api/event.php and include it like the one previously.


### Why not use hooks

Before I end here I want to cover the reasons why I sometimes favor inheritance over hooks. Hooks are great, but have some backdraws especially for more complex systems, which benefit most from those classes we've created.


### Finish up
