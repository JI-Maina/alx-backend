import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to te server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server')
});

function setNewSchools() {
  client.HSET('HolbertonSchools', 'Portland', '50', print);
  client.HSET('HolbertonSchools', 'Seattle', '80', print);
  client.HSET('HolbertonSchools', 'New York', '20', print);
  client.HSET('HolbertonSchools', 'Bogota', '20', print);
  client.HSET('HolbertonSchools', 'Cali', '40', print);
  client.HSET('HolbertonSchools', 'Paris', '2', print);
}

function displaySchools() {
  client.HGETALL('HolbertonSchools', (err, res) => {
    console.log(res);
  });
}

setNewSchools();
displaySchools();
