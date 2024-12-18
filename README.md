<p align="center">
  <a href="https://github.com/XpressAI/xircuits/tree/master/xai_components#xircuits-component-library-list">Component Libraries</a> •
  <a href="https://github.com/XpressAI/xircuits/tree/master/project-templates#xircuits-project-templates-list">Project Templates</a>
  <br>
  <a href="https://xircuits.io/">Docs</a> •
  <a href="https://xircuits.io/docs/Installation">Install</a> •
  <a href="https://xircuits.io/docs/category/tutorials">Tutorials</a> •
  <a href="https://xircuits.io/docs/category/developer-guide">Developer Guides</a> •
  <a href="https://github.com/XpressAI/xircuits/blob/master/CONTRIBUTING.md">Contribute</a> •
  <a href="https://www.xpress.ai/blog/">Blog</a> •
  <a href="https://discord.com/invite/vgEg2ZtxCw">Discord</a>
</p>






<p align="center"><i>Xircuits Component Library to interface with 
RabbitMQ! Build robust messaging and queuing workflows.</i></p>

---

## Xircuits Component Library for RabbitMQ

This library enables Xircuits to integrate with RabbitMQ for building messaging-based workflows. It provides components to connect, publish, consume, and manage messages in RabbitMQ queues efficiently.

## Table of Contents

- [Preview](#preview)
- [Prerequisites](#prerequisites)
- [Main Xircuits Components](#main-xircuits-components)
- [Try the Examples](#try-the-examples)
- [Installation](#installation)

## Preview

### The Example:

<img src="https://github.com/user-attachments/assets/989f0754-ba3f-4b4c-b05c-fac88c2edffa" alt="rabbitmq_sample"/>

### The Result:


<img src="https://github.com/user-attachments/assets/b930cdf0-46ca-48ca-ae4f-c4d0aa106d17" alt="rabbitmq_sample_result" />

## Prerequisites

Before you begin, you will need the following:

1. Python3.9+.
2. Xircuits.
3. RabbitMQ

## Main Xircuits Components

### RabbitMQConnect Component:  
Connects to a RabbitMQ broker with optional credentials (username, password). Initializes the RabbitMQ client and channel for message operations.  

<img src="https://github.com/user-attachments/assets/edb4be11-f037-4c1a-9885-e87f0d6deec6" alt="RabbitMQConnect" width="200" height="150" />

### RabbitMQPublish Component:  
Publishes a message to a specified queue, exchange, or routing key. If the queue does not exist, it is created automatically.  

<img src="https://github.com/user-attachments/assets/9e12bc0c-49a8-4ed1-8905-ec96a178f249" alt="RabbitMQPublish" width="200" height="150" />

### RabbitMQConsume Component:  
Consumes messages from a queue and triggers a connected component (`on_message`) for processing. Acknowledges messages automatically after processing.  

## Try The Examples

We have provided an example workflow to help you get started with the RabbitMQ component library. Give it a try and see how you can create custom RabbitMQ components for your applications.

### RabbitMQ Example  
This example demonstrates how to connect to a RabbitMQ server, consume messages from a queue, modify them by appending extra text, and publish the modified messages to another queue. It also prints the processed messages for verification.

## Installation
To use this component library, ensure that you have an existing [Xircuits setup](https://xircuits.io/docs/main/Installation). You can then install the RabbitMQ library using the [component library interface](https://xircuits.io/docs/component-library/installation#installation-using-the-xircuits-library-interface), or through the CLI using:

```
xircuits install rabbitmq
```
You can also do it manually by cloning and installing it:
```
# base Xircuits directory
git clone https://github.com/XpressAI/xai-rabbitmq xai_components/xai_rabbitmq
pip install -r xai_components/xai_rabbitmq/requirements.txt
```

## RabbitMQ Local Setup

To set up RabbitMQ locally for testing:

1. **Install RabbitMQ**:
   - On **Ubuntu/Debian**:
     ```bash
     sudo apt update && sudo apt install rabbitmq-server -y
     ```
   - On **Windows**:
     Download and install RabbitMQ and Erlang from the [official RabbitMQ website](https://www.rabbitmq.com/install-windows.html).

2. **Start RabbitMQ**:
   - On Linux:
     ```bash
     sudo systemctl start rabbitmq-server
     sudo systemctl enable rabbitmq-server  # Optional: Auto-start on boot
     ```
   - On Windows: Start RabbitMQ as a service via `services.msc` or the command prompt.

3. **Access RabbitMQ**:
   - Open the RabbitMQ Management UI at [http://localhost:15672](http://localhost:15672).
   - Default login:
     - Username: `guest`
     - Password: `guest`

4. **Run the Xircuits Example**:
   - Create the `testing` and `testing_reply` queues in RabbitMQ.
   - Execute the Xircuits example to consume and process messages.