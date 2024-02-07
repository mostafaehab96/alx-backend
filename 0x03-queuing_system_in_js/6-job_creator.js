const kue = require('kue');

const queue = kue.createQueue();
const jobData = {
  phoneNumber: '01148989290',
  message: 'Hello this is me',
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) console.log(`Error creating job ${err}`);
    console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', () => console.log('Notification job completed'));

job.on('failed', () => console.log('Notification job failed'));
