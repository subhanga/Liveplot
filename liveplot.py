import serial
import matplotlib.pyplot as plt
import numpy as np


def show_all():
  plt.clf()
  plt.subplot(1, 3, 1)
  plt.xlim(0, 4)
  plt.ylim(0, 100)
  plt.scatter(disp1_u, force1_u)
  plt.grid(True)
  plt.subplot(1, 3, 3)
  plt.xlim(0, 4)
  plt.ylim(0, 100)
  plt.scatter(disp2_u, force2_u)
  plt.show()
  plt.grid(True)


plt.ion()
fig = plt.figure()

force1 = list()
disp1 = list()
force1_u = list()
disp1_u = list()

force2 = list()
disp2 = list()
force2_u = list()
disp2_u = list()

i = 0
j = 0
k = 0
limit = 1000

ser = serial.Serial('COM6', 9600)
ser.close()
ser.open()

sample = 40000  # YOU HAVE TO CHANGE THIS PART

while True:
  if k < limit:
      plt.clf()
      data = ser.readline()
      dec = data.decode()
      split = dec.split(",")

      split[0] = float(split[0])
      split[1] = float(split[1])

      force1.append(split[0])
      disp1.append(split[1])
      force1_u.append(split[0])
      disp1_u.append(split[1])

      plt.subplot(3, 1, 1)
      plt.grid(True)

      if i > sample:
          force1.pop(0)
          disp1.pop(0)

      plt.xlim(0,4)
      plt.ylim(0,10)

      plt.xlabel("Displacement 01")
      plt.ylabel("Force 01")
      i += 1
      plt.scatter(disp1, force1)

      split[2] = float(split[2])
      split[3] = float(split[3])

      force2.append(split[2])
      disp2.append(split[3])
      force2_u.append(split[2])
      disp2_u.append(split[3])

      plt.subplot(3, 1, 3)
      plt.grid(True)

      if j > sample:
          force2.pop(0)
          disp2.pop(0)

      plt.xlim(0, 4)
      plt.ylim(0, 10)

      plt.xlabel("Displacement 02")
      plt.ylabel("Force 02")
      j += 1
      plt.scatter(disp2, force2)

      plt.show()
      plt.pause(0.0001)  # Note this correction
      #print(force1_u)

  else:
      show_all()
      break

  k = k + 1


