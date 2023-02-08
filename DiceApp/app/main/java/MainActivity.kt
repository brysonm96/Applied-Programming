package com.example.diceapp

import android.os.Bundle
import android.widget.Button
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private fun rollDice() {
        //Create six-sided dice object
        val dice = Dice(6)
        val diceRoll = dice.roll()

        val diceImage: ImageView = findViewById(R.id.imageView)

        //Conditions that display image bases on roll
        when (diceRoll) {
            1 -> diceImage.setImageResource(R.drawable.dice_1)
            2 -> diceImage.setImageResource(R.drawable.dice_2)
            3 -> diceImage.setImageResource(R.drawable.dice_3)
            4 -> diceImage.setImageResource(R.drawable.dice_4)
            5 -> diceImage.setImageResource(R.drawable.dice_5)
            6 -> diceImage.setImageResource(R.drawable.dice_6)
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val rollButton: Button = findViewById(R.id.button)
        rollButton.setOnClickListener {
            rollDice()
        }
    }
}

//Used to test multiple cases, ignore
//fun main() {
    //val myFirstDice = Dice(6)
    //val rollResult = myFirstDice.roll()
    //val luckyNumber = 4

    //when (rollResult) {
        //luckyNumber -> println("You won!")
        //1 -> println("So sorry! You rolled a 1. Try again!")
        //2 -> println("Sadly, you rolled a 2. Try again!")
        //3 -> println("Unfortunately, you rolled a 3. Try again!")
        //5 -> println("Don't cry! You rolled a 5. Try again!")
        //6 -> println("Apologies! You rolled a 6. Try again!")
    //}
//}

class Dice(private val numSides: Int) {
    fun roll(): Int {
        return (1..numSides).random()
    }
}
