import { createQueue } from 'kue';

const queue = createQueue();

const obj = {
  phoneNumber: '0770416102',
  message: 'Here we go!',
}

const job = queue.create('push_notification_code', obj).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
  }
);

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
