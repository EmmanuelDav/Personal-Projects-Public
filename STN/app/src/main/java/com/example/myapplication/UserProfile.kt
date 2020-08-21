package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_user_profile.*

class UserProfile : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_user_profile)

        //Helping New users Get use to the U.I
        HelpButtonProfile.setOnClickListener {
            Toast.makeText(this, "Click The Icons Next to the Fields to Update/Enter Your information" , Toast.LENGTH_LONG).show()
        }
    }
}