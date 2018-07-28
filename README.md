# MoMo 

![pylint: 9.21](https://img.shields.io/badge/pylint-9.21-green.svg)

### Motivation
This project was created as a practical Python challenge for a job application.

#### Problem Definition

*Note: I have rewritten the following problem definition in my own words. Misconceptions or -interpretations are entirely possible, if not likely.*

Implement a payment processing app that 

1. *accepts* data from multiple payment service providers, differing in **data formats** (XML, CSV, etc.) and **communication channels** (Web APIs, FTP dumps, email, etc.)
2. *standardizes* the received data and **stores** (and logs) it for compliance reasons
3. *'routes'* the standardized payment data to its destination. This destination is a **SaaS instance** (run in a seperate container) of software used for managing products and customers in the renewable energy sector.
