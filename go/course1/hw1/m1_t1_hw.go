/*
Задача №1
Вход:
    расстояние(50 - 10000 км),
    расход в литрах (5-25 литров) на 100 км и
    стоимость бензина(константа) = 48 руб

Выход: стоимость поездки в рублях
*/
package main

import "fmt"

func main() {

	const fuelPrice = 48.0
	var dist, consumption float32

	fmt.Println("Введите дистанцию в км от 50 до 10000")
	fmt.Scanf("%g/n", &dist)
	fmt.Println("Введите расход в литрах от 5 до 25")
	fmt.Scanf("%g/n", &consumption)

	fmt.Printf("Стоимость поездки, составила: %.2f руб \n", (dist / 100 * consumption * fuelPrice))

}
