import { createQueue } from 'kue';
import { describe, it } from 'mocha';

import createPushNotificationsJobs from './8-job';

const queue = createQueue();

const list = [
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
    },
    {
        phoneNumber: '4153518781',
        message: 'This is the code 12345 to verify your account',
    },
];

describe('createPushNotificationsJobs test', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should return correct no. of jobs', () => {
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });

  it('should return correct job details', () => {
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs[0].data).to.equal({
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    });
  });
}); 
