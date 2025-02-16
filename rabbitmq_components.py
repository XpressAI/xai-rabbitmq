from xai_components.base import InArg, OutArg, InCompArg, Component, BaseComponent, xai_component
import pika


@xai_component
class RabbitMQConnect(Component):
    broker: InArg[str]
    port: InArg[int]
    username: InArg[str]
    password: InArg[str]
    vhost: InArg[str]

    def execute(self, ctx) -> None:
        if self.username.value is not None:
            credentials = pika.PlainCredentials(self.username.value, self.password.value)
            parameters = pika.ConnectionParameters(
                host=self.broker.value,
                port=self.port.value,
                virtual_host=self.vhost.value if self.vhost.value is not None else '/',
                credentials=credentials)
            client = pika.BlockingConnection(parameters)
        else:
            parameters = pika.ConnectionParameters(
                host=self.broker.value,
                port=self.port.value,
                virtual_host=self.vhost.value if self.vhost.value is not None else '/')
            client = pika.BlockingConnection(parameters)

        ctx['rabbitmq_client'] = client
        ctx['rabbitmq_channel'] = client.channel()

@xai_component
class RabbitMQPublish(Component):
    queue: InArg[str]
    routing_key: InArg[str]
    exchange: InArg[str]
    message: InArg[str]

    def execute(self, ctx) -> None:
        channel = ctx['rabbitmq_channel']

        if ctx.get('rabbitmq_queue') is None:
            channel.queue_declare(queue=self.queue.value)
            ctx['rabbitmq_queue'] = self.queue.value

        exchange = '' if self.exchange.value is None else self.exchange.value
        routing_key = '' if self.routing_key.value is None else self.routing_key.value

        channel.basic_publish(exchange=exchange, routing_key=routing_key, body=self.message.value)


@xai_component
class RabbitMQConsume(Component):
    on_message: BaseComponent
    queue: InArg[str]
    exchange: InArg[str]
    routing_key: InArg[str]
    message: OutArg[str]

    def execute(self, ctx) -> None:
        channel = ctx['rabbitmq_channel']

        if ctx.get('rabbitmq_queue') is None:
            channel.queue_declare(queue=self.queue.value)
            ctx['rabbitmq_queue'] = self.queue.value

        channel.basic_consume(
            queue=self.queue.value,
            on_message_callback=lambda ch, meth, prop, body: self.process_message(ctx, ch, meth, prop, body))


    def process_message(self, ctx, channel, method, properties, body):
        self.message.value = body.decode('utf-8')
        ctx['rabbitmq_message'] = body
        ctx['rabbitmq_properties'] = properties

        self.on_message.do(ctx)

        channel.basic_ack(delivery_tag=method.delivery_tag)


@xai_component
class RabbitMQStartConsuming(Component):

    def execute(self, ctx) -> None:
        channel = ctx['rabbitmq_channel']

        try:
            channel.start_consuming()
        except Exception as e:
            print(e)


@xai_component
class RabbitMQDisconnect(Component):

    def execute(self, ctx) -> None:
        client = ctx['rabbitmq_client']

        try:
            client.close()
        except Exception as e:
            print(e)
