function prerequisitiesValidator (Prerequisities, Enrollment){
  // arg Prerequisities should be in this format:
  // Prerequisities = {"code":{"1": ["COMP9021", "COMP9024"],"2": ["COMP9020", "COMP9024"]},"UOC": 0}
  let canBeEnrolled = false;
  //console.log(Prerequisities.code, Enrollment);
  if (Prerequisities.code[1].length === 0 && Prerequisities.code[2].length === 0){
    //console.log('1');
    canBeEnrolled = true;
  }else if(Prerequisities.code[1].length >= 1 && Prerequisities.code[2].length === 0){
    //console.log('2');
    for(let course of Prerequisities.code[1]){
      if(Enrollment.includes(course)){
        canBeEnrolled = true;
        break;
      }
    }
  }else if(Prerequisities.code[1].length === 0  && Prerequisities.code[2] >= 1){
    //console.log('3');
    for(let course of Prerequisities.code[2]){
      if(Enrollment.includes(course)){
        canBeEnrolled = true;
        break;
      }
    }
  }else if(Prerequisities.code[1].length >= 1 && Prerequisities.code[2].length >=1 ){
    //console.log('4');
    let validatorCodeList1 = false;
    let validatorCodeList2 = false;
    for(let course of Prerequisities.code[1]){
      if(Enrollment.includes(course)){
        canBeEnrolled = true;
        break;
      }
    }
    for(let course of Prerequisities.code[2]){
      if(Enrollment.includes(course)){
        canBeEnrolled = true;
        break;
      }
    }
    if(validatorCodeList1 === true && validatorCodeList2 === true){
      canBeEnrolled = true;
    }
  }
  return canBeEnrolled;
}


