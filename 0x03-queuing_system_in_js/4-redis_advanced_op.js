import { createClient, print } from 'redis';

const client = createClient()
  .on('error', (error) => console.log(`Redis client not connected to the server: ${error}`))
  .on('connect', () => console.log(('Redis client connected to the server')));

const hashKey = 'HolbertonSchools';

const hashValues = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

Object.entries(hashValues).forEach((hash, index) => {
  const [key, value] = hash;
  client.hset(hashKey, key, value, print);
});

client.hgetall(hashKey, (err, data) => {
  // eslint-disable-next-line no-unused-expressions
  err ? console.log(err) : console.log(data);
});
