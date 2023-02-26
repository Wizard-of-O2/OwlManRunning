import { env } from '$env/dynamic/private';
import amqp from 'amqplib';

export const sendToQueue = async (msg: string) => {
  const queue = 'omr';

	const conn = await amqp.connect(`amqp://${env.AMQP_HOST}`);
	const chan = await conn.createChannel();

	await chan.assertQueue(queue, {
		durable: true
	});
  chan.sendToQueue(queue, Buffer.from(msg));
  console.log('[x] sendToQueue');

	setTimeout(() => {
		conn.close();
	}, 500);
};
