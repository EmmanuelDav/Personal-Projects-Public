package com.example.myapplication

import android.content.Intent
import android.content.pm.PackageManager
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import com.google.firebase.auth.FirebaseAuth
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        fun Login() {
            //checking if the information is not submitted
            if (email.text.isEmpty() || password.text.isEmpty()) {
                Toast.makeText(this, "Populate both Email and Password", Toast.LENGTH_LONG).show()
            }
            else {
                val auth = FirebaseAuth.getInstance()
                auth.signInWithEmailAndPassword(email.text.toString(), password.text.toString())
                    //Redirection To MainPage(Home)
                    .addOnSuccessListener {
                        var array = arrayOf(android.Manifest.permission.WRITE_EXTERNAL_STORAGE)
                        ActivityCompat.requestPermissions(this, array, 3)
                    }
                    //Updating UI
                    .addOnFailureListener {
                        Toast.makeText(this, "Invalid Login", Toast.LENGTH_LONG).show()
                    }
            }
        }
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        LOGIN.setOnClickListener {
            Login()
        }
        signup.setOnClickListener {
            val SignupInt  = Intent(this , SignUpPage::class.java)
            startActivity(SignupInt)
        }
        }

    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        if(grantResults[0]== PackageManager.PERMISSION_GRANTED && requestCode == 3){
            val mainInt = Intent(this , Home::class.java)
            startActivity(mainInt)
        }
        else{
            FirebaseAuth.getInstance().signOut()
            Toast.makeText(this , "You must give us certain permissions in order to use this app.. Please Re-login", Toast.LENGTH_LONG).show()
        }
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
    }
    }