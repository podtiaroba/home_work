#https://github.com/Bandydan/php/blob/master/06_Practice_practice_practice.md

#Задача 1. Курьер. В какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру

flats_per_floor = 8#кол-во квартир на этаже
floors = 24#этажность дома
front_door = (flats_per_floor) * (floors)#кол-во квартир в подъезде

apartment_number = int(input("Apartment number: "))#номер квартиры
current_floor = 1#текущий этаж
entrance_number = 1#текущий подъезд

while apartment_number > front_door*entrance_number:
  entrance_number += 1

apartment_number -= front_door*(entrance_number-1)

while current_floor <= floors:
  if apartment_number <= current_floor * flats_per_floor:
      print ("Floor {}, entrance number {}.".format(current_floor, entrance_number))
      break
  current_floor +=1
  