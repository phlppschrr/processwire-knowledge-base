# About the ProcessWire API

Source: https://processwire.com/docs/start/api/

## Summary

What the API is, why we think you'll like it, and how it makes ProcessWire a unique platform in the CMS landscape.

## Key Points

- What the API is, why we think you'll like it, and how it makes ProcessWire a unique platform in the CMS landscape.
- API means application programming interface. In our context, it most commonly refers to the clearly defined interface (or tools) that the web developer uses to interact with content managed by the CMS. This interaction is most commonly used to produce output (like markup for the front-end of a site). In our case, the interactions can also be to manipulate content, create new content, and so on.
- ProcessWire is entirely built around the API, and its admin panel is actually a website built using this API. ProcessWire was a headless CMS before there was a term for it. ProcessWire's easy-to-use API can do everything that you can do interactively in the admin, and more.

## Sections


## Introduction to the API


### What is an API in a CMS?

API means application programming interface. In our context, it most commonly refers to the clearly defined interface (or tools) that the web developer uses to interact with content managed by the CMS. This interaction is most commonly used to produce output (like markup for the front-end of a site). In our case, the interactions can also be to manipulate content, create new content, and so on.


### Why is the API so important?

When it comes to a CMS, the API is the primary interface and set of tools that the web developer uses is developing a CMS-driven website/application. The web developer most commonly works within the context of output, like HTML, CSS and perhaps Javascript. But when it comes to retrieving or manipulating the actual content, it's between the CMS API and the developer.


### What’s unique about ProcessWire’s API?

The ProcessWire API may already be comfortable and familiar for you, even if you've never used it before. To explain why it's both unique and familiar, lets first look at where it came from.


## What makes up the API?

ProcessWire’s API consists of a few different components:


### API Variables

The API consists of a few variables (via PHP objects) which are provided to your site's template files. These variables enable you to get or modify anything from your content, much in the same way that jQuery enables you to get and modify anything from the DOM.


### Selectors

Another major component of ProcessWire's API are selectors. Like in jQuery, selectors are simple strings of text that specify fields and values. For example, "name=ryan" is a simple selector that says: "find items that have the name ryan." These selectors are used throughout ProcessWire to get and find pages (and other types of data). ProcessWire selectors resemble jQuery selectors in many instances, but are also quite different. More about ProcessWire selectors


### Fluent Interfaces

Most of the API objects in ProcessWire are chainable, using a fluent interface. This enables you to accomplish multiple operations on one line, for example:
