function PersonalDetails(details){
    this.details = [details];

};
PersonalDetails.prototype.newContact = function(newDetail){
    this.details.push(newDetail);
    return this.details;
};
PersonalDetails.prototype.modify = function (modifiedData) {
    for(let key in this.details){
    if (modifiedData === this.details[key]){
        this.details[key] = modifiedData;
    }
}
return `${modifiedData} not in the list` 
}


PersonalDetails.prototype.removeDetail = function(removeDetail){
    let index = this.details.indexOf(removeDetail);
    if(index !== 1){
        this.details.splice(index,1);
        return `{removeDetail} has been removed`;
    }else{
        return`{removeDetail} not in the list`
    }
}
PersonalDetails.prototype.updatedDetails = function(){
    return this.details
    
}
const gladwine = new PersonalDetails({name: "Gladwine", school: "AkiraChix"});
gladwine.newContact({friend: "Meron"})
console.log(gladwine.updatedDetails());
gladwine.removeDetail({school:"Akirachix"});
gladwine.modify({food:"Rice"})






