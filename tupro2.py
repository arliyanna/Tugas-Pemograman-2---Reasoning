# -*- coding: utf-8 -*-
"""Tupro2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NOKohN5dFPdOWQ7Fl8kZuqXmRdcW68cB

**Kelompok LI**
1.   Muhammad Naufal (1301204134)
2.   Arliyanna Nilla (1301200263)
"""

#install library for create file xlsx
!pip install xlsxwriter

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import xlsxwriter

#input data
#Output : Membaca file xlsx dari Excel dan diubah menjadi array (Library pandas)
dataset = pd.read_excel("bengkel.xlsx")
dataset

def importData():
  data = []
  setData = pd.read_excel("bengkel.xlsx")
  for i in range(len(setData['id'])):
    data.append([])
    data[i].append(setData['id'][i])
    data[i].append(setData['servis'][i])
    data[i].append(setData['harga'][i])
  return data

"""**Fungsi Linguistik**

**Kualitas Servis :**

1.   Buruk -> 1 - 45
2.   Normal -> 50 - 75
3.   Baik -> 80 - 100

**Harga :**


1.   Murah -> 1 - 3
2.   Terjangkau - > 4 - 7
3.   Mahal -> 8 - 10
"""

#Procedure Service
#Output : Menampilkan Grafik Fungsi Servis
def StatikServis():
  x1 = [0, 45, 50, 100]
  y1 = [1, 1, 0, 0]

  x2 = [0, 45, 50, 75, 80, 100]
  y2 = [0, 0, 1, 1, 0, 0]

  x3 = [0, 75, 80, 100]
  y3 = [0, 0, 1, 1]

  plt.title(" Service Quality ")
  plt.xlabel("Kualitas")
  plt.plot(x1, y1, label ="Buruk", color = "Red")
  plt.plot(x2, y2, label ="Normal", color = "Yellow")
  plt.plot(x3, y3, label ="Baik", color = "Blue")
  plt.legend()
  plt.xticks(np.arange(min(x1), max(x1)+1, 10.0))
  plt.show()

#Procedure Harga
#Output : Menampilkan Grafik Harga
def StatikHarga():
  x1 = [0, 3, 4, 10]
  y1 = [1, 1, 0 , 0]

  x2 = [0, 3 , 4, 7, 8, 10]
  y2 = [0, 0, 1, 1, 0, 0]

  x3 = [0, 7, 8, 10]
  y3 = [0, 0, 1, 1]

  plt.title("Service Price")
  plt.xlabel("Harga")
  plt.plot(x1, y1, label ="Murah", color = "Orangered")
  plt.plot(x2, y2, label ="Terjangkau", color = "royalblue")
  plt.plot(x3, y3, label ="Mahal", color = "green")
  plt.legend()
  plt.xticks(np.arange(min(x1), max(x1)+1, 1.0))
  plt.show()

def kelayakan():
  x1 = [0, 50, 70, 100]
  y1 = [1, 1, 0, 0]

  x2 = [0, 50, 70, 100]
  y2 = [0, 0, 1, 1]

  plt.title("Kelayakan")
  plt.xlabel("Nilai")
  plt.plot(x1, y1, label ="Tidak Direkomendasi", color = "crimson")
  plt.plot(x2, y2, label ="Direkomendasi", color = "lime")
  plt.legend()
  plt.xticks(np.arange(min(x1), max(x1)+1, 10.0))
  plt.show()

def FuzzyServis(NS): #Menghasilkan output nilai buruk, normal, baik berdasarkan input
  buruk = 0
  #Buruk
  if (NS <= 45):
    buruk = 1
  elif (NS >= 50):
    buruk = 0
  elif (NS <= 45 and NS <= 50):
    buruk = (50-NS)/(50-45)

  normal = 0
  #Normal
  if (NS <= 45 or NS >= 80):
    normal = 0
  elif (NS >= 50 and NS <= 75):
    normal = 1
  elif (NS >= 45 and NS < 50):
    normal = (NS - 45) / (50 - 45)
  elif (NS > 75 and NS < 80):
    normal = (75 - NS) / (80 - 75)
    
  baik = 0
  #Baik
  if (NS <= 75):
    baik = 0
  elif (NS >= 80 and NS <= 100):
    baik = 1
  elif (NS > 75 and NS < 80):
    baik = (NS - 75) / (80 - 75)
  return round(buruk,3), round(normal,3), round(baik, 3)

def FuzzyHarga(NH): #Menghasilkan output harga murah, terjangkau , dan mahal berdasarkan input
  murah = 0
  #Murah
  if (NH <= 3):
    murah = 1
  elif (NH >= 4):
    murah = 0
  elif (NH > 3 and NH < 4 ):
    murah = (4 - NH) / (4 - 3)
  terjangkau = 0
  #terjangkau
  if (NH <= 3 or NH >= 8):
    terjangkau = 0
  elif(NH >= 4 and NH <= 7):
    terjangkau = 1
  elif(NH > 3 and NH < 4):
    terjangkau = (NH - 3) / (4 - 3)
  elif(NH > 7 and NH < 8):
    terjangkau =  (8 - NH) / (8 - 7)
  mahal = 0
  #Mahal
  if (NH <= 7):
    mahal = 0
  elif (NH >= 8 and NH <= 10):
    mahal = 1
  elif (NH  > 7 and NH < 8):
    mahal = (NH - 7)/(8 - 7)
  return round(murah,3), round(terjangkau,3), round(mahal,3)

