package com.example.myapplication
import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import androidx.constraintlayout.widget.Placeholder
import androidx.recyclerview.widget.DividerItemDecoration
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.storage.FirebaseStorage
import com.google.firebase.storage.ListResult
import com.google.firebase.storage.StorageMetadata
import com.google.firebase.storage.StorageReference
import kotlinx.android.synthetic.main.activity_home.*


data class Contact(val ok :StorageReference){

}


class Home : AppCompatActivity() {
    // initial start with 20 items.... -> Onscrolled detects last position -> re-calls the sortlistfunction-> updates the adapter class with new final sortedarray and increase item count of adapter class
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_home)




        var cont  = applicationContext

        var listallinfo =
            FirebaseStorage.getInstance().getReference().child("MainTimeline/").listAll()
        listallinfo.addOnSuccessListener {


            val layoutmanager = LinearLayoutManager(this)
            var mainadapt = MainAdapter(it.items.size , cont)
            Timeline.layoutManager = layoutmanager
            Timeline.adapter = mainadapt
            Timeline.addOnScrollListener(object : RecyclerView.OnScrollListener(){
                override fun onScrolled(recyclerView: RecyclerView, dx: Int, dy: Int) {
                    if (layoutmanager.findLastVisibleItemPosition() == mainadapt.maxitemcount){
                        Toast.makeText(cont , "End Of Timeline Please Refresh Timeline!" ,Toast.LENGTH_LONG).show()
                    }
                }

            })
        }









        val divideritem = DividerItemDecoration(Timeline.context , 1)
        divideritem.setDrawable(getDrawable(R.drawable.dividerdraw)!!)
        Timeline.addItemDecoration(divideritem)

        tothetopbutton.setOnClickListener {
            finish()
            this.recreate()
            val restart = Intent(this , Home::class.java)
            startActivity(restart)
        }
        HelpButton.setOnClickListener {
            val action1 = Intent(this, HelpPage::class.java)
            startActivity(action1)
        }
        PostStoryButton.setOnClickListener {
            val action2 = Intent(this, AddStory::class.java)
            startActivity(action2)
        }
        ViewStoriesButton.setOnClickListener {
            val action3 = Intent(this , personalstories_view::class.java)
            startActivity(action3)
        }
        SettingsButton.setOnClickListener {



        }


    }
    override fun onBackPressed() {
        FirebaseAuth.getInstance().signOut()
        super.onBackPressed()
    }


}



