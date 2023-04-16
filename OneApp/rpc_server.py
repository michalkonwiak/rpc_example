import json
import os
import pika


def rpc_server():
    connection = pika.BlockingConnection(
        pika.URLParameters(
            "amqp://admin:jamnik677@rabbitmq:5672"
        )
    )

    channel = connection.channel()
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="projekt", on_message_callback=on_request)

    print(" [x] Awaiting RPC requests")
    channel.start_consuming()


def on_request(ch, method, props, body):
    data = str(body)

    print(f"Got rpc type with data {data}")

    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body="123"
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
    rpc_server()
