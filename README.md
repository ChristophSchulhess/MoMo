# MoMo 
## Payment Processing App

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="76" height="20"><linearGradient id="b" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="a"><rect width="76" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#a)"><path fill="#555" d="M0 0h41v20H0z"/><path fill="#97CA00" d="M41 0h35v20H41z"/><path fill="url(#b)" d="M0 0h76v20H0z"/></g><g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="110"><text x="215" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="310">pylint</text><text x="215" y="140" transform="scale(.1)" textLength="310">pylint</text><text x="575" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="250">9.21</text><text x="575" y="140" transform="scale(.1)" textLength="250">9.21</text></g> </svg>

### Motivation
This project was created as a practical Python challenge for a job application.

### Problem Definition

We have recently chosen to offer our internal software as a SaaS (software as a service) product to outside partners. Our software enables other renewable energy companies to manage their products and customers. A huge part of this involves accepting payments through financial institutions like telcos, mobile money aggregators, banks, card payments aggregators etc. A direct integration with these entities allows us to deliver the required service to our customers. For instance, a customer sends $2 to our bank account and we are required to immediately process that transaction so that we can send them a token worth $2 of electricity. Each payment partner uses different technologies, they range from REST based APIs, SOAP APIs, CSV dumps via FTP, Emails etc.

In order to facilitate a SaaS architecture we implemented a single application to process all payments, called MoMo. This single app is responsible for processing and then routing payments to the relevant instances (each of our partners are given their own instance of the software in a separate container).
In light of this, design a sort of 'skeleton' version of MoMo. You are to build the underlying models so that another engineer can easily and cleanly create all the controllers and front-end magic at a later date.

For this challenge focus on the following:

1. The model structure: Your application should be aware of Partners and Payments, as well as any other models that make sense to you. Note that we receive the payment data in all sorts of formats from our payment partners; we need to store everything for compliance purposes (some logged) but we also want to store it in a standardized way. By standardizing it we can then send identically structured data downstream to SaaS instances. Payments sent by partners will always have a reference_number and an account_number. The reference_number uniquely identifies the individual customer, the account_number uniquely identifies the company/partner/entity who is receiving the payment (eg. one of our SaaS partners).

2. The routing structure: A payment partner can have a number of accounts set up for our different downstream SaaS instances. For example, instance 1 and instance 2 might both accept payments from Africa Bank. So we have one API integration with Africa Bank but it sends us payments with unique identifiers for instance 1 and instance 2. Your structure should take these instances into account and how this 'routing' data is going to be stored so that the controllers can route payments to their destined instances. Payments can be routed by either reference_number or account_number. When implementing the routing structure focus on simplicity and extensibility (future use cases might arise where we route based on other attributes of the payment).

We want to see your model design and what behaviour you think these models can have to make the other engineers' work as easy as possible. Focus on the design/structure of your code, rather than just getting it working. You can design your own models or use an ORM of your choice e.g django.db.models.Model
