package com.example.myapplication

import android.app.Activity
import android.content.Intent
import android.graphics.drawable.BitmapDrawable
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.MediaStore
import android.widget.Toast
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.storage.FirebaseStorage
import com.google.firebase.storage.StorageMetadata
import com.google.firebase.storage.StorageReference
import com.google.firebase.storage.ktx.storageMetadata
import kotlinx.android.synthetic.main.activity_add_story.*
import kotlinx.android.synthetic.main.activity_sign_up_page.*
import java.util.*
data class timeline(val Storageref :StorageReference)
class AddStory : AppCompatActivity() {

    var PhotoSelected = false
    var photouri : Uri?= null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val auth = FirebaseAuth.getInstance()
        setContentView(R.layout.activity_add_story)

        fun selectphoto() {
            val photoselectionintent = Intent(Intent.ACTION_PICK)
            photoselectionintent.type ="image/*"
            startActivityForResult(photoselectionintent , 555)
        }

        fun publicupload() {

            //photo metadata
            var metadataforpublic = storageMetadata {
                setCustomMetadata("Name", NameEntry.text.toString())
                setCustomMetadata("Date", DateEntry.text.toString())
                setCustomMetadata("Story", StoryEntry.text.toString())
                setCustomMetadata("Phone Number", PhoneNumberEntry.text.toString())
                setCustomMetadata("Email", EmailEntry.text.toString())
                setCustomMetadata("Location", LocationEntry.text.toString())
                setCustomMetadata("Relationship", RelationshipEntry.text.toString())
                setCustomMetadata("Likes", "0")
                setCustomMetadata("Reports", "0")
                setCustomMetadata("UID", FirebaseAuth.getInstance().currentUser!!.uid)
            }
            //generating random filename
            val filename = UUID.randomUUID().toString()
            //ref
            val publicstorageref = FirebaseStorage.getInstance().getReference()
                .child("MainTimeline/${auth.currentUser!!.uid}.${filename}")

            //upload
            val public_uploadtask = publicstorageref.putFile(photouri!!, metadataforpublic)
            public_uploadtask.addOnSuccessListener {


                Toast.makeText(
                    this,
                    "Photo Successfully Uploaded to Public timeline.",
                    Toast.LENGTH_LONG
                ).show()
                PostButton.isEnabled = true

            }





            }



        fun personalupload(){
            //photo metadata
            var metadataforpersonal = storageMetadata{
                setCustomMetadata("Name"  , NameEntry.text.toString())
                setCustomMetadata("Date" , DateEntry.text.toString())
                setCustomMetadata("Story" , StoryEntry.text.toString())
                setCustomMetadata("Phone Number" , PhoneNumberEntry.text.toString())
                setCustomMetadata("Email" , EmailEntry.text.toString())
                setCustomMetadata("Location" , LocationEntry.text.toString())
                setCustomMetadata("Relationship" , RelationshipEntry.text.toString())
                setCustomMetadata("Reports" , "0")
            }
            //generating random filename
            val filename = UUID.randomUUID().toString()
            //ref
            val personalstorageref = FirebaseStorage.getInstance().getReference().child("${auth.currentUser!!.email}/Posts/${filename}")
            //upload
            val Personal_uploadtask = personalstorageref.putFile(photouri!! , metadataforpersonal)
            Personal_uploadtask.addOnSuccessListener {
                publicupload()

            }
            Personal_uploadtask.addOnFailureListener {
                Toast.makeText(this, "Issue Uploading Story" , Toast.LENGTH_LONG).show()
                PostButton.isEnabled=true
            }

        }

        fun PostStory(){
            //Checking To make sure requirements are met
            if (NameEntry.text.toString().isEmpty() || DateEntry.text.toString().isEmpty() || LocationEntry.text.toString().isEmpty()||StoryEntry.text.toString().isEmpty()){
                Toast.makeText(this  , "All Fields With '*' must be populated" , Toast.LENGTH_LONG).show()
            }
            else if (PhotoSelected == false){
                Toast.makeText(this, "Please make sure you select a photo for this post" , Toast.LENGTH_LONG).show()
            }
            else if(StoryEntry.text.length < 10){
                Toast.makeText(this ,"The story must be at least 10 characters.." ,Toast.LENGTH_LONG).show()
            }
            else{
                PostButton.isEnabled=false
                personalupload()

            }
        }
        //Button Events
        clickhereforimage.setOnClickListener{
            selectphoto()
        }
        PostButton.setOnClickListener {
            PostStory()
        }
    }

        //making sure that a photo is selected
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        if (requestCode == 555 && resultCode== Activity.RESULT_OK && data != null){
            PhotoSelected = true
            val uridata  = data.data
            val bitmapforphoto = MediaStore.Images.Media.getBitmap(contentResolver ,uridata)
            val bitmapdraw = BitmapDrawable(bitmapforphoto)
            //gather photo data
            photouri = uridata
            imageofprofile.setImageResource(0)
            imageofprofile.setBackgroundDrawable(bitmapdraw)

        }





        super.onActivityResult(requestCode, resultCode, data)
    }
}