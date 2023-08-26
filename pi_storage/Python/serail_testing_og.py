import serial
import time

serial_port = '/dev/ttyACM0'
baud_rate = 115200


ser = serial.Serial(serial_port, baud_rate, timeout=1) #connect to ser
x_velocities = [0] #m/s
y_velocities = [0] #m/s
t = 0.001 #sec
count = 0
x_velocity = 0
y_velocity = 0


try:
			
	while True:
					
			data = ser.readline().decode('utf-8').strip() #read from serial
			data_lst = data.split(",")
			cleaned_lst = [value.strip() for value in data_lst]
			x_accel = float(cleaned_lst[0])
			y_accel = float(cleaned_lst[1])
					
			if data:
						
				x_velocity = x_velocities[count] + (x_accel * t)
				x_velocities.append(x_velocity)
				y_velocity = y_velocities[count] + (y_accel * t)
				y_velocities.append(y_velocity)
				count += 1
						
			print("Recieved data from serial port: ", round(x_velocity, 3),
			round(y_velocity, 3)) 
			time.sleep(0.001)
					

except KeyboardInterrupt:
	print("Closing the serial port.")
	ser.close()
