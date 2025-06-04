fun main(){
    println(addContactDetail("Gladwin","0976787677","gladwin@gmail.com"))
    println(modifyContact("Meron","meron"))
    println(removeContactDetails("Meron"))
    retriveContactDetails()
}
data class ContactDetails(
    var name: String,
    var phoneNumber: String,
    var email: String
)
var contactDetails = mutableListOf<ContactDetails> (ContactDetails("Meron","0983532246","meron@gmail.com"),ContactDetails("Jowanita","0985657899","jewanita@gmail.com"))
//Adds Contact Details
fun addContactDetail( name: String, phoneNumber: String, email: String): MutableList<ContactDetails>{
    var newContactDetails = ContactDetails(name,phoneNumber,email)
    var updatedContactDetails = contactDetails.add(newContactDetails)
    return contactDetails
}
//Modifies Contact Details
fun modifyContact (name: String, newName: String): MutableList<ContactDetails>{
    contactDetails.forEach { contact ->
        if (contact.name.lowercase().contains(name.lowercase())){
            contact.name = newName

        }
    }
    return contactDetails
}

//Removes Contact Details
fun removeContactDetails(deletedname: String): MutableList<ContactDetails> {
    contactDetails.removeIf { contact ->
        contact.name.lowercase().contains(deletedname.lowercase())
    }
    return contactDetails
}
fun retriveContactDetails(){
    println(contactDetails)
}