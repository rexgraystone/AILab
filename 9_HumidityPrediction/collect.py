import machine
import dht
import time

# Create a DHT11 object and specify the GPIO pin
d = dht.DHT11(machine.Pin(0))

# Open the data file for writing
with open('data.txt', 'w') as f:

    # Write the header row
    f.write('Temperature,Humidity\n')

    i = 1000
    # Continuously read data from the DHT11 sensor and write it to the file
    while i >= 0:
        # Read the temperature and humidity from the DHT11 sensor
        d.measure()
        temperature = d.temperature()
        humidity = d.humidity()
        print(f"Temperature: {temperature} c")
        print(f"Humidity: {humidity}%")
        print()

        # Write the temperature and humidity to the file
        f.write(f'{temperature},{humidity}\n')

        # Wait for 1 second before taking the next reading
        time.sleep(1)
        i = i - 1