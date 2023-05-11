import machine
import dht
import utime

# Specify the model coefficients and intercept 
coefficients = -2.8212674826885054
intercept = 151.34381063636422

# Create a DHT11 object and specify the GPIO pin
d = dht.DHT11(machine.Pin(0))

# Continuously read data from the DHT11 sensor and predict the humidity using the loaded model
while True:
    # Read the temperature from the DHT11 sensor
    d.measure()
    temperature = d.temperature()
    true_humidity = d.humidity()

    # Predict the humidity using the loaded model
    start_time = utime.ticks_us()
    humidity = temperature * coefficients + intercept
    end_time = utime.ticks_us()
    execution_time_us = utime.ticks_diff(end_time, start_time)
    
    # Print the predicted humidity and the execution time
    print(f"Temperature: {temperature} C")
    print(f"Predicted Humidity: {humidity:.0f} %")
    print(f"True Humidity: {true_humidity:.0f} %")
    print(f"Execution Time: {execution_time_us} μs")
    print()
    # Wait for 1 second before taking the next reading
    utime.sleep(1)