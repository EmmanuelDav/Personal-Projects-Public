package com.example.myapplication

import android.app.Activity
import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.drawable.BitmapDrawable
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.MediaStore
import android.widget.Toast
import androidx.core.app.ActivityCompat
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.ktx.Firebase
import com.google.firebase.storage.FirebaseStorage
import kotlinx.android.synthetic.main.activity_add_story.*
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.activity_sign_up_page.*

class SignUpPage : AppCompatActivity() {
    private lateinit var auth: FirebaseAuth

    var PhotoSelected = false
    var photouri : Uri?= null

    //user object for the database
    data class User ( val email : String , val Admin:  Boolean ,  val UserProfilepicuri : String ,val password :String , val likes : Int)


    fun select_photo () {
        val photoselectionintent = Intent(Intent.ACTION_PICK)
        photoselectionintent.type ="image/*"
        startActivityForResult(photoselectionintent , 33)
    }

    fun databaseinteraction( url : String){
        //creating the user inside of firebase database
        val databaseref =FirebaseDatabase.getInstance().reference.child("/Users/${auth.currentUser!!.uid}")
        val userdata = User(auth.currentUser!!.email.toString(), false, url.toString(), PasswordSignup.text.toString(), 0)
        val databaseinit = databaseref.setValue(userdata)
        databaseinit.addOnSuccessListener {
            Toast.makeText(this , "Database upload comp" , Toast.LENGTH_LONG).show()
            val action1 = Intent(this , Home::class.java)
            startActivity(action1)
        }
        databaseinit.addOnFailureListener {
            Toast.makeText(this , "Database interaction Issue", Toast.LENGTH_LONG).show()
        }

    }


    fun imageupload(){
      //Uploading user profile picture to storage
        val storageinfo = FirebaseStorage.getInstance().getReference().child("${EmailSignup.text.toString()}/profilepic")
        val imageuploadtask = storageinfo.putFile(photouri!!)
        imageuploadtask.addOnSuccessListener {
            imageurldownload()
        }
        imageuploadtask.addOnFailureListener{
            Toast.makeText(this, "Issue Uploading Image" , Toast.LENGTH_LONG).show()

        }
    }

    fun imageurldownload(){
        //downloading the location of the uploaded image
        val storageinfo = FirebaseStorage.getInstance().getReference().child("${EmailSignup.text.toString()}/profilepic")
        val uridownload = storageinfo.downloadUrl
        uridownload.addOnSuccessListener {
            databaseinteraction(it.toString())
        }
        uridownload.addOnFailureListener {
            Toast.makeText(this, "Issue with Downloading Url", Toast.LENGTH_LONG).show()
        }

    }


    fun SignUp(){
        //Var For error conditions
        var Holder = ""

        if (EmailSignup.text.isEmpty() || PasswordSignup.text.isEmpty() || ConfirmSignup.text.isEmpty()){
            Holder += " All Boxes must be Populated.."
        }
        if (PasswordSignup.text.toString() != ConfirmSignup.text.toString()){
            Holder += " Passwords Didn't Match"
            PasswordSignup.setText("")
            ConfirmSignup.setText("")
        }
        if (PasswordSignup.text.length<6){
            Holder +="..Password must be at least 6 characters"
        }
       //updating ui if conditions not met
        if (Holder.length >0){
            Toast.makeText(this , Holder , Toast.LENGTH_LONG).show()
        }
        else if (PhotoSelected== false){
            Toast.makeText(this , "Make Sure You Select A Profile Photo" , Toast.LENGTH_LONG).show()
        }
        else {
            val createtask = auth.createUserWithEmailAndPassword(
                EmailSignup.text.toString(), PasswordSignup.text.toString()
            )
            createtask.addOnSuccessListener {
                imageupload()

            }
            createtask.addOnFailureListener {
                Toast.makeText(this, "Error creating User" , Toast.LENGTH_LONG).show()
            }
        }
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_sign_up_page)
        auth = FirebaseAuth.getInstance()
        Clickhere.setOnClickListener{
            select_photo()
        }

        SignupButton.setOnClickListener {
            SignUp()
        }
    }
    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        if(grantResults[0]== PackageManager.PERMISSION_GRANTED && requestCode == 0){
            val mainaction = Intent(this , Home::class.java)
            startActivity(mainaction)
        }
        else{
            Toast.makeText(this , "You must give us certain permissions in order to use this app.. Please go to the Main Page and sign in to proceed..", Toast.LENGTH_LONG).show()
        }
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
    }
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        if (requestCode == 33 && resultCode== Activity.RESULT_OK && data != null){
            PhotoSelected = true
            val uridata  = data.data
            val bitmapforphoto = MediaStore.Images.Media.getBitmap(contentResolver ,uridata)
            val bitmapdraw = BitmapDrawable(bitmapforphoto)
            //gather photo data
            photouri = uridata
            profileimagecard.alpha= 1f
            Profileimage.setImageResource(0)
            Profileimage.setBackgroundDrawable(bitmapdraw)
        }


        super.onActivityResult(requestCode, resultCode, data)
    }
}
