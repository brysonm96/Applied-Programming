package com.example.dinnerapp

import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val rollButton: Button = findViewById(R.id.button)
        rollButton.setOnClickListener {
            //Call food randomizer method
            rollFood()
        }
    }

    //Function to randomly select food
    private fun rollFood() {
      
        //Food list items
        val meals = listOf("Pizza", "Hamburgers", "Tacos", "Pasta", "Seafood", "Soup","Sandwiches"
        , "Fried Chicken", "Sushi", "Pork chops", "Breakfast", "Steak", "Casserole", "Baked Potatoes" )
        
        //Initialize food variable to random list item
        val chosenFood = meals.random()
        
        //Displays the random selected food to user
        val resultTextView: TextView = findViewById(R.id.textView)
        resultTextView.text = chosenFood.toString()
    }
}
