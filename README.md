# MoMo 

A payment processing app for renewable energy management applications.

## Motivation
This project was created as a practical Python challenge for a job application.

## Description

*Note: The challenge description has been (non-exhaustively) rewritten in my own words. Misconceptions or -interpretations are entirely possible, if not likely.*

Implement a payment processing app that 

1. *provides* data from multiple payment service providers (PSPs), differing in **data formats** (XML, CSV, etc.) and **communication channels** (Web APIs, FTP dumps, email, etc.). Each data set does however include an **account_id** (referencing the corresponding SaaS instance, see below) and a **reference_id** (referencing the individual customer, initating the transaction).
2. *standardizes* the received data and **stores** (and logs) it for compliance reasons.
3. *'routes'* the standardized payment data to its destination. This destination is a **SaaS instance** (run in a seperate container) of software used for managing products and customers in the renewable energy sector. An instance that receives payment data in the standardized form will be able to process it and provide electricity according to the corresponding value. The application should be able to route payments by account_id **and** reference_id.

The focus should lie on the **simplicity** and **extendability** of the design, specifically with regard to the implementation of new PSP adapters and routing mechanisms.

## Tech Stack

The core behaviour is implemented as a [Django](https://www.djangoproject.com/) app and uses the [Django REST framework](http://www.django-rest-framework.org/). It also uses [requests - http for humans](http://docs.python-requests.org/en/master/) for routing.

## Features

### Model Structure

something about the model structure

### Core API

The application exposes a single API that accepts payment data in a **standardized format**. Services that integrate with individual payment service providers are written seperately. This has two basic advantages:

1. There are few constraints on API integrations for specific payment service providers. They can basically be written in any language as long as they register with the core API and update their current status (UP/DOWN).

2. Payment service providers that wish to integrate with the MoMo API can do so by posting their data directly to core, thereby eliminating the need for a specific adapater/API integration.

3. By outsourcing the adapters from the core API, we facilitate a clear *separation of concerns*. All the tasks that relate to individual PSPs are done by the adapters, all core tasks by core.

Disadvantages of this approach are the reduced performance of HTTP based API communication compared to a monolitic app. Furthermore the loose coupling between adapters and core may require the implementation of more complex monitoring and/or debugging mechanisms.

### Routers

Each time a payment data object is received by the core API and saved to its database, a router will redirect it to the destination instance. How this routing takes place depends on the respective router class to be instantiated. Currently two routers are available: **AccountIdRouter** and **ReferenceIdRouter**. However new routers can easily be added by adding subclasses to the *routers.py* file in the core/ directory.
