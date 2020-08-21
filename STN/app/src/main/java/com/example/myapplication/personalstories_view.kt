package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.recyclerview.widget.LinearLayoutManager
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.storage.FirebaseStorage
import kotlinx.android.synthetic.main.activity_personalstories_view.*

class personalstories_view : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_personalstories_view)




        val listallinfo = FirebaseStorage.getInstance().reference.child("${FirebaseAuth.getInstance().currentUser!!.email}/Posts/").listAll()
        listallinfo.addOnSuccessListener {
            PersonalTimeline.layoutManager= LinearLayoutManager(this)
            PersonalTimeline.adapter = PersonalAdapter(this  ,it.items.size )

        }
        listallinfo.addOnFailureListener {
            Toast.makeText(this, "issue loading data" , Toast.LENGTH_LONG).show()
        }

    }


}