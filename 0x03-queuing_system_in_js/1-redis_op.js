import { createClient, print } from 'redis';

const client = createClient()
  .on('error', (error) => console.log(`Redis client not connected to the server: ${error}`))
  .on('connect', () => console.log(('Redis client connected to the server')));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (data, err) => {
    // eslint-disable-next-line no-unused-expressions
    err ? console.log(err) : console.log(data);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
