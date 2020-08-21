package com.example.myapplication

import android.content.Context
import android.content.Intent
import android.nfc.Tag
import android.text.method.ScrollingMovementMethod
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.view.ViewParent
import android.widget.ImageView


import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

import androidx.recyclerview.widget.RecyclerView
import com.google.android.gms.tasks.Task
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.database.ValueEventListener
import com.google.firebase.database.ktx.getValue
import com.google.firebase.storage.FirebaseStorage
import com.google.firebase.storage.StorageMetadata
import com.google.firebase.storage.StorageReference
import com.google.firebase.storage.ktx.storageMetadata
import com.squareup.picasso.Picasso
import kotlinx.android.synthetic.main.activity_add_story.view.*
import kotlinx.android.synthetic.main.maintimelinelayoutcard.view.*
import kotlinx.android.synthetic.main.personalstorieslayout.view.*
import java.sql.Timestamp
import java.util.concurrent.ArrayBlockingQueue
import kotlin.properties.Delegates








    data class ContactValues(val email: String , val victimname :String , val phonenumber:String , val relationship :String , val postref :String )

    class MainAdapter(totalitems :Int, contextofparent:Context ) : RecyclerView.Adapter<ViewHolder>() {
        //Item Control

        var maxitemcount = totalitems
        var contextofparentvar= contextofparent

        fun ModifyUsableAndVisableWidgets(hlder: ViewHolder , opacityfororiginal:Float,opacityforprofile:Float, OrignalActiveStatus:Boolean , ProfileActivestatus:Boolean){
            //original widgets
            hlder.itemView.PostersProfile.alpha = opacityfororiginal
            hlder.itemView.user.alpha= opacityfororiginal
            hlder.itemView.Location.alpha = opacityfororiginal
            hlder.itemView.testimony.alpha = opacityfororiginal
            hlder.itemView.LikeButton.alpha = opacityfororiginal
            hlder.itemView.contactdownload.alpha = opacityfororiginal
            hlder.itemView.reportbutton.alpha =opacityfororiginal
            hlder.itemView.LocationImage.alpha = opacityfororiginal
            hlder.itemView.VictimImage.alpha = opacityfororiginal
            hlder.itemView.imageloadtext.alpha = opacityfororiginal
            hlder.itemView.Likes.alpha = opacityfororiginal
            //active status of originals
            hlder.itemView.imageloadtext.isEnabled = OrignalActiveStatus
            hlder.itemView.Likes.isEnabled = OrignalActiveStatus
            hlder.itemView.PostersProfile.isEnabled = OrignalActiveStatus
            hlder.itemView.user.isEnabled = OrignalActiveStatus
            hlder.itemView.Location.isEnabled = OrignalActiveStatus
            hlder.itemView.testimony.isEnabled = OrignalActiveStatus
            hlder.itemView.LikeButton.isEnabled = OrignalActiveStatus
            hlder.itemView.contactdownload.isEnabled = OrignalActiveStatus
            hlder.itemView.reportbutton.isEnabled = OrignalActiveStatus
            hlder.itemView.LocationImage.isEnabled = OrignalActiveStatus
            hlder.itemView.VictimImage.isEnabled= OrignalActiveStatus
            //Poster Profile Widgets
            hlder.itemView.BacktoPost.alpha = opacityforprofile
            hlder.itemView.Likedisplayimage.alpha = opacityforprofile
            hlder.itemView.likesofperson.alpha = opacityforprofile
            hlder.itemView.Memberstatus.alpha = opacityforprofile
            hlder.itemView.Memberstatustext.alpha = opacityforprofile
            hlder.itemView.MagnifiedProfileImage.alpha = opacityforprofile
            //active status of poster profile
            hlder.itemView.BacktoPost.isEnabled  = ProfileActivestatus
            hlder.itemView.Likedisplayimage.isEnabled = ProfileActivestatus
            hlder.itemView.likesofperson.isEnabled = ProfileActivestatus
            hlder.itemView.Memberstatus.isEnabled = ProfileActivestatus
            hlder.itemView.Memberstatustext.isEnabled = ProfileActivestatus
            hlder.itemView.BacktoPost.isEnabled = ProfileActivestatus
            hlder.itemView.MagnifiedProfileImage.isEnabled = ProfileActivestatus



        }

        fun updateimage(hlder: ViewHolder, urlinfo: String, imgref :ImageView){
            Picasso.get().setLoggingEnabled(true)
            Picasso.get().load(urlinfo).fit().into(imgref)
        }




        fun GatherUrlandMagnifyPosterImage(uidref: StorageMetadata,hlder: ViewHolder , imgref: ImageView){
            val uid = uidref.getCustomMetadata("UID")
            val ref  = FirebaseDatabase.getInstance().reference.child("Users").child(uid!!).child("userProfilepicuri")
            val changelisten = object :ValueEventListener{
                override fun onDataChange(snapshot: DataSnapshot) {
                    val info = snapshot.getValue<String>()

                    ModifyUsableAndVisableWidgets(hlder,0f , 1f , false , true)
                    updateimage(hlder , info!! , imgref)

                }

                override fun onCancelled(error: DatabaseError) {
                    Showtoast("Issue Loading Profile!")
                }
            }
            ref.addListenerForSingleValueEvent(changelisten)

        }

        fun Updatedatabasereportsorlikes(uidref :StorageMetadata ,  reportsorlikes:String , canceledkeyword:String){
            val uid = uidref.getCustomMetadata("UID")
            var ref = FirebaseDatabase.getInstance().reference.child("Users").child(uid!!).child(reportsorlikes)
            val changelisten = object : ValueEventListener{

                override fun onDataChange(snapshot: DataSnapshot) {
                    val info:Any? = snapshot.getValue<Any>()
                    //if the user have no "likes" or "reports" parameter in the database
                    if (info == null){
                       val initaltask = ref.setValue("1")
                        initaltask.addOnSuccessListener {

                        }
                        initaltask.addOnFailureListener {

                        }
                    }
                    //increasing the current likes or reports by 1
                    else{
                        val valuetoint = info!!.toString().toInt() + 1
                        val updatetask = ref.setValue(valuetoint)
                       updatetask.addOnSuccessListener {
                        }
                        updatetask.addOnFailureListener {
                        }
                    }
                }

                override fun onCancelled(error: DatabaseError) {
                    Showtoast("Issue Liking Post")
                }
            }
            ref.addListenerForSingleValueEvent(changelisten)



        }


        fun ToastDisplayAfterCallbackDatabase(task:Task<Void> ,successmessage:String , failuremessage:String){
            task.addOnSuccessListener {
                Showtoast(successmessage)
            }
            task.addOnFailureListener {
                Showtoast(failuremessage)
            }

        }

        fun ToastDisplayAfterCallbackStorage(task:Task<StorageMetadata> ,successmessage:String , failuremessage:String){
            task.addOnSuccessListener {
                Showtoast(successmessage)
            }
            task.addOnFailureListener {
                Showtoast(failuremessage)
            }

        }

        fun Showtoast(text:String){
            Toast.makeText(contextofparentvar , text , Toast.LENGTH_LONG).show()
        }




        fun downloadcontact(phonedownload :String, emaildownload: String , relationdownload:String , contactUIDdownload:String , victimnamedownload:String , postrefdownload:String){
            val contactinfo = ContactValues(emaildownload, victimnamedownload,phonedownload,relationdownload,postrefdownload)
            val ref=  FirebaseDatabase.getInstance().getReference().child("/Users/${FirebaseAuth.getInstance().currentUser!!.uid}/Contacts/${contactUIDdownload}")
            val valuetask = ref.setValue(contactinfo)
            ToastDisplayAfterCallbackDatabase(valuetask,
                "Contact Successfully Saved!!" ,
                "Issue Saving Contact , please try again!")


        }
        fun setonclickevents(holderref: ViewHolder , mtaref:StorageReference  , itref: StorageMetadata , contactref: String ) {
            holderref.itemView.LikeButton.setOnClickListener {
                val likes = itref.getCustomMetadata("Likes")
                val updatedlikes = likes!!.toInt() + 1
                val storagemtalikes = storageMetadata {
                    setCustomMetadata("Likes", updatedlikes.toString())
                }
               val likeupdatetask = mtaref.updateMetadata(storagemtalikes)
                ToastDisplayAfterCallbackStorage(likeupdatetask  ,"Post Successfully Liked!!" , "Error Liking post , please try again!!" )
                Updatedatabasereportsorlikes(itref,"likes", "Liking")



            }
            holderref.itemView.reportbutton.setOnClickListener {
                val reports = itref.getCustomMetadata("Reports")
                val updatedreports = reports!!.toInt() +1
                val storagemtareports = storageMetadata {
                    setCustomMetadata("Reports", updatedreports.toString())
                }
               val reportupdatetask = mtaref.updateMetadata(storagemtareports)
                ToastDisplayAfterCallbackStorage(reportupdatetask, "Post Reported to the STN Team!! We will review it ASAP!!" , "Error Reporting Post, please try again..")
                Updatedatabasereportsorlikes(itref, "reports" , "Reporting")

            }

             holderref.itemView.contactdownload.setOnClickListener {
                 val phonecontact = itref.getCustomMetadata("Phone Number")
                 val emailcontact = itref.getCustomMetadata("Email")
                 val relationshipcontact = itref.getCustomMetadata("Relationship")
                 val victimnamecontact = itref.getCustomMetadata("Name")
                 val contactUID = itref.getCustomMetadata("UID")
                 val postrefcontact = contactref
                 downloadcontact(phonecontact!!, emailcontact!!,relationshipcontact!!,contactUID!! , victimnamecontact!!,postrefcontact)
             }
            holderref.itemView.PostersProfile.setOnClickListener {
                GatherUrlandMagnifyPosterImage(itref,holderref, holderref.itemView.MagnifiedProfileImage )
            }
            holderref.itemView.BacktoPost.setOnClickListener {
                ModifyUsableAndVisableWidgets(holderref, 1f , 0f , true , false)
            }

        }
        fun updateitemlayout(itref: StorageMetadata, holderref: ViewHolder) {
            val name = itref.getCustomMetadata("Name")
            val location = itref.getCustomMetadata("Location")
            val story = itref.getCustomMetadata("Story")
            val likes = itref.getCustomMetadata("Likes")
            val email = itref.getCustomMetadata("Email")
            holderref.itemView.user.text = email.toString()
            holderref.itemView.testimony.text = story.toString()
            holderref.itemView.Location.text = location.toString()
            holderref.itemView.imageloadtext.text = name.toString()
            holderref.itemView.Likes.text = "Likes:${likes.toString()}"
            if (story!!.length > 200){
                holderref.itemView.ViewFullStory.alpha= 1f
                holderref.itemView.ViewFullStory.isEnabled = true

            }


        }



        override fun getItemCount(): Int {
            return maxitemcount

        }


            override fun onBindViewHolder(holder: ViewHolder, position: Int) {
                //increasing the itemcount if user reaches end of timeline

                holder.itemView.ViewFullStory.isEnabled = false


                var listallinfo =
                    FirebaseStorage.getInstance().getReference().child("MainTimeline/").listAll()
                listallinfo.addOnSuccessListener { listResult ->
                    //maintimelineattributes
                    var MainTimeLineAttributes = FirebaseStorage.getInstance().getReference()
                        .child("MainTimeline/${listResult.items[position].name}")
                    var ContactAttributes = FirebaseStorage.getInstance().getReference()
                        .child("MainTimeline/${listResult.items[position]}").toString()
                    //testing to see if url could be downloaded..
                    var urldownload = MainTimeLineAttributes.downloadUrl
                    urldownload.addOnSuccessListener {

                        //metadata attributes
                        var mda = MainTimeLineAttributes.metadata

                        mda.addOnSuccessListener {
                            updateimage(holder,urldownload.result.toString() , holder.itemView.VictimImage)
                            updateitemlayout(it, holder)
                            setonclickevents(holder, MainTimeLineAttributes, it , ContactAttributes)
                        }

                        mda.addOnFailureListener {
                            Showtoast("Issue downloading Info")
                        }
                    }
                    urldownload.addOnFailureListener {
                       Showtoast("Issue Downloading image")
                    }
                }

                    listallinfo.addOnFailureListener {
                      Showtoast("Issue Listing Data")
                    }
                }




        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
            val layoutinflation = LayoutInflater.from(parent?.context)
            val cellforrow = layoutinflation.inflate(R.layout.maintimelinelayoutcard, parent, false)
            return ViewHolder(cellforrow)

        }
    }



        class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {



        }
