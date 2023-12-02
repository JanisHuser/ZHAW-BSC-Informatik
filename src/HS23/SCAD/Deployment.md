# Deployment

- Deployment of Helm chart to kubernetes cluster

## Requirements

### Expressivity

- Holistic application models vs. purely instructive scripts
- In principle *TOSCA/CAMEL* in practise: *Helm, SAM, Etc,...*

### Optimality

- Application runtime requirements X inftrastructure capabilities

Global: Cloud service selection based on Critiera [C]

Local: Assignment of workload (e.g. containers) or components (e.g. autonomous managers [AM] managing resources [R]) per cloud

![](images/deployment/IMG_0331.jpeg)

### Transactionality

- Hight- Availability (Seamlessness), rollback, versioning, staging, dry runs

Built in seamless *rolling updates* and *rollback*

### Immutability

- Indirect modification through, e.g. git push, single-system images

Def. immutability: system does not change after deployment

- immutable infrastructure, changes via continous deployment & delivery
- consistency, cattle vs pet stateless containers
- intrusion resilence (easy to recover)

### Reproducibility

- Multiple instances with exact same behaviour or controlled deviation

Authoritiative source needed for any public dependencies

Master source: Software Heritage append-only archive
-> unique cross-force fingerprinting of repositories

**Reproducible builds**: It should be possible to reproduce, byte for byte, every build of every package

![](images/deployment/IMG_0330.jpeg)


### Architectural Requirements

    Deployment <- -> Design / Architecture

- Artefact types: short-running, long-running containers; functions; flows
- Architectural preparation
    - cloud-nativeness
    - downward compatibility
    - metrics provisioning
- Pre-deployment planning (sizing, etc,.) + checks / analytics
- Automated deployment
- Post-deployment observability (resizing, autoscaling adjustments etc.)

![](images/deployment/IMG_0332.jpeg)
![](images/deployment/IMG_0333.jpeg)

## TOSCA (Topology and Orchestration Specification for Cloud Applications)

![Topology Template](images/deployment/IMG_0334.png)

TOSCA is an open standard language used to describe cloud applications and their components, including their relationships, dependencies, and deployment configurations. It facilitates the automation of cloud application management tasks such as deployment, scaling, and configuration.

Key benefits of using TOSCA include:

1. **Portability:** TOSCA enables cloud applications to be defined and deployed across different cloud platforms, promoting portability and reducing vendor lock-in.

2. **Automation and Reusability:** TOSCA templates can be reused to automate cloud application deployment and management tasks, saving time and effort.

3. **Standardized Language:** TOSCA provides a common language for defining cloud applications, fostering collaboration and communication among developers and operators.

4. **Extensible Framework:** TOSCA supports extensions for specific use cases or vendor-specific requirements, allowing for customization and flexibility.

5. **Integration with Tools and Platforms:** TOSCA integrates with various cloud management tools and platforms, providing a comprehensive solution for cloud application management.