"""**Fuzzy Rules**
1.   Tidak Direkomdendasi
2.   Direkomendasi 





"""

dataset1 = pd.read_excel("Fuzzy Rules.xlsx")
dataset1

def FuzzyRules(servis, harga): #Membuat array yang berisi aturan yang telah di inferensi
  arrRules = [
      #Buruk, Mahal [0]
      #Normal, Terjangkau [1]
      #Baik, Murah [2]
      #Buruk, Mahal
      ["Tidak Rekomendasi", min(servis[0], harga[0])],
      #Buruk, Terjangkau
      ["Tidak Rekomendasi", min(servis[0], harga[1])],
      #Buruk, Murah
      ["Tidak Rekomendasi", min(servis[0], harga[2])],
      #Normal, Mahal
      ["Tidak Rekomendasi", min(servis[1], harga[0])],
      #Normal, Terjangkau
      ["Tidak Rekomendasi", min(servis[1], harga[1])],
      #Normal, Murah
      ["Rekomendasi", min(servis[1], harga[2])],
      #Baik, Mahal
      ["Tidak Rekomendasi", min(servis[2], harga[0])],
      #Baik, Terjangkau
      ["Rekomendasi", min(servis[2], harga[1])],
      #Baik, Murah
      ["Rekomendasi", min(servis[2], harga[2])],
  ]
  return arrRules

def inferensi(arrRules):
    arrRekomendasi = []
    arrTidakRekomendasi = []
    for i in range(len(arrRules)):
        if arrRules[i][0] == "Rekomendasi":
            arrRekomendasi.append(arrRules[i][1])
        else:
            arrTidakRekomendasi.append(arrRules[i][1])
    return max(arrRekomendasi), max(arrTidakRekomendasi)

def Best10Result(arrResult): #Mencari 10 hasil 
    arrTemp = []
    for i in range(len(arrResult)):
        arrTemp.append(arrResult[i])
    arrTemp.sort(key=lambda arrTemp:arrTemp[1])
    arrTemp.reverse()
    arrTemp = arrTemp[:10]
    print(arrTemp)
    arrResult = []
    return arrTemp

def deffuzyfikasi(arrInferensi):#Mamdani Method
    #x1 = [0, 50, 70, 100]
    #y1 = [1, 1, 0, 0]

    #x2 = [0, 50, 70, 100]
    #y2 = [0, 0, 1, 1]
    left = 0
    right = 0
    result = 0
    mamdani = [10,20,30,40,50,60,70,80,90,100]
    for i in range(len(mamdani)):
      if(mamdani[i] <= 50):
        left = left + (mamdani[i] * arrInferensi[0])
        result = result + arrInferensi[0]
      elif(mamdani[i] >= 70):
        right = right + (mamdani[i] * arrInferensi[0])
        result = result + arrInferensi[1]

    return(right + left) / result

#program main
def main():
  #import data from dataset
  dataBengkel = importData()

  #Display Graphic
  #Statik Servis
  StatikServis()
  print(" ")
  #statik Harga
  StatikServis()
  print(" ") 
  #kelayakan
  kelayakan()
  print(" ")

  #Fuzzy Servis
  arrFuzzyServis = []
  for i in range(len(dataBengkel)):
    arrFuzzyServis.append(FuzzyServis(dataBengkel[i][1]))
  #Fuzzy Harga
  arrFuzzyHarga = []
  for i in range(len(dataBengkel)):
    arrFuzzyHarga.append(FuzzyHarga(dataBengkel[i][2]))

  #process for get array id bengkel and defuzzy value
  arrResult = []
  for i in range(len(dataBengkel)):
    #for get rules from inferensi
    Fuzzy = FuzzyRules(arrFuzzyServis[i], arrFuzzyHarga[i])
    #for get value kelayakan for calculate defuzzy
    inference = inferensi(Fuzzy)
    #for get defuzzy value
    arrResult.append([i+1, deffuzyfikasi(inference)])

  #for get best 10 result
  arrResult = Best10Result(arrResult)
  #for print best 10 result
  print(" id", "|", arrResult)
  #create file xlsx
  WorkBook = xlsxwriter.Workbook('Hasil.xlsx')
  #create sheet
  sheet = WorkBook.add_worksheet("Hasil")
  #create format
  format = WorkBook.add_format()
  format.set_bold()
  format.set_font_color('red')
  #write header
  sheet.write(0,0,"id",format)
  sheet.write(0,1,"Hasil",format)
  #write data
  for i in range(len(arrResult)):
    sheet.write(i+1,0,arrResult[i][0])
    sheet.write(i+1,1,arrResult[i][1]) 
  WorkBook.close()

main()