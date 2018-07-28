# MoMo 

![pylint: 9.21](https://img.shields.io/badge/pylint-9.21-green.svg)

### Motivation
This project was created as a practical Python challenge for a job application.

#### Problem Definition

*Note: The problem definition has been (non-exhaustively) rewritten in my own words. Misconceptions or -interpretations are entirely possible, if not likely.*

Implement a payment processing app that 

1. *provides* data from multiple payment service providers (PSPs), differing in **data formats** (XML, CSV, etc.) and **communication channels** (Web APIs, FTP dumps, email, etc.). Each data set does however include an **account_id** (referencing the corresponding SaaS instance, see below) and a **reference_id** (referencing the individual customer, initating the transaction).
2. *standardizes* the received data and **stores** (and logs) it for compliance reasons.
3. *'routes'* the standardized payment data to its destination. This destination is a **SaaS instance** (run in a seperate container) of software used for managing products and customers in the renewable energy sector. An instance that receives payment data in the standardized form will be able to process it and provide electricity according to the corresponding value. The application should be able to route payments by account_id **and** reference_id.

The focus should lie on the **simplicity** and **extendability** of the design, specifically with regard to the implementation of new PSP adapters and routing mechanisms.
