# Lab 3 – Component Modelling & Architectural Pattern Selection

## Project
### Meal Planning and Diet Management System

## 1. Objective

The objective of this lab is to select a suitable architectural style for the
Meal Planning and Diet Management System and create a UML Component Diagram
showing the major components, interfaces, and interactions.

## 2. Selected Architecture

**Microservices Architecture**

The system is divided into independent services, where each service handles a
specific functionality of the application.

## 3. Main Components

The component diagram contains the following major components:

- User Profile & Preferences
- Dietary Preference Service
- Meal Subscription Service
- Payment & Billing Service
- Meal Planning Service
- Meal Recommendation Service
- User Database
- Subscription & Payment Database
- Meal Database

## 4. Main Functionalities

The system supports the following major functions:

- Manage user profile and preferences
- Manage dietary preferences and allergies
- Browse and manage meal subscriptions
- Make payments and view billing details
- Manage daily meal plans
- View recommended meals

## 5. Component Interactions

The major interactions represented in the component diagram include:

- User → User Profile & Preferences
- User → Meal Subscription Service
- User → Payment & Billing Service
- User → Meal Planning Service
- User Profile & Preferences → User Database
- Dietary Preference Service → User Database
- Meal Subscription Service → Subscription & Payment Database
- Payment & Billing Service → Subscription & Payment Database
- Meal Planning Service → Meal Recommendation Service
- Meal Recommendation Service → Meal Database

## 6. Architecture Justification

Microservices Architecture was selected because the system contains multiple
independent business functions such as user management, dietary preferences,
subscriptions, payments, meal planning, and meal recommendations.

The architecture allows individual services to be developed, maintained, and
scaled independently. It also provides separation between sensitive operations
such as payment processing and other application services.

## 7. Files Included

- `Component_Diagram.pdf` – UML Component Diagram
- `Architecture_Justification.pdf` – Architectural selection and justification

## 8. Tools Used

- Draw.io / UML modelling tool
- PDF export
- GitHub for submission
