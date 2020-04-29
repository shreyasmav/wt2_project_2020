from django.shortcuts import render,redirect
from .models import Destination,Post1,comment1,ContactForm
from django.forms.models import model_to_dict
from django.http import JsonResponse,HttpResponse
from django.core import serializers
import json
from threading import Timer
from joblib import load

# Create your views here.
def main(request):
    return render(request,'main.html')
def login(request):
    if(request.method=="POST"):
        name1=request.POST["username"]
        password=request.POST["pass"]
        care=Destination.objects.all()
        if(len(care)==0):
            return render(request,'index1.html',{"Message":"Wrong username"})
        else:
            for i in care:
                if(name1==i.name and password==i.password):
                    return redirect("http://127.0.0.1:8000/blog/?username="+name1)
        return render(request,'index1.html',{"Message":"Wrong username"})

    return render(request,'index1.html')
def signup(request):
    if(request.method == "POST"):
        name1=request.POST["name"]
        care=Destination.objects.all()
        if(len(care)!=0):
            for i in care:
                if name1==i.name:
                    return render(request,'index.html',{"Message":"User_already exists"})
            email1=request.POST["email"]
            password1=request.POST["pwd"]
            #print(name1,email1,password1)
            details=Destination(name=name1,password=password1,email=email1)
            details.save()
            return redirect("http://127.0.0.1:8000/login/")
        else:
            email1=request.POST["email"]
            password1=request.POST["pwd"]
            #print(name1,email1,password1)
            details=Destination(name=name1,password=password1,email=email1)
            details.save()
            return redirect("http://127.0.0.1:8000/login/")
    return render(request,'index.html')
def blog(request):
    global name2
    name2=request.GET["username"]
    return render(request,'blog.html',{"name":name2})
def createblog(request):
    print(name2)
    if(request.method=="POST"):
        username=name2
        title=request.POST["title"]
        description=request.POST["textarea1"]
        extracted_model = load("nb_model.joblib")
        extracted_cv = load("vector.joblib")
        msg = description
        msgInput = extracted_cv.transform([msg])
        predict = extracted_model.predict(msgInput)
        if(predict==0):
            spam=1
        else:
            spam=0
        details=Post1(name1=name2,title=title,description=description,spam=spam)
        details.save()
        return redirect("http://127.0.0.1:8000/blog/?username="+name2)
    return render(request,'createblog.html',{"name":name2})
def allblogs(request):
    blogs=Post1.objects.all()
    dict1={}
    for i in blogs:
        if i.count in dict1:
            dict1[i.count].append(i.pk)
        else:
            dict1[i.count]=[i.pk]
    list1=[]
    print(dict1)
    for i in sorted(dict1,reverse=True):
        for j in dict1[i]:
            for k in blogs:
                if(k.pk==j):
                    list1.append(k)
                    break
    return render(request,'allblogs.html',{'blogs':list1})

// for bodyparser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended : true}));

function getSum(array) {
  return array.reduce(function (r, a) {
      return r + a;
  }, 0);
}

// ----------------------------------------------------get the user infomation for display in studentprofile ---------------------

app.get('/api/user/:id', (req, res) => {
  const userInfo = new Promise((resolve, reject) => {
    MongoClient.connect(url, {useNewUrlParser: true}, function(err, db){
      if (err) reject(err);
      let dbo =db.db('coursetest');
      dbo.collection("User").findOne({_id: parseInt(req.params.id)}, function(err, result){
        if (err) reject (err);
        db.close();
        resolve(result);
      });
    });
  });
  userInfo.then((result) => {
    //console.log(res);
    res.json({username : result})    //// TEMP: need use "then" to load user's trasction, until both info loaded,then return to front-end.
  })
  .catch((err) => {
    console.log(`Opz, something wrong, the error message is ${err}`);
  });
});




// ----------------------------------------------------get the enrollment info ---------------------
app.get('/api/enrollment/:id', (req, res) => {
  const enrollmentInfo = new Promise((resolve, reject) => {
    mongoose.connect(url+'coursetest')
    .then(
      () => {
        console.log('Database connect')
      },
      err => { console.log(err) }
    )

  enrollmentModel
    .find({'user': parseInt(req.params.id)})
    .exec(function(err, docs){
      if (err) return handleError(err);
      //console.log('docs', docs);
      for( let enroll of docs){
        //console.log(enroll.course_list)
        var enroll_list = [];
        var nb_of_course = enroll.course_list.length;
        for( let course of enroll.course_list) {
          //console.log('coursename',course)
          courseModel
            .findOne({'_id': course._id})
            .lean()
            .exec(function(e, result) {
              if (e) {
                console.log(e);
              }
              enroll_list.push(result)
              //console.log('enroll_list', enroll_list);
              mongoose.disconnect();
              if (enroll_list.length === nb_of_course){
                //console.log(enroll_list);
                resolve(enroll_list);
              }
            });
        }
      }
    })
  }) // promise end
  //console.log(enroll_list);
  enrollmentInfo.then( enroll_list => {
      return res.json(enroll_list);
  })
});



// ----------------------------------------------------get the course review info ---------------------
app.get('/api/review/:id',(req,res) => {
  // connect database
  // by data schema provided by mongoose
  const courseReview = new Promise((resolve,reject) => {
    mongoose.connect(url + 'coursetest')
    .then(
      () => {
        console.log('Database connect');
      },
      err => {
        console.log(err);
      }
    )

  // get user-course-star information from enrollment table
    enrollmentModel
    .find({
      'user': parseInt(req.params.id)
    })
    .populate('course_list._id')
    .exec(function(err, docs){
      if (err) return handleError(err);
      var reviewList = [];

      // no data searched
      if (docs[0] === undefined){
        reviewList = [];      
      }

      // searching data success
      else{
        docs[0].course_list.forEach(course => {
          reviewList.push({'code' : course._id.code, 'name': course._id.name, 'star':course.star,'term': course._id.term});    
        });
        resolve(reviewList);
        mongoose.disconnect();
    
      }})
  })

  // send json data to frontend 
  courseReview
    .then( reviewList => {
      return res.json(reviewList
      );
    })
});

                comment_array.append((i.comment,i.name1))
    return render(request,'comment.html',{'comments':comment_array})
