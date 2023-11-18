# Architekturen

## XaaS Everything as a Service

*Application-specific*

SaaS - Software

DaaS - Data

DBaaS - Database

*Cloud Services*

IaaS - Infrastrucutre

PaaS - platform, CaaS  - Containers

Serverless - FaaS, (+CaaS), BaaS

## Function as a Service (FaaS)

Stateless & Shortlived

high elastic scalability

triggered by external events

single functionality & responsiblity

pay per use

Function can for example run in a CaaS (Container)

## Backend as a Service (BaaS)

FaaS hat nur Computing Ressourcen (fast) kein Storage.

Daher BaaS welche stateful ist mit low latency

Dafür zusätliche kosten.

Databases, Message brokers …

## Platform as a Service (PaaS)

- Long Lived
- More Flexible resource models
- Language constrained


## Container as a Service (CaaS)

- Long Lived
- More flexible resource models
- unconstrained runtime
- "serverless CaaS": short-lived, resource constraints
- often underlying PaaS/FaaS, especially "FaaS with contaniers"