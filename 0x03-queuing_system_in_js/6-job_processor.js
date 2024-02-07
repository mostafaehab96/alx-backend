const kue = require('kue');

const queue = kue.createQueue();

const sendNotifications = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotifications(phoneNumber, message);
  done();
});